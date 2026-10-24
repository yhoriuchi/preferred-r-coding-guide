# My Preferred R Coding Guide: readable end-to-end analysis
# What this code is about: Clean a small synthetic survey, document exclusions,
# estimate a treatment contrast, and save figures and their numerical source.
# Unit of observation: One synthetic survey respondent.
# Inputs: Synthetic records defined below; no private or external data.
# Outputs: examples/output/ and examples/figures/ (listed at the end).
# Author: Codex, for Yusaku Horiuchi
# Last updated: 2026-10-24

# Initial settings --------------------------------------------------------

library(tidyverse)
library(ggthemes)
library(estimatr)

output_dir <- "examples/output"
figure_dir <- "examples/figures"

# These folders are included with the guide. Run from the guide's root.
stopifnot(dir.exists(output_dir), dir.exists(figure_dir))

# Read the demonstration data ---------------------------------------------

# Artificial values for illustrating code style, not empirical evidence.
# -99 means missing outcome; a blank group means unknown assignment.
raw_data <- tribble(
  ~respondent_id, ~treatment, ~outcome,
  "001", "Control", 3,
  "002", " control ", 4,
  "003", "CONTROL", 2,
  "004", "Control", 5,
  "005", "Control", -99,
  "006", "Treatment", 6,
  "007", " treatment ", 5,
  "008", "TREATMENT", 7,
  "009", "Treatment", 4,
  "010", "Treatment", 6,
  "011", "", 3,
  "012", "Control", 4
)

# Inspect the original data -----------------------------------------------

glimpse(raw_data)
raw_data |>
  count(treatment, outcome) |>
  print()

duplicate_ids <- raw_data |>
  count(respondent_id) |>
  filter(n > 1)

stopifnot(nrow(duplicate_ids) == 0)

# Clean and prepare variables ---------------------------------------------

cleaned_data <- raw_data |>
  mutate(
    treatment_original = treatment,
    treatment = str_trim(treatment) |> str_to_lower(),
    treatment = na_if(treatment, ""),
    outcome_original = outcome,
    outcome = na_if(outcome, -99)
  )

# Check the vocabulary before factor conversion can hide unexpected values.
unexpected_groups <- cleaned_data |>
  filter(!is.na(treatment), !treatment %in% c("control", "treatment"))

stopifnot(nrow(unexpected_groups) == 0)

cleaned_data <- cleaned_data |>
  mutate(treatment = factor(treatment, levels = c("control", "treatment")))

cleaned_data |>
  count(treatment_original, treatment) |>
  print()

# Check the analysis sample -----------------------------------------------

# Exclusion categories are mutually exclusive, in the order shown here.
sample_accounting <- cleaned_data |>
  mutate(status = case_when(
    is.na(treatment) ~ "Missing treatment",
    is.na(outcome) ~ "Missing outcome",
    TRUE ~ "Included"
  )) |>
  count(status, name = "n_respondents")

sample_accounting

analysis_data <- cleaned_data |>
  drop_na(treatment, outcome)

stopifnot(
  nrow(analysis_data) == 10,
  sum(sample_accounting |> pull(n_respondents)) == nrow(raw_data),
  all(analysis_data |> pull(outcome) >= 1),
  all(analysis_data |> pull(outcome) <= 7)
)

# Summarize the data -------------------------------------------------------

group_summary <- analysis_data |>
  group_by(treatment) |>
  summarise(
    n_respondents = n(),
    mean_outcome = mean(outcome),
    .groups = "drop"
  )

group_summary

# Estimate the model ------------------------------------------------------

# Illustrative unadjusted contrast: treatment minus control.
# HC2 and a 95% interval are explicit choices for this example, not defaults
# for every research design. These synthetic observations are independent.
treatment_model <- lm_robust(
  outcome ~ treatment,
  data = analysis_data,
  se_type = "HC2",
  alpha = 0.05
)

model_results <- broom::tidy(treatment_model) |>
  select(term, estimate, std.error, conf.low, conf.high, p.value)

model_results

plot_data <- model_results |>
  filter(term == "treatmenttreatment") |>
  mutate(comparison = "Treatment vs. control")

# The plotted contrast must equal the difference in the two group means.
mean_control <- group_summary |>
  filter(treatment == "control") |>
  pull(mean_outcome)

mean_treatment <- group_summary |>
  filter(treatment == "treatment") |>
  pull(mean_outcome)

stopifnot(
  nrow(plot_data) == 1,
  isTRUE(all.equal(
    plot_data |> pull(estimate),
    mean_treatment - mean_control
  ))
)

# Make the figures --------------------------------------------------------

plot_data

effect_plot <- ggplot(
  plot_data,
  aes(x = estimate, y = comparison)
) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "gray60") +
  geom_linerange(aes(xmin = conf.low, xmax = conf.high), orientation = "y") +
  geom_point(size = 2.5) +
  labs(x = "Difference in mean outcome (scale points)", y = NULL) +
  theme_few(base_size = 12)

# Preview in RStudio; batch execution saves only the named files below.
if (interactive()) {
  print(effect_plot)
}

sample_plot <- ggplot(
  group_summary,
  aes(x = treatment, y = n_respondents)
) +
  geom_col(fill = "gray60", width = 0.6) +
  geom_text(aes(label = n_respondents), vjust = -0.4) +
  scale_x_discrete(labels = c(control = "Control", treatment = "Treatment")) +
  scale_y_continuous(
    breaks = 0:5,
    expand = expansion(mult = c(0, 0.12))
  ) +
  labs(x = NULL, y = "Number of respondents") +
  theme_few(base_size = 12)

if (interactive()) {
  print(sample_plot)
}

# Save outputs ------------------------------------------------------------

write_rds(analysis_data, file.path(output_dir, "analysis_data.rds"))
write_csv(sample_accounting, file.path(output_dir, "sample_accounting.csv"))
write_csv(group_summary, file.path(output_dir, "group_summary.csv"))
write_csv(model_results, file.path(output_dir, "model_results.csv"))
write_csv(plot_data, file.path(output_dir, "effect_plot_data.csv"))

ggsave(
  file.path(figure_dir, "treatment_effect.pdf"),
  plot = effect_plot,
  width = 6.5,
  height = 1.6,
  units = "in"
)

ggsave(
  file.path(figure_dir, "treatment_effect.png"),
  plot = effect_plot,
  width = 6.5,
  height = 1.6,
  units = "in",
  dpi = 150
)

ggsave(
  file.path(figure_dir, "sample_counts.png"),
  plot = sample_plot,
  width = 5,
  height = 3.5,
  units = "in",
  dpi = 150
)

figure_caption <- str_c(
  "Synthetic example: treatment-minus-control difference in mean outcome. ",
  "The point is an unadjusted OLS estimate; the line is a 95% confidence ",
  "interval using HC2 robust standard errors. Ten artificial respondents ",
  "have observed treatment and outcome. The dashed line marks zero. ",
  "These numbers illustrate coding style and are not research findings."
)

write_lines(figure_caption, file.path(output_dir, "figure_caption.txt"))
write_lines(capture.output(sessionInfo()), file.path(output_dir, "session_info.txt"))

# Verification ------------------------------------------------------------

saved_data <- read_rds(file.path(output_dir, "analysis_data.rds"))
stopifnot(identical(saved_data, analysis_data))
stopifnot(file.exists(file.path(figure_dir, "treatment_effect.pdf")))

# Restart R and rerun this script from the guide's root directory.
# Open the saved figures; check labels, uncertainty, and final-size legibility.
