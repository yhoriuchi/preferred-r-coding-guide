"""Package the public guide without local history, audits, or session data."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    'index.html', 'evidence.html', 'verification.html',
    'README.md', 'PREFERRED_R_STYLE.md', 'APPLY_GUIDE.md',
    'preferred_r_coding_guide.Rproj',
    'scripts/build_guide.py', 'scripts/package_guide.py',
    'scripts/check_guide.py',
    'analysis/EVIDENCE.md', 'analysis/VERIFICATION.md',
    'assets/site.css', 'assets/guide.css', 'assets/guide.js',
    'templates/analysis_script.R',
    'examples/01_readable_analysis.R',
    'examples/02_wrangling_and_functions.R',
    'examples/figures/treatment_effect.pdf',
    'examples/figures/treatment_effect.png',
    'examples/figures/sample_counts.png',
    'examples/output/analysis_data.rds',
    'examples/output/sample_accounting.csv',
    'examples/output/group_summary.csv',
    'examples/output/model_results.csv',
    'examples/output/effect_plot_data.csv',
    'examples/output/monthly_data.csv',
    'examples/output/figure_caption.txt',
]

destination = ROOT / 'preferred_r_coding_guide.zip'
temporary = destination.with_suffix('.tmp.zip')
with ZipFile(temporary, 'w', ZIP_DEFLATED) as archive:
    for name in FILES:
        data = (ROOT / name).read_bytes()
        if name == 'index.html':
            data = data.replace(
                b'<a class="button" href="preferred_r_coding_guide.zip" download>Download Guide Package</a>\n', b'')
        archive.writestr('preferred_r_coding_guide/' + name, data)
with ZipFile(temporary) as archive:
    assert archive.testzip() is None
temporary.replace(destination)
print(f'Packaged {len(FILES)} public files into {destination.name}.')
