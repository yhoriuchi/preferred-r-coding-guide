# My Preferred R Coding Guide

A source-based guide for producing R code that Yusaku Horiuchi can read and
understand rapidly, even when AI performs the full analysis.

Read the [published guide](https://yhoriuchi.github.io/preferred-r-coding-guide/),
or open [index.html](index.html) locally in a browser. Its visual design follows the
existing five-guide family. The complete maintainable text is
[PREFERRED_R_STYLE.md](PREFERRED_R_STYLE.md). The page's copy button includes
both the application prompt and the full guide.

## Files

- `PREFERRED_R_STYLE.md`: complete guide, with authority/evidence labels.
- `APPLY_GUIDE.md`: short application prompt to accompany the complete guide.
- `templates/analysis_script.R`: intentionally incomplete script starter.
- `examples/01_readable_analysis.R`: executable synthetic analysis and figures.
- `examples/02_wrangling_and_functions.R`: executable wrangling and function recipes.
- `analysis/EVIDENCE.md`: source coverage, provenance, exceptions, and design comparison.
- `analysis/VERIFICATION.md`: checks, actual execution results, and limitations.
- `scripts/build_guide.py`: static HTML builder using Python 3 and R's `commonmark`.
- `scripts/package_guide.py`: rebuild the portable guide ZIP from an explicit file list.
- `scripts/check_guide.py`: check links, tables, copied text, and R snippet syntax.
- `assets/site.css`: base stylesheet copied from the existing LaTeX guide.
- `assets/guide.css` / `guide.js`: guide-specific navigation and copy support.

## Run the examples

From this folder, with the documented R dependencies already installed:

```sh
Rscript --vanilla examples/01_readable_analysis.R
Rscript --vanilla examples/02_wrangling_and_functions.R
```

The example output directories are included. The examples use synthetic data
and do not download anything. The script template deliberately stops until
completed; it is not a runnable empirical analysis.

## Rebuild the HTML

```sh
python3 scripts/build_guide.py
python3 scripts/package_guide.py
python3 scripts/check_guide.py
```

Edit the Markdown source, then rebuild, so the readable and copied versions
stay synchronized. The generated HTML is standalone except for local CSS and
JavaScript files. No server is needed to read it. Clipboard permissions vary
by browser; a manual-copy fallback is provided.

## GitHub Pages

Repository: [yhoriuchi/preferred-r-coding-guide](https://github.com/yhoriuchi/preferred-r-coding-guide).
GitHub Pages serves the committed static files from the root of `main`.
The `.nojekyll` file preserves the existing HTML without Jekyll processing.
After editing Markdown, run the three commands above, review the changes,
and commit and push the updated sources, HTML, and ZIP to `main`.

Original teaching materials are not distributed. Project history, source-audit
inventories, logs, and local session information remain private and are excluded
from Git and the downloadable package. Global operating rules were not changed.
