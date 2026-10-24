# Verification Record

Checked October 24, 2026. This record distinguishes source inspection from execution of the new examples.

## Source Review

- All 35 actual `.R` files in the supplied ZIP were read and passed `parse()` under R 4.6.1.
- Two revised scripts were compared with their originals; the screenshot copy and overlapping optional examples were identified separately.
- The course style document, relevant workflow instructions, and all seven substantive Technical Notes were read.
- The inventory includes the 66 `.Rnw` files, but not every embedded code chunk or surrounding course document was individually audited. Original course analyses and live downloads were not rerun.
- The archive SHA-256 and per-file digests are recorded locally. Original source files were not changed.

## New R Files

`styler` 1.11.0 was run on both examples, the starter template, and the source-inspection script. Changes were reviewed. The two runnable examples then completed with `Rscript --vanilla` from the guide root, without analysis/model/plot warnings. Tidyverse startup messages identify normal function-name conflicts; the examples do not use ambiguous external versions of those functions.

The starter template parses but deliberately stops until filled in. It is not presented as a completed analysis. Markdown code excerpts are explanatory snippets; their syntax is checked separately, but they do not all run independently without the surrounding named objects.

| Check | Result |
|---|---|
| Synthetic input records | 12 unique respondent IDs |
| Sample accounting | 10 included, 1 missing outcome, 1 missing treatment |
| Analysis sample | 5 control and 5 treatment respondents |
| Means | Control 3.6; treatment 5.6 |
| Estimated contrast | 2.0 scale points; agrees with the difference in means |
| Uncertainty | HC2 standard error 0.7211103; 95% interval approximately 0.3371 to 3.6629 |
| Saved data | RDS reloaded and identical to the analysis object |
| Wrangling example | 4 country-month rows, no duplicate keys, no unmatched lookup rows |
| Wrangling totals | Japan 2,100; Australia 1,850; total 3,950 |
| Programmatic extraction | Ordinary `$`/bracket extraction avoided; one documented `.data[[.variable]]` exception |

Relevant versions: R 4.6.1 (2026-06-24); tidyverse 2.0.0; dplyr 1.2.1; purrr 1.2.2; readr 2.2.0; ggplot2 4.0.3; ggthemes 5.2.0; estimatr 1.0.6; broom 1.0.13; styler 1.11.0. The complete session information is saved with the example outputs.

`modelsummary` was not installed in the checked environment. The guide documents its source-backed use, but no newly generated `modelsummary` table is claimed to have been executed or validated.

## Visual and Browser Checks

- The saved treatment-effect PDF was rendered with Poppler and visually inspected. Its final dimensions are 6.5 × 1.6 inches; the matching PNG uses the same dimensions. Text, interval, zero line, and category label are readable and unclipped.
- The sample-count PNG was visually inspected, including its zero baseline, direct count labels, and axis labels.
- The guide was rendered in the in-app browser at its available narrow viewport. The title, metadata, buttons, contents, table, and code presentation were checked; section navigation and the complete-guide copy button were exercised successfully.
- The base CSS is an exact copy of the existing LaTeX guide's stylesheet. The five guides' CSS values were compared; their small existing differences are documented in the evidence report. Desktop rules are inherited and checked in source; no separate wide-viewport screenshot is claimed.
- Static checks verify local link targets, unique heading IDs, table column consistency, and equality of the copied text to the maintained prompt plus guide. The local package is checked for archive integrity and excludes project history.

## Repairs and Practical Limits

The first `styler` attempt encountered a cache-directory write restriction. Disabling styler's cache for the formatting process resolved it; no global setting or package installation was changed. An initial deprecated `across()` form in the audit utility was replaced by an explicit function. A Python 3.9 string-formatting issue in the HTML builder was fixed. Markdown pipes inside tables were escaped after browser inspection exposed incorrect cell splitting.

The first Poppler render reported a missing font configuration and unwritable cache. A temporary fontconfig file using system fonts and a temporary cache resolved this. A temporary loopback-only preview server required normal sandbox escalation and was allowed; no public server or deployment was created.

Final cleanup identified an unintended `Rplots.pdf` from automatic printing during batch execution. Plot previews are now explicitly interactive; batch execution writes only the named figure files. The temporary file was removed, and the analysis was rerun to verify that it did not recur.

The copy fallback is implemented for browsers without clipboard access. The successful clipboard path was exercised in the current browser; the denied-permission path was inspected in source, not forced through a browser permission change. Complete understanding by the human collaborator cannot be mechanically guaranteed; the guide gives a repeatable standard for making that outcome more likely.
