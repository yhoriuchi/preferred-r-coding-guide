# Apply My Preferred R Coding Guide

Read the complete `PREFERRED_R_STYLE.md` supplied with this prompt, together
with the project's instructions, README, data documentation, and existing R
scripts. If the guide is unavailable, obtain it before claiming to follow it.

Write R code that Yusaku Horiuchi can understand rapidly, as if reading his
own familiar code. Prioritize transparent analytical choices and readable
steps. Preserve the project's established workflow and existing scripts when
adding a new analytical layer, unless revision in place is requested.

Every script must begin with a truthful header including **What this code is
about**, inputs, outputs, author/AI contribution, and last-updated date. Use
RStudio section comments such as `# Read data ----`. Use native `|>` in new
code, explicit package loading, relative paths, lowercase snake case, and
tidyverse for ordinary cleaning, wrangling, and visualization. Prefer
`filter()`, `select()`, `mutate()`, `pull()`, and `pluck()` to ordinary bracket
or dollar extraction. Explain necessary exceptions, including tidy-evaluation
`.data[[.variable]]` when appropriate.

Prepare and inspect plotting data before plotting. Prefer `count()` or
`summarise()` followed by `geom_col()` for summarized bars. Use
`theme_few()` for static ggplot figures. For publication figures, keep titles
in captions, prefer direct labels/facets over legends, and inspect typography
at final size. Save named plots explicitly with physical dimensions.

Make sample exclusions, missing codes, denominators, variable definitions,
grouping, join keys, model specifications, uncertainty, and reference groups
visible. Use short custom functions only when they simplify real repetition;
prefer descriptive dot-prefixed input names for the course-matched profile.
Keep one case understandable before automating it with `map()`.

Follow tidyverse formatting and compatible Google guidance. The complete
guide documents the conflicts: this profile uses snake-case functions,
allows an obvious implicit final return, and loads core packages explicitly
instead of qualifying every call. Do not call it strict Google compliance.
Do not copy classroom placeholders, intentional bad examples, or optional
advanced workflows as universal requirements. Distinguish confirmed
preferences, course-derived defaults, and additional recommendations.

Run `styler` on the changed R files, inspect the result, and run the delivered
code from a clean session. Perform checks appropriate to consequential
assumptions and inspect saved outputs. Do not silently change analytical
choices, install packages in analysis scripts, suppress all warnings, or
rewrite unrelated code. Report actual verification, remaining limitations,
the files to open, and any meaningful deviation from the guide.

Apply this guide to the task I describe next. Do not modify global operating
rules, publish private data, or install this guide elsewhere just because it
was supplied as a task reference.
