# My Preferred R Coding Guide

**Yusaku Horiuchi · Created October 24, 2026 · Version 1.0**

## 1. The Goal: Code I Can Immediately Understand

AI may do the cleaning, wrangling, analysis, and visualization. The resulting R scripts should still feel familiar to me: I should be able to open a script, see what it does, follow every consequential step, inspect the intermediate data, and understand its outputs quickly.

Optimize for **my comprehension, analytical correctness, and reproducibility**, in that order of presentation—not for the shortest code or the most sophisticated implementation. Correctness remains a requirement: familiar-looking code must never conceal an analytical change.

This guide translates my explicit requests and Waseda University 2026 teaching materials into an actionable coding profile. It is a guide for working with me, not a claim that there is only one good way to write R.

### How to use this guide

1. Give the AI this complete guide and the project's existing scripts, README, and relevant data documentation.
2. State the substantive question, expected output, and any project or journal requirements.
3. Require readable scripts, inspectable intermediate objects, saved outputs, and a brief verification report.
4. Use the [script template](templates/analysis_script.R) for a new analysis. For a working example, run [the end-to-end demonstration](examples/01_readable_analysis.R) from this guide's root folder.

The [application prompt](APPLY_GUIDE.md) can be pasted into another AI chat. The guide must be available in that chat or project; a reference to a file the AI cannot read is insufficient.

### Evidence and authority

The labels below distinguish what was requested from what was inferred:

| Label | Meaning | How to apply it |
|---|---|---|
| **Confirmed** | Explicitly requested in the October 24, 2026 request, or recorded as confirmed in the existing R/figure reference | Follow unless a later explicit instruction or a stronger project requirement applies. |
| **Course-derived** | A stated preference or repeated pattern in the supplied teaching materials | Use as this guide's working default; do not claim it has independently become a universal operating rule. |
| **Recommendation** | An implementation choice added to make the user's goal reliable | Explain consequential choices. It is not a newly confirmed personal preference. |
| **Context-specific** | A teaching exercise, optional advanced technique, illustration, or deliberate counterexample | Apply only in the relevant context. |

The latest explicit task instruction comes first. Next come applicable project and journal requirements, confirmed personal preferences, and the course-derived profile. A necessary exception should be narrow and explained beside the code. This new guide does not itself modify the global operating manual or install instructions in other projects.

The source audit covers **all 35 `.R` files, including two revised versions, ten paired bad/better visualization demonstrations, and one screenshot copy**. It also examines the course style document, the workflow handout, and seven substantive Technical Notes. The [evidence report](analysis/EVIDENCE.md) records limitations and conflicting examples; the archive inventory preserves file names and checksums. The course programs were read and parsed, not all executed against their original datasets or live websites.

## 2. The Core Coding Profile

| Area | Preferred behavior | Status |
|---|---|---|
| Purpose | Every script says **“What this code is about”** near the top | Confirmed |
| Navigation | Use RStudio section comments, created with Insert Section when editing interactively | Confirmed |
| Data work | Use tidyverse consistently; avoid ordinary `[]`, `[[]]`, and `$` extraction where a clear tidyverse alternative exists | Confirmed; `[[]]` preference is the natural extension of avoiding bracket extraction |
| Formatting | Follow the tidyverse style guide, use `styler`, and apply compatible Google guidance | Confirmed; conflicts are resolved explicitly below |
| Pipes | Native `\|>` in new scripts; preserve an established legacy `%>%` style when maintaining it | Existing reference and course-derived |
| Structure | Explicit package loading, relative paths, small readable steps, useful comments | Existing reference and course-derived |
| Intermediate objects | Make the data used for a figure or model visible and inspectable | Course-derived |
| Static figures | Start from `theme_few()` | Confirmed |
| Publication figures | Readable at final size; direct identification; compact layout; titles in manuscript captions | Previously confirmed |
| Completion | Format, run from a clean session, inspect saved outputs, and report actual verification | Existing reference and course-derived |

## 3. Every Script Needs a Purpose and a Reading Order

**Confirmed / course-derived.** Start with single-`#` comments. Do not surround the opening header with decorative rules. State the purpose in substantive language, not merely “data analysis.” Name the inputs, outputs, unit of observation, and important scope choices when they help the reader.

```r
# Survey project: prepare the analysis sample
# What this code is about: Clean responses, compare treatment groups,
# and save an estimate plot that can be checked against the results table.
# Unit of observation: One survey respondent.
# Inputs: data/raw/responses.csv
# Outputs: data/derived/analysis_data.rds; figures/treatment_effect.pdf
# Author: Yusaku Horiuchi, with AI assistance
# Last updated: YYYY-MM-DD
```

Use truthful author and date information. The template's placeholders must be completed before handoff. Do not claim that I personally wrote or verified AI-produced code.

Use recognizable stages:

```r
# Initial settings --------------------------------------------------------
# Read data ---------------------------------------------------------------
# Inspect the original data -----------------------------------------------
# Clean and prepare variables ---------------------------------------------
# Check the analysis sample -----------------------------------------------
# Summarize the data -------------------------------------------------------
# Estimate models ---------------------------------------------------------
# Make figures ------------------------------------------------------------
# Save outputs ------------------------------------------------------------
# Verification ------------------------------------------------------------
```

Adapt these headings to the script. A tiny script does not need ten empty sections. Headings should describe the work: “Check unmatched country names” is more useful than “Step 7.”

RStudio's **Insert Section** shortcut is **Cmd + Shift + R on macOS** and **Ctrl + Shift + R on Windows/Linux**. A comment ending with at least four dashes is recognized as a section. When an AI writes the file directly, it should produce this same syntax; it should not pretend to have pressed a keyboard shortcut. See the [official RStudio documentation](https://docs.posit.co/ide/user/ide/guide/code/code-sections.html).

Keep the narrative visible from top to bottom. Put a helper function before its first use, under a descriptive heading. Avoid sourcing a chain of obscure helpers merely to perform a short analysis.

## 4. Formatting: Tidyverse, Google, and My Own Profile

**Confirmed / course-derived.** Use two spaces for indentation, `<-` for object assignment, double quotes for strings, spaces around ordinary operators, and one main operation per line. Break long calls across lines, with one significant argument per line and the closing parenthesis on its own line. Aim for about 80 characters, while keeping unavoidable paths and URLs intact. Use complete `TRUE` and `FALSE`.

Use lowercase `snake_case` for new files, objects, and functions. Prefer meaningful nouns for data objects and verbs for functions: `analysis_data`, `group_summary`, `treatment_model`, `make_effect_plot()`. Preserve original data-column names until a deliberate, documented rename. Existing course names such as `US_rank`, `primes.L`, and `Figure1.pdf` are not new naming defaults.

These formatting rules follow the [tidyverse syntax guide](https://style.tidyverse.org/syntax.html), interpreted with the source materials' preference for readable steps.

### The two external guides are not identical

[Google's current R guide](https://google.github.io/styleguide/Rguide.html) is derived from the tidyverse guide but makes several different choices. Literal compliance with both is impossible in those areas.

| Question | Google-specific convention | Working profile for this guide |
|---|---|---|
| Function names | `BigCamelCase` | `snake_case`, matching the course and existing reference |
| Function results | Explicit `return()` | An obvious final expression is acceptable; use `return()` for an early exit or when it clarifies the result |
| External functions | Generally qualify with `package::function()` | Load core packages at the top; qualify ambiguous or occasional functions explicitly |
| Custom argument names | Not the course's dot-prefix convention | Use descriptive dot-prefixed arguments where they help distinguish inputs from columns |

This is a **course-matched interpretation**, not a declaration of complete Google compliance. The compatible Google principles include using `styler`, avoiding `attach()`, and avoiding right-hand assignment. If a project explicitly requires strict Google style, record that exception and use its full convention consistently. Do not silently switch naming or namespace styles halfway through a script.

### Use `styler`, then read the result

In RStudio, use **Addins → Style active file** or **Style selection**. For a specific saved script:

```r
styler::style_file("scripts/01_clean_data.R")
```

Format only the files being worked on unless broader reformatting is requested. Review the changes and rerun the script. `styler` improves formatting; it does not verify the estimand, sample, joins, missing-data decisions, plotting choices, or compliance with this personal profile. It does not automatically rewrite all base R as tidyverse. See the [styler documentation](https://styler.r-lib.org/).

## 5. Packages, Projects, and Paths

**Course-derived / existing reference.** Load the packages needed for the script near the beginning, with unquoted names:

```r
library(tidyverse)
library(ggthemes)
library(estimatr)
```

Do not add packages just because they are familiar to the AI. For a function outside the core workflow, `broom::tidy()` or `dplyr::select()` can make its origin clear and prevent a conflict. The course's introductory namespace restriction does not prohibit useful namespace qualification in research code.

Installation belongs in a separate setup step. The workflow handout expresses a strong preference for manual installation through RStudio's Packages pane. Do not place `install.packages()` or automatic update logic in an ordinary analysis script. Explain a missing dependency rather than changing the environment invisibly.

Open the project through its `.Rproj` file and work from the project root. Use forward slashes and relative paths. Use `file.path()` when assembling components. Avoid `setwd()` pointing to a personal computer, absolute Dropbox paths, `file.choose()`, and reliance on a previously restored `.RData` workspace.

Preserve raw/received data. Put derived data, tables, and figures in their intended folders. Keep stable, descriptive filenames and consistent numbering. When adding a new analytical layer, preserve existing scripts and use a new clearly numbered script unless an in-place revision was requested.

For classroom materials, use the supplied folders or the manual folder-creation instructions. In research code, explicit directory creation can be reasonable; the classroom restriction on `dir.create()` is not universal.

## 6. Think in Tibbles and Visible Transformations

**Confirmed / course-derived.** Prefer the tidyverse vocabulary throughout ordinary rectangular-data work:

| Task | Preferred tools | Make explicit |
|---|---|---|
| Read/write | `read_csv()`, `read_rds()`, `write_csv()`, `write_rds()` | Types, missing codes, filenames |
| Keep rows/columns | `filter()`, `select()`, `slice_*()` | Conditions, selected fields, ordering |
| Create/rename | `mutate()`, `rename()`, `relocate()` | Definitions and units |
| Count/summarize | `count()`, `group_by()`, `summarise()` | Group, denominator, missing handling |
| Reshape | `pivot_longer()`, `pivot_wider()` | The new row unit and keys |
| Combine | `left_join()`, `anti_join()`, `bind_rows()` | Keys and row retention |
| Strings | `str_detect()`, `str_replace()`, `str_trim()`, `str_c()` | Matching and replacement rules |
| Categories | `fct_relevel()`, `fct_reorder()`, `fct_recode()` | Reference, display order, labels |
| Dates | `ymd()`, `mdy()`, `make_date()`, `year()`, `month()` | Format, fiscal/calendar interpretation |
| Repetition | A readable function with `map()` and `list_rbind()` | Input and output of one iteration |

Keep a pipeline focused on one understandable transformation. Split it when the unit of observation changes, an important check is needed, or the result feeds multiple outputs. Do not invent a rigid maximum number of pipe steps.

```r
analysis_data <- raw_data |>
  filter(year >= 2000) |>
  mutate(country = str_trim(country))

country_summary <- analysis_data |>
  group_by(country) |>
  summarise(
    n_observed = sum(!is.na(outcome)),
    mean_outcome = mean(outcome, na.rm = TRUE),
    .groups = "drop"
  )
```

This short example assumes each country has an observed outcome. In an actual dataset, check that condition or handle an all-missing group explicitly. A pipe is not a reason to hide data validation.

Names such as `df1` and `df2` are common in short teaching exercises. In a longer research script, use names that expose purpose and stage. Avoid both anonymous chains and dozens of disposable objects with no meaningful distinction.

## 7. Minimize Brackets and Dollar Extraction

**Confirmed.** Prefer operations that state what is happening:

| Instead of ordinary extraction | Prefer |
|---|---|
| `df[df$year >= 2000, ]` | `df \|> filter(year >= 2000)` |
| `df[, c("country", "year")]` | `df \|> select(country, year)` |
| `df$outcome` | `df \|> pull(outcome)` |
| `df$outcome <- ...` | `df <- df \|> mutate(outcome = ...)` |
| `x[1]` when the first value is intended | `first(x)` |
| `tables[["results"]]` | `pluck(tables, "results")` |
| `coef(model)[2]` | Tidy the model and select the coefficient by its term |

`select(outcome)` returns a one-column data frame; `pull(outcome)` returns a vector. State which is needed. A filtered `pull()` is not automatically a scalar: check that exactly one row matches when a single value is required. Use `slice()` only when row position has a defined meaning; prefer an identifier filter otherwise.

**Necessary exceptions are allowed.** A matrix API, an object without a suitable accessor, or tidy evaluation may require brackets. For a column whose name is supplied as a string, `.data[[.variable]]` is an established tidyverse pattern inside data-masking contexts. It is different from casually extracting columns with `df$column`. Do not contort the code to remove it. Explain unfamiliar syntax once, close to the function. See [Programming with dplyr](https://dplyr.tidyverse.org/articles/programming.html).

The archive itself contains bracket and dollar examples, particularly in R-language and programming lessons. Their presence does not override the current request to minimize them.

## 8. Inspect Before Cleaning, and Show What Changed

**Course-derived, with recommended checks.** Inspect `glimpse()`, `count()`, `distinct()`, and selected rows before deciding how to clean. Know what one row represents. Check identifiers before treating repeated rows as duplicates.

For each consequential recode, make the original and cleaned values easy to compare:

```r
cleaned_data <- raw_data |>
  mutate(
    state_original = state,
    state = str_trim(state),
    state = case_when(
      state == "D.C." ~ "District of Columbia",
      state == "Lousiana" ~ "Louisiana",
      TRUE ~ state
    )
  )

cleaned_data |>
  count(state_original, state, sort = TRUE)
```

These particular corrections come from the mass-shooting exercise. They illustrate an explicit correction table; do not apply them blindly to unrelated data. Avoid fuzzy matching, automatic deduplication, imputation, or outlier deletion unless the task and source documentation justify them.

Use explicit readr missing codes and column types when needed. Identifiers with leading zeros are often character values. `show_col_types = FALSE` hides a type message, not parsing problems; inspect `problems()` for imported text data. Keep the original text when a parsing decision is consequential.

Use `str_*()` for text. Explain unfamiliar regex patterns in plain language and check matched values. Distinguish `str_replace()` from `str_replace_all()`. Do not treat “at least 100” or “100–200” as an exact value of 100 simply because `parse_number()` can extract it. A parser is not a substantive coding rule.

Normalize new names deliberately. Backticks are appropriate when referring to incoming names with spaces or symbols. Human-readable figure labels belong in labels or a mapping table; they need not become awkward working column names.

## 9. Missing Values, Denominators, and Grouping

**Course-derived, with recommended checks.** Use `is.na()`; never compare a value to `NA` with `==` or `!=`. Distinguish true missing values, literal strings such as `"NA"`, and meaningful zeroes. Do not convert all missing values to zero.

Apply `drop_na()` to the columns required for the particular analysis. A blanket `drop_na()` can remove observations because of irrelevant fields. Report the number of rows retained and excluded. Make the denominator explicit when calculating shares or means.

`na.rm = TRUE` is an analytical choice, not an automatic fix. If a whole group is missing, `sum(..., na.rm = TRUE)` returns zero and `mean(..., na.rm = TRUE)` returns `NaN`. Preserve the distinction between “nothing observed” and “observed zero.”

```r
group_summary <- cleaned_data |>
  group_by(group) |>
  summarise(
    n_rows = n(),
    n_observed = sum(!is.na(outcome)),
    mean_outcome = if (all(is.na(outcome))) {
      NA_real_
    } else {
      mean(outcome, na.rm = TRUE)
    },
    .groups = "drop"
  )
```

Understand the difference between `group_by() |> mutate()` (retains rows) and `group_by() |> summarise()` (collapses rows). End grouping when it has served its purpose: use `.groups = "drop"` in a summary, or `ungroup()` after grouped mutations. Do not add redundant `ungroup()` after every operation without understanding the result.

For a top-five result **within each year**, explicitly group by year at the ranking step. Removing every group and then taking five rows gives a global ranking. Decide how ties should be handled; `slice_max()` can return more than `n` rows by default. `reframe()` is useful for multiple results per group and returns ungrouped data; it is not a reason to replace every simple summary.

## 10. Reshape and Join Without Hiding the Row Unit

**Course-derived / recommendation.** Before and after `pivot_longer()` or `pivot_wider()`, state what one row represents and check the relevant key. Choose columns explicitly or use a deliberate helper such as `starts_with()` or `all_of()`. Avoid selecting by position when column order can change.

`values_drop_na = TRUE` removes missing cells during reshaping. Use it only when those missing cells should not remain as observations. `fill()` is appropriate for carried-down headings in an administrative table; it is not a general imputation rule. Remove subtotal and total rows deliberately to avoid double counting. In fiscal-year data, document how October–December map to calendar years rather than copying the course's year constants.

For a join, state the key and intended relationship. The course repeatedly checks unmatched labels with `anti_join()` before joining. Make that check visible:

```r
unmatched <- observations |>
  anti_join(country_lookup, by = "country")

duplicate_keys <- country_lookup |>
  count(country) |>
  filter(n > 1)

unmatched
duplicate_keys

stopifnot(nrow(unmatched) == 0, nrow(duplicate_keys) == 0)

joined_data <- observations |>
  left_join(
    country_lookup,
    by = "country",
    relationship = "many-to-one",
    na_matches = "never"
  )

stopifnot(nrow(joined_data) == nrow(observations))
```

This example assumes every observation should match one lookup row. If unmatched rows are legitimate, retain and explain them instead of imposing this assertion. `relationship` and `na_matches` make important join assumptions executable; they are recommended safeguards rather than literal course syntax. See the [dplyr join reference](https://dplyr.tidyverse.org/reference/mutate-joins.html).

A map can have many polygon vertices for one geographic identifier. Repeated polygon keys are not automatically errors. Keep the full map with a suitable `left_join()`, and check that the **summary being joined to it** has the intended key. An inner join can silently remove geographic units.

## 11. Factors and Dates Are Analytical Choices

**Course-derived.** Use `fct_relevel()` for a reference or deliberate order, `fct_reorder()` for ordering by a numeric quantity, and `fct_recode()` for changing labels. Check the result with `count()` or `levels()` after `pull()`. Do not let alphabetical ordering choose the reference group accidentally.

The values inside a factor are stored as integers. Do not use `as.numeric(factor_value)` as if it recovered the original numeric data. Treat explicit conversion to factor positions for plotting as a documented exception.

Use date parsers that match the source (`mdy()`, `dmy()`, or `ymd()`). Check failed parsing and date ranges. Keep dates as dates until presentation. Avoid manual substring extraction when a clear date parser expresses the intended operation, while preserving special parsing needed for unusual source formats.

Order time-series data before using `lag()`, `first()`, `last()`, or cumulative calculations. Choose factor order, calendar mapping, ranking direction, and treatment baselines because of their meaning, not for a convenient-looking plot.

## 12. Model Code Should Reveal the Statistical Design

**Course-derived / recommendation.** Show the outcome, treatment or explanatory variables, reference category, analysis sample, estimator, uncertainty method, weights, and clustering where applicable. These decisions come from the research design; a style guide cannot choose them.

The modeling precept uses `estimatr::lm_robust()` and tidies its output before plotting. Preserve that readable sequence where the model is appropriate. Do not substitute robust standard errors, a different estimator, a different sample, or a different confidence level as a cosmetic improvement.

```r
treatment_model <- lm_robust(
  outcome ~ treatment,
  data = analysis_data,
  se_type = "HC2",
  alpha = 0.05
)

model_results <- broom::tidy(treatment_model) |>
  select(term, estimate, std.error, conf.low, conf.high, p.value)

model_results
```

Here HC2 and 95% intervals are illustrative choices, made explicit. They are not universal methodological defaults. Use `broom::tidy()` or the model's documented tidier rather than extracting an unexplained coefficient position.

For figures, identify the intended terms by name. Removing an intercept is appropriate only when the figure should show contrasts rather than the baseline. Check that all intended terms are present. Label terms through an explicit mapping; do not classify every unfamiliar coefficient as a second treatment category using a catch-all `if_else()`.

Keep several explicit model calls if they are easiest to read. Only after one model is understood should a helper or repeated-model workflow replace repetition. Display a formula assembled from strings before fitting it. Keep the sample size and exclusions available for each specification.

A subgroup difference needs an appropriate comparison or interaction analysis; different significance levels alone do not establish a difference. This is a methodological safeguard, not a coding preference inferred from the class exercise.

## 13. Functions and Repetition: Explain One Case First

**Course-derived.** Custom functions should solve a concrete repetition problem. Start from a working, inspectable single case, then wrap that logic in a short named function. Explain its input, output, and any consequential assumption. Use simple `if`/`else` checks with informative errors when needed.

The course explicitly describes dot-prefixed input names as a useful personal convention: `.file`, `.universities`, `.vars`, `.year`, and `.limits`. Prefer this pattern for new custom analytical helpers when it clarifies the distinction between arguments and data columns. It is not perfectly consistent in the source, and it is not a general tidyverse rule. Use `.dataframe` rather than `.data` for a custom data argument when the `.data` pronoun is also needed.

```r
# Return one row per group with its number of observed outcomes.
count_observed <- function(.dataframe, .group, .outcome) {
  .dataframe |>
    group_by({{ .group }}) |>
    summarise(
      n_observed = sum(!is.na({{ .outcome }})),
      .groups = "drop"
    )
}

count_observed(analysis_data, treatment, outcome)
```

`{{ .group }}` means that the argument is supplied as an unquoted column name. If a character column name is needed instead, use the documented `.data[[.variable]]` pattern. Do not introduce `eval(parse())`, intricate quasiquotation, or dynamic object creation when a plain function or named list would be clearer.

For several input files, make a visible file list, test the function on one file, and then use `map()` followed by `list_rbind()`. Add a source filename column where it helps trace the rows. The course already presents this two-step alternative; current [purrr documentation](https://purrr.tidyverse.org/reference/map_dfr.html) recommends it over the superseded `map_dfr()` family. Existing working `map_dfr()` code need not be rewritten without a reason.

A straightforward loop remains acceptable when it is easier to understand. If indexing is necessary, use `seq_along()` rather than `1:length()`. Do not turn the preference for tidyverse into an absolute ban on base R functions such as `mean()`, `sum()`, `lm()`, `file.path()`, or `stopifnot()`.

## 14. Prepare the Plot Data Before Drawing the Plot

**Course-derived, strongly supported by explicit comments.** Do the relevant transformation first. Inspect the data frame that will be plotted. Then construct the figure.

For counts or summaries shown as bars, prefer `count()` or `summarise()` followed by `geom_col()`. This makes the bar heights and labels refer to the same visible numbers. Use `geom_histogram()` for a distribution with an explicit binning decision. Do not replace appropriate statistical geoms indiscriminately.

```r
plot_data <- analysis_data |>
  count(treatment, name = "n_respondents")

plot_data

sample_plot <- ggplot(
  plot_data,
  aes(x = treatment, y = n_respondents)
) +
  geom_col(fill = "gray60") +
  geom_text(aes(label = n_respondents), vjust = -0.4) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.10))) +
  labs(x = NULL, y = "Number of respondents") +
  theme_few(base_size = 12)
```

Put common mappings in `ggplot()` when several layers share them. Use layer-specific `data =` and `aes()` when the data or mapping differs. Name `mapping =` if the argument position could be mistaken. Put fixed settings such as `color = "gray60"` outside `aes()`; put variable-based aesthetics inside it.

Layer order matters. Draw background bands and reference elements before focal data when appropriate, then labels. Use `annotate()` or a dedicated annotation tibble for a single note or rectangle; do not unintentionally draw it once for every data row. The Technical Notes document this exact source of confusing opacity and overprinted text.

## 15. The Default Visual Style

**Confirmed.** Begin static ggplot figures with `theme_few()`. Add plot-specific `theme()` adjustments **after** the complete theme. Its documented default base size is 12 points; see [ggthemes](https://jrnold.github.io/ggthemes/reference/theme_few.html). The appropriate delivered size depends on the final physical figure size.

Prefer a small, purposeful palette. Gray works well for context and a single accent for the focal comparison. Use accessible colors and non-color identification where needed. Do not add a gradient, an extra legend, or decorative color merely because a plotting function supports it.

Prefer direct labels, meaningful axis labels, or facet headings to legends. Remove a legend only when the reader can still identify what each visual element means. A continuous map scale may need a legend; that is a useful exception, not a failure.

Use small multiples when they make comparisons easier. Share scales when magnitude comparison is central. `scales = "free_y"` is a deliberate choice for within-panel patterns; it weakens direct cross-panel magnitude comparisons and should be explained.

For publication figures, put the title, estimand, uncertainty definition, sample, source, and methodological notes in the manuscript caption. Do not embed a large title or subtitle in the graphic. Standalone teaching, slides, dashboards, and animations may need a title or a visible date: the course's title-bearing figures are context-specific.

Choose physical width and height for the intended placement. Keep text approximately the manuscript text size or only slightly smaller after scaling. Avoid excess blank space without clipping labels or intervals. A large RStudio preview is not evidence that a figure will be readable in a paper.

## 16. Axes, Coordinates, and Chart Choices

**Course-derived / previously confirmed.** Use `coord_cartesian()` for zooming when data should remain in statistical calculations. Scale limits can discard observations and change a smooth, histogram, or boxplot. Define limits, breaks, and labels in one scale call for an aesthetic; adding another scale replaces the earlier one.

The fact that a plot is technically valid does not make it substantively helpful. The Day 5 paired examples support these choices:

| Problem | Preferred response |
|---|---|
| Truncated bar baseline | Start bars at zero |
| Many crossing lines and a crowded legend | Label endpoints, highlight a focal series, or facet |
| Pie slices that require precise comparison | Use sorted bars or points |
| Unrelated dual y-axes | Separate clearly labeled panels |
| Overplotted scatter labels | Reduce overplotting and label selected observations |
| Raw-count map confounded by population | Use a meaningful rate when the question is comparative risk |
| Stacked areas without a common baseline | Use small multiples when comparing component trends |
| Difficult Likert comparisons | Consider a diverging arrangement with explicit neutral handling |
| Grouped bars for change | Consider connected points or a slope display |
| Decorative 3D bars | Use a clear two-dimensional chart |

A count map may still answer a total-burden question. A diverging Likert figure is one option, not a universal requirement. The decision should follow the comparison the reader needs to make.

For estimates, show points and uncertainty intervals with a clear null/reference line. For ranks, choose the direction deliberately. For polygons, use the correct group identifier and coordinate system. For geographic data, do not treat longitude and latitude as arbitrary Cartesian coordinates.

## 17. Tables and Saved Outputs

**Previously confirmed / course-derived.** Keep table construction reproducible. The modeling precept uses `modelsummary()` with meaningful coefficient labels, selected fit statistics, and notes identifying robust standard errors. Preserve this explicit control rather than relying on an opaque default table.

For new publication tables where manuscript conventions support it, use `threeparttable`, `tabularx` spanning `\textwidth`, `booktabs`, no vertical rules, caption/label above, and flush-left notes below. Prefer `[!t]`, a 1.25 baseline stretch, `@{\extracolsep{\fill}}`, and modest section spacing where appropriate. Use estimates on one row with robust standard errors beneath when that is the specified uncertainty method. Include concise useful fit statistics, and use `\num{}` when `siunitx` is loaded.

Keep coding definitions, reference groups, sample, uncertainty method, and significance notation in the notes. Do not invent significance stars or a robust specification just to mimic a classroom table. Do not hand-edit numerical results in exported LaTeX. If a table is too wide, revise structure or labels before shrinking it to unreadable size.

Save a named plot explicitly:

```r
ggsave(
  filename = "figures/treatment_effect.pdf",
  plot = effect_plot,
  width = 6.5,
  height = 3,
  units = "in"
)
```

These dimensions are examples, not a fixed rule. Prefer vector PDF for LaTeX manuscripts; save a matching PNG when needed for previews or web use. Keep counterpart physical dimensions consistent. Specifying `plot =` prevents an intervening diagnostic plot from being exported accidentally; see [ggsave()](https://ggplot2.tidyverse.org/reference/ggsave.html).

## 18. Reproducibility Without Unnecessary Machinery

**Course-derived / recommendation.** A completed script should run from a clean R session, top to bottom, with documented inputs. Test the script as delivered. Restart R or run `Rscript --vanilla`; do not mistake `rm(list = ls())` for a complete session reset.

Use `set.seed()` before simulation, sampling, or other relevant random operations; use a supported local seed for label placement or jitter when available. Record meaningful R and package versions. Preserve the project's existing dependency-management method instead of adding a new framework automatically.

Do not globally suppress warnings. Inspect import, model, and plotting warnings. Narrow suppression is justified only for a known, explained condition after confirming the result. The course contains suppressed parsing warnings and deliberately failing demonstrations; those are not general research defaults.

For scraped or downloaded data, keep a reproducible snapshot when permitted, with source and retrieval date. Do not rely on a live HTML table remaining at index 3 forever. Validate its column names and content. Separate data acquisition from analysis when network changes would otherwise make reruns unstable.

Use targeted checks for important assumptions: unique respondent IDs, join cardinality, allowed categories, missing values, expected model terms, and agreement between plotted estimates and saved results. Avoid a large testing framework for a small one-off analysis unless the project needs it.

Open saved figures and tables. Check labels, legend necessity, clipping, scale direction, uncertainty, number formatting, and final-size legibility. Confirm that the caption describes the actual exported plot.

## 19. What Belongs Only to Teaching

Do not copy the following into every research script merely because they appear in this archive:

- Course/day/precept titles and `Name: xxx` / `Date: xxx` placeholders.
- One script per 100-minute precept and the literal “End of Precept” heading.
- Restrictions to functions already taught, or a universal prohibition on `dir.create()`.
- Multiple alternative solutions, deliberate errors, incomplete exercises, or “bad” figures.
- Repeated scraping inside a teaching function, fixed HTML table indices, or example-specific recoding assumptions.
- The 11-by-8-inch classroom figure dimensions, all-uppercase input fields, or mixed legacy filenames.
- Every use of `theme_minimal()`, `theme_void()`, `theme_light()`, `$`, or brackets.
- Advanced optional grouped-model, tidy-evaluation, interactive-map, or animation workflows as the default for a simple task.

Retain their underlying lessons: structure, explicit choices, inspectability, meaningful comparisons, and clean-session verification.

## 20. The AI's Handoff Checklist

Before delivering work, the AI should be able to answer all of these:

1. **Purpose:** Does each script explain what it does, its inputs, and its outputs?
2. **Reading order:** Can I follow the data from import to the final result without hidden transformations?
3. **Familiar vocabulary:** Is ordinary data work consistently tidyverse, with extraction exceptions explained?
4. **Sample and coding:** Are exclusions, missing values, denominators, units, reference categories, and consequential recodes visible?
5. **Joins and grouping:** Are keys, expected relationships, row counts, and the end of grouping checked?
6. **Models:** Are the formula, sample, estimator, uncertainty method, and plotted terms explicit?
7. **Figures and tables:** Do they follow the intended publication/teaching context, with readable labels and correct saved content?
8. **Formatting:** Was `styler` actually run on the relevant files and the result reviewed?
9. **Execution:** Did the delivered script actually run in a clean session? What warnings or limitations remain?
10. **Explanation:** Does the handoff name the files, explain important changes, and point to the intermediate objects I should inspect?

The handoff should be concise: what changed, where to start reading, what was verified, and any meaningful exception. Do not claim that matching this guide proves I have understood the work. The practical test is whether I can locate and explain each consequential operation with little effort.

## 21. Sources and Supporting Files

The primary evidence is the user-supplied `waseda_2026.zip` snapshot, not a live course folder that may have changed. Specific source paths and line references appear in [the evidence report](analysis/EVIDENCE.md). The existing personal R/figure reference supplies the previously confirmed publication conventions.

- [Runnable end-to-end example](examples/01_readable_analysis.R): synthetic survey data, cleaning, sample accounting, HC2 model, tidy results, and saved figures.
- [Runnable wrangling and function recipes](examples/02_wrangling_and_functions.R): reshaping, checked joins, strings, dates, factors, dot-prefixed arguments, and `map()`.
- [New-script template](templates/analysis_script.R): a deliberately incomplete starter, not a validated analysis.
- [AI application prompt](APPLY_GUIDE.md): the instruction to accompany this complete guide.
- [Source evidence](analysis/EVIDENCE.md) and [verification record](analysis/VERIFICATION.md).

Official references checked October 24, 2026: [Google R guide](https://google.github.io/styleguide/Rguide.html), [tidyverse style](https://style.tidyverse.org/), [styler](https://styler.r-lib.org/), [RStudio code sections](https://docs.posit.co/ide/user/ide/guide/code/code-sections.html), and the package references linked in the relevant sections. The five existing guides were used as local design references; their specific operational instructions were not treated as instructions for this task.
