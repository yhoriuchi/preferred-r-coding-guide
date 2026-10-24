# My Preferred R Coding Guide: wrangling and readable functions
# What this code is about: Tidy a small administrative table, check a lookup
# join, and demonstrate familiar functions with explicit input arguments.
# Unit of observation: One country-month after pivot_longer().
# Inputs: Synthetic data defined below; no network or private data.
# Outputs: examples/output/monthly_data.csv and a printed grouped summary.
# Author: Codex, for Yusaku Horiuchi
# Last updated: 2026-10-24

# Initial settings --------------------------------------------------------

library(tidyverse)

# Read and inspect the example table --------------------------------------

raw_table <- tribble(
  ~country, ~jan_2026, ~feb_2026,
  " Japan ", "1,000", "1,100",
  "Australia", "900", "950"
)

country_lookup <- tribble(
  ~country, ~iso3,
  "Japan", "JPN",
  "Australia", "AUS"
)

raw_table

# Reshape and clean -------------------------------------------------------

monthly_data <- raw_table |>
  mutate(country = str_trim(country)) |>
  pivot_longer(
    cols = c(jan_2026, feb_2026),
    names_to = "month_source",
    values_to = "count_source"
  ) |>
  mutate(
    # An explicit map avoids dependence on the computer's date locale.
    month = case_when(
      month_source == "jan_2026" ~ 1L,
      month_source == "feb_2026" ~ 2L,
      TRUE ~ NA_integer_
    ),
    date = make_date(year = 2026, month = month, day = 1),
    # These demonstration strings contain comma-separated exact counts.
    n_cases = parse_number(count_source, locale = locale(grouping_mark = ","))
  ) |>
  select(country, date, n_cases, count_source)

monthly_data

duplicate_country_months <- monthly_data |>
  count(country, date) |>
  filter(n > 1)

stopifnot(
  nrow(duplicate_country_months) == 0,
  !anyNA(monthly_data |> select(country, date, n_cases))
)

# Check and join the lookup -----------------------------------------------

unmatched <- monthly_data |>
  anti_join(country_lookup, by = "country")

duplicate_lookup_keys <- country_lookup |>
  count(country) |>
  filter(n > 1)

stopifnot(nrow(unmatched) == 0, nrow(duplicate_lookup_keys) == 0)

monthly_data <- monthly_data |>
  left_join(
    country_lookup,
    by = "country",
    relationship = "many-to-one",
    na_matches = "never"
  ) |>
  mutate(country = fct_relevel(country, "Japan", "Australia")) |>
  arrange(country, date)

stopifnot(nrow(monthly_data) == 4)

# Make one function and inspect one case ----------------------------------

# Input: a tibble and one country name. Output: one summary row.
summarize_country <- function(.country, .dataframe) {
  country_data <- .dataframe |>
    filter(country == .country)

  if (nrow(country_data) == 0) {
    stop("The requested country has no observations.")
  }

  country_data |>
    summarise(
      country = .country,
      n_months = n(),
      total_cases = sum(n_cases)
    )
}

summarize_country("Japan", monthly_data)

# Repeat the same understandable calculation -------------------------------

countries <- c("Japan", "Australia")

# map() supplies each country to .country; .dataframe stays the same.
country_summaries <- map(countries, summarize_country, .dataframe = monthly_data) |>
  list_rbind()

country_summaries

# Tidy evaluation: a justified bracket exception ---------------------------

# .variable is a character column name. .data is dplyr's data pronoun,
# not the function's .dataframe argument. This use of [[ ]] is intentional.
sum_named_column <- function(.dataframe, .variable) {
  .dataframe |>
    summarise(total = sum(.data[[.variable]])) |>
    pull(total)
}

total_cases <- sum_named_column(monthly_data, "n_cases")
stopifnot(total_cases == 3950)

# Save and verify ---------------------------------------------------------

write_csv(monthly_data, "examples/output/monthly_data.csv")
stopifnot(sum(country_summaries |> pull(total_cases)) == total_cases)

# Restart R and run this script from the guide's root directory.
