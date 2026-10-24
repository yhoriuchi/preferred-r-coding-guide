# Evidence Behind the Preferred R Coding Guide

Audit date: October 24, 2026. This report is a source interpretation, not a revision of the Waseda course.

## Scope and Method

The supplied archive is the source snapshot. It contains 5,024 ZIP entries, including directories and macOS metadata. After excluding `__MACOSX`, there are **35 actual `.R` files with 7,020 lines**. All 35 were read; the two revised scripts were compared with their originals, and the screenshot copy was identified separately. All 35 pass R's parser.

The 35 comprise 22 ordinary teaching scripts, two revised scripts, ten files containing bad/better visualization comparisons, and one screenshot copy. These counts describe files, not 35 independent endorsements of a coding convention. Repeated versions and alternative solutions are not independent evidence.

Additional reading covered the complete course style document, the relevant workflow instructions, and all seven substantive Technical Notes. The other `.Rnw` files are inventoried, but this audit does not claim to have fully reviewed every exam, answer key, slide, PDF, or data file. R code embedded in those documents was not subjected to an exhaustive separate audit. The source inventory contains 66 `.Rnw` files, including the technical-note summary, plus the 35 scripts and the style document.

The scripts were parsed without executing them. Live scraping, downloads, incomplete exercises, and original empirical analyses were not rerun. The new runnable demonstrations were separately executed, as recorded in the verification report.

Locally retained files: `source_inventory.csv` records archive-relative paths, bytes, line counts, roles, and SHA-256 digests; `source_summary.json` records the archive digest; `r_syntax_inventory.csv` records per-script parsing and selected token counts. These private audit companions are excluded from the public repository and downloadable package. No original course materials are distributed.

## Why Frequency Alone Is Insufficient

Parsing identifies 551 native-pipe tokens, no magrittr pipe tokens, 15 dollar operators, 23 single-bracket operators, and 53 double-bracket operators across the 35 scripts. These counts exclude commented-out code and string contents. They include duplicates, demonstrations, and intentionally bad examples.

The native pipe is both a consistent source pattern and an explicit course convention. The bracket counts, however, do not establish a preference for bracket extraction: those operations are concentrated in programming and list lessons. The latest user request explicitly favors avoiding brackets and `$` where practical.

Likewise, `theme_minimal()` appears in the paired visualization demonstrations, including their improved plots. The demonstrations teach chart design; their existence does not override the user's explicit `theme_few()` preference. Plot titles in classroom examples do not override the confirmed rule for manuscript figures.

## Source Key

Paths below are relative to `waseda_2026/` inside the ZIP. Line numbers refer to the original snapshot, not a reformatted copy.

| Key | Source path |
|---|---|
| STYLE | `style_guide/style_guide.tex` |
| WORKFLOW | `day01/precept01_setup/documents/precept01_workflow.Rnw` |
| P01 | `day01/precept01_setup/scripts/precept01_script.R` |
| P02 | `day01/precept02_r_language/scripts/precept02_script.R` |
| P03 | `day01/precept03_explore_1/scripts/precept03_script.R` |
| P04 | `day01/precept04_explore_2/scripts/precept04_script.R` |
| P04-OPT | `day01/precept04_explore_2/scripts/precept04_optional_challenges_script.R` |
| P05 | `day02/precept05_data_exploration_part3/scripts/precept05_script.R` |
| P06 | `day02/precept06_data_exploration_part4/scripts/precept06_script.R` |
| P07 | `day02/precept07_data_exploration_part5/scripts/precept07_script.R` |
| P08 | `day03/precept08_data_wrangling_part1/scripts/precept08_script.R` |
| P09 | `day03/precept09_data_wrangling_part2/scripts/precept09_script.R` |
| P10 | `day03/precept10_data_wrangling_part3/scripts/precept10_script.R` |
| P11-1 / P11-2 | `day04/precept11_programming_part1/scripts/precept11_script_part1.R` / `precept11_script_part2.R`, with both `_revised.R` versions |
| P12-1 / P12-2 / PREP | `day04/precept12_programming_part2/scripts/precept12_script_part1.R`, `precept12_script_part2.R`, `precept12_preparation.R` |
| P13-1 / P13-2 | `day04/precept13_statistical_modeling_visualization/scripts/precept13_script_part1.R` / `precept13_script_part2.R` |
| WORKSHOP | `day05/handout01_good_bad_data_visualization/scripts/workshop_script.R` |
| BAD01–BAD10 | The ten `bad_visualization_*.R` files in that handout's `scripts/bad_visualizations/` folder |
| INTERACTIVE | The three `interactive_data_visualization_script_*.R` files in `day05/handout02_interactive_data_visualization/scripts/` |
| TN01–TN07 | `technical_notes/technical_notes_01.Rnw` through `technical_notes_07.Rnw` |

## Preference-to-Evidence Map

| Guide choice | Primary evidence | Interpretation |
|---|---|---|
| Script purpose near the top | Current request; WORKFLOW around line 190 | Confirmed, with course support |
| Single-`#` header, no decorative wrapper | STYLE, Script Style; all script openings | Course-derived |
| RStudio sections | Current request; WORKFLOW shortcut table; STYLE | Confirmed |
| `styler` | Current request; WORKFLOW line 184; STYLE line 303 | Confirmed |
| Native pipe | STYLE line 304; WORKFLOW pipe section; parsed scripts | Course-derived, also existing reference |
| Explicit `library()` near the top | STYLE, Package Names; script settings sections | Course-derived |
| Manual installation outside analysis scripts | WORKFLOW line 93 and preceding explanation | Explicit preference in course source; not a new global installation rule |
| Relative paths from `.Rproj` root | WORKFLOW project section; STYLE; P13 `file.path()` | Course-derived, also existing reference |
| Lowercase snake case | STYLE file naming; existing R/figure reference | Working default; source has legacy exceptions |
| Readable multistep pipelines | P05–P10, P12, STYLE | Repeated pattern |
| `read_csv()` over `read.csv()` | P05 lines 25–29 | Explicit source preference; do not generalize type guessing as guaranteed |
| Visible intermediate objects | P04 figure-specific frames; P07 `df2a`/`df2b`; P13 tidy results | Repeated pattern |
| `pull()` versus one-column `select()` | P06 scalar extraction; P11-1 vector/data-frame comparison | Explicit conceptual distinction |
| Avoid ordinary `$` and brackets | Current request | Latest instruction takes precedence over teaching demonstrations |
| `pluck()` as list extraction | Practical tidyverse alternative | Recommendation; not claimed as a repeated course idiom |
| Clean and compare source labels | P09 lines 33–61 | Source demonstrates explicit corrections and unmatched-name inspection |
| Keep original values for consequential recodes | P09 inspection approach | Recommendation extending source inspectability |
| Regex and stringr distinctions | P09; TN06 | Course-derived |
| Reshape administrative tables | P08 `fill()`, pivots, totals, fiscal dates | Source workflow; individual constants are task-specific |
| Explain dropped missing cells | P08 line 80 | Recommendation prompted by `values_drop_na = TRUE` |
| End persistent grouping | P05 lines 99–104; TN02 | Strong explicit source recommendation |
| Top-N and tie decisions | P06 rank alternatives; TN02 | Source distinction plus corrected interpretation of global/per-year ranking |
| Check joins with `anti_join()` | P09 lines 41, 44, 60 | Repeated explicit checks |
| Preserve map polygons with `left_join()` | P11-2 map join and explanatory comment | Explicit source rationale |
| Check relationship and row count | P09/P11 join reasoning; dplyr reference | Recommendation beyond literal source syntax |
| Factor labels/order | P10; P06 ranking; P13 treatment outcomes | Repeated source pattern |
| Dot-prefixed function inputs | P11-2 lines 117–120; P12-2; TN07 | Explicit self-described preference in source, not completely consistent |
| Start with one case before automating | P11 function progression; P12 loop/function/map sequence | Course-derived |
| `map()` then `list_rbind()` | P12-1 lines 117–120; current purrr reference | Existing source alternative and current recommendation |
| Allow clear implicit return | P11-1 and P12-1 explanations | Course-derived; conflicts with strict Google |
| Explain embracing and string indirection | TN07; P13-1 optional functions | Context-specific tools, legitimate bracket exception |
| Model → tidy results → plot | P13-1 | Repeated analytical workflow |
| `lm_robust()` where appropriate | P13-1 and P13-2 | Demonstrated estimator, not a universal model choice |
| Explicit coefficient labels and notes | P13-2 line 67 onward | Source table workflow |
| Aggregate before `geom_col()` | P03 line 143; P05 bars; P07 lines 76, 119 | Strong explicit source preference |
| Put shared aesthetics in `ggplot()` | P03 inheritance discussion; P07; TN03 | Course-derived |
| Separate mapping from setting | P03/P04; TN03 | Explicit teaching principle |
| Layer order matters | P04 points over smooth; P05 areas/bars/lines | Strong source emphasis |
| One annotation, not one per row | TN01 | Explicit technical note |
| `theme_few()` | Current request; existing confirmed reference; main course figures | Confirmed |
| Theme adjustments follow complete theme | P06; P07; P11-2 | Repeated source explanation |
| Direct labels and small multiples | P04-OPT; WORKSHOP; BAD02/BAD07 | Source design direction; confirmed legend preference in existing reference |
| Zoom without dropping observations | TN04; P13-1 | Explicit explanation |
| One scale per aesthetic | TN05 | Corrected synthesis: combine settings instead of reversing competing scales |
| Zero baselines and useful chart choices | All ten BAD/better pairs | Learn from the better alternative, not the deliberate failure |
| Named `plot =` in exports | P13-1; BAD examples | Source pattern plus safety rationale |
| Seed relevant randomness | P04 jitter; BAD examples; plotly example | Repeated source pattern |
| Clean-session and saved-output checks | WORKFLOW final paragraph; most script endings | Explicit course instruction |
| Preserve scripts; manuscript captions, typography, tables | Existing personal R/figure reference | Previously confirmed preferences; not newly inferred from this ZIP |

## Coverage Notes by Script Group

- **P01 and its screenshot copy:** relative paths, map layers, single-`#` header; `theme_minimal()` is a setup demonstration. The copy omits the final reproducibility reminder and is not independent evidence.
- **P02:** base language and type demonstrations; brackets, `data.frame()`, coercion, and elementary comments are teaching content.
- **P03:** mapping/inheritance, optional comparisons, an explicit statement favoring pre-wrangling plus `geom_col()`; several examples are intentionally undesirable or incomplete alternatives.
- **P04 and P04-OPT:** time-series frames, gray context, direct line labels, annotations, jitter seed, `theme_few()`. The optional file overlaps the main script; do not double-count it as a second preference endorsement.
- **P05:** readr preference, group persistence, within-country comparisons, precomputed bar data, layer order, explicit date windows.
- **P06:** comparison of limits, `pull()` for scalars, three ranking conventions, patchwork versus facets, explicit factor/display ordering.
- **P07:** row-unit and duplicate inspection, missing-value explanation, counts before bars, selective labels, residual inspection, visible statistical modeling.
- **P08:** messy tables, filled headings, explicit month mapping, subtotal removal, fiscal dates, saved RDS stages, visible shares and annotations.
- **P09:** regex, state-name correction, unmatched joins, string normalization, dates, geographic transformation, informative inspection.
- **P10:** forcats operations, source coding, property-damage units, logged values, thresholds, facets, geographic keys. Literal source thresholds and legacy object capitalization remain contextual.
- **P11-1 and revised:** increasingly capable functions, vector/list distinctions, input validation, live HTML extraction. The revised file adds clarification; it does not introduce a new analysis workflow.
- **P11-2 and revised:** dot-prefixed inputs, correct map join, explicit maps, special multi-country handling, branching. The only revised-file change is introductory wording. Dividing multi-country deaths equally is an exercise-specific assumption, not a cleaning rule.
- **P12-PREP:** acquisition is separate from the main script; archive URLs and timeout settings are task-specific.
- **P12-1:** loop, function, `map()`, `map_dfr()`, `list_rbind()`, and `all.equal()` comparison. Narrow suppressed read warnings are not generalized.
- **P12-2:** optional list construction, flexible functions, separate optional filters, source-file labels, factors, nonlinear smooth. Positional latest-file selection is not a reliable general “most recent” rule.
- **P13-1:** model/tidy/plot progression, subgroup examples, explicit plot exports, optional automation and unfinished exercise. Preserve simple explicit models as a readable option.
- **P13-2:** construct a derived outcome, inspect its coding, build formulas, label table coefficients, identify uncertainty in notes.
- **WORKSHOP:** rankings, highlighted small multiples, reverse axis, gray comparison data, no-legend identification; optional expanded background data is intentional duplication for plotting.
- **BAD01:** truncated versus zero-baseline bars.
- **BAD02:** crowded line legend versus endpoint labels.
- **BAD03:** pie slices versus sorted bars.
- **BAD04:** unrelated dual axes versus separate panels.
- **BAD05:** too many labels versus selected, repelled labels.
- **BAD06:** counts versus population-adjusted rates; only the comparison question determines the correct quantity.
- **BAD07:** stacked area versus shared-baseline small multiples.
- **BAD08:** stacked Likert versus a diverging view; neutral responses need deliberate treatment.
- **BAD09:** grouped bars versus slope comparisons.
- **BAD10:** decorative 3D polygons versus sorted horizontal bars.
- **Three INTERACTIVE scripts:** animation, ggplotly, and leaflet demonstrations; no basis for requiring interactive outputs or their themes in every analysis.

## Source Problems Not Promoted into Rules

1. **TN02 ranking wording:** the text describes finding the top five within each year, but fully ungrouping and then `slice_max()` yields a global selection. The guide explicitly separates those targets.
2. **TN05 scale replacement:** reversing the order of two scale definitions merely changes which one is replaced. The guide recommends combining scale settings and separating coordinate zooming.
3. **TN07 “Name injection”:** `mutate(new_var := {{ .variable }})` uses a fixed output name; it is not an example of dynamically injecting a name. The guide does not reproduce that interpretation.
4. **P11 live table indices and source-specific parsing:** HTML positions and country allocations can change or encode assumptions. The guide requires content validation and an explicit rationale.
5. **P12 warning suppression / alphabetical file order:** neither establishes a general default for hiding read failures or selecting a latest release.
6. **P13 alternative-function exercise:** the final placeholder function has intentionally unfinished branches. It is an exercise, not a reusable production implementation.
7. **Legacy styles:** `ifelse()`, `data.frame()`, mixed-case names, different themes, and direct extraction remain valid source observations but are not automatically preferred for newly generated code.

These findings were used to improve the synthesis. The original teaching materials were not edited.

## Matching the Other Five Guides

Local source and CSS were inspected for Guide to Recording AI Use, Replication Package Guide, BibTeX Cleaning Agent Guide, QSF Audit Agent Guide, and LaTeX Research Article Guide. All share the same overall visual family, but they are not pixel-identical.

The new guide copies the LaTeX guide's base stylesheet, which matches the common QSF/BibTeX typography and spacing: system sans-serif body font; `#f7f8fb` background; `#18202a` text; teal links; dark code blocks; a 948px maximum shell; 32px total horizontal allowance; 40px top / 64px bottom shell padding; a responsive 2.3rem–4.8rem title; 1.55rem section headings; and 1.6 body line height. Mobile follows the same 760px breakpoint and 22px total horizontal allowance.

The AI-use guide uses line height 1.52 and some smaller section gaps; the replication guide uses a slightly different shell allowance and bottom padding. The chosen base follows the majority family rather than pretending all five have identical values. Additional rules support a table of contents, focus outlines, and local download/copy controls without changing the shared base typography.

The existing guides are English web guides, so the deliverable uses English and static HTML, with Markdown as the maintainable text source. Following the author's publication request, this guide is distributed through the `yhoriuchi/preferred-r-coding-guide` repository and GitHub Pages. At the author's request, the homepage includes the same Hits.sh page-view badge used by the LaTeX guide, with a separate counter for this guide. It appears below the author and date metadata; the companion evidence and verification pages do not increment that homepage counter.

## Limits on Interpretation

This is a substantial, source-based first version. It cannot establish undocumented preferences with certainty or guarantee effortless understanding of every future analysis. Course-derived choices and recommendations remain labeled. The global manual and existing R/figure reference were not rewritten. Future explicit corrections from Yusaku should update this guide through the applicable rule-management workflow when they become durable operating rules.
