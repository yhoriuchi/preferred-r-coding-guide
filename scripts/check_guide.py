"""Check rendered links, headings, tables, copied text, and R snippet syntax."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import collections
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


class InspectHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.tables = []
        self.in_table = False
        self.rows = []
        self.cells = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ['href', 'src']:
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'table':
            self.in_table = True
            self.rows = []
        if tag == 'tr':
            self.cells = 0
        if tag in ['td', 'th']:
            self.cells += 1

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.rows.append(self.cells)
        if tag == 'table':
            self.tables.append(self.rows)
            self.in_table = False


errors = []
summary = {}
for filename in ['index.html', 'evidence.html', 'verification.html']:
    source = ROOT / filename
    parsed = InspectHTML()
    parsed.feed(source.read_text())
    duplicate_ids = [key for key, n in collections.Counter(parsed.ids).items() if n > 1]
    if duplicate_ids:
        errors.append((filename, 'duplicate ids', duplicate_ids))
    for link in parsed.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = source.parent / unquote(url.path) if url.path else source
        if not target.exists():
            errors.append((filename, 'missing target', link))
        if not url.path and url.fragment and url.fragment not in parsed.ids:
            errors.append((filename, 'missing anchor', link))
    for rows in parsed.tables:
        if len(set(rows)) != 1:
            errors.append((filename, 'table columns', rows))
    summary[filename] = dict(ids=len(parsed.ids), links=len(parsed.links), tables=len(parsed.tables))

page = (ROOT / 'index.html').read_text()
payload = re.search(r'<script type="application/json" id="guide-text">(.*?)</script>', page, re.S).group(1)
expected = (ROOT / 'APPLY_GUIDE.md').read_text() + '\n\n---\n\n' + (ROOT / 'PREFERRED_R_STYLE.md').read_text()
assert json.loads(payload) == expected

chunks = re.findall(r'```r\n(.*?)```', (ROOT / 'PREFERRED_R_STYLE.md').read_text(), re.S)
with tempfile.TemporaryDirectory(prefix='rguide_snippets_') as directory:
    folder = Path(directory)
    for index, chunk in enumerate(chunks):
        (folder / f'chunk_{index:02d}.R').write_text(chunk)
    command = ['Rscript', '--vanilla', '-e',
               'files <- list.files(commandArgs(TRUE), full.names = TRUE); '
               'invisible(lapply(files, parse)); cat(length(files), "snippets parsed\\n")',
               str(folder)]
    result = subprocess.run(command, text=True, capture_output=True, check=True)
    summary['r_snippets'] = result.stdout.strip()

summary['copy_payload_matches'] = True
summary['errors'] = errors
(ROOT / 'analysis/html_checks.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
if errors:
    raise SystemExit(1)
