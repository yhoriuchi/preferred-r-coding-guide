"""Build local, dependency-light HTML guides from the maintained Markdown."""
from pathlib import Path
import html
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def render_markdown(text):
    command = [
        'Rscript', '--vanilla', '-e',
        'cat(commonmark::markdown_html(paste(readLines("stdin", warn = FALSE), '
        'collapse = "\\n"), extensions = c("table", "autolink")))'
    ]
    return subprocess.run(command, input=text, text=True, check=True,
                          capture_output=True).stdout


def add_anchors(body):
    headings = []

    def replace(match):
        level, text = match.groups()
        plain = re.sub('<[^>]+>', '', text)
        anchor = re.sub('[^a-z0-9]+', '-', html.unescape(plain).lower()).strip('-')
        if level == '2':
            headings.append((anchor, plain))
        return f'<h{level} id="{anchor}">{text}</h{level}>'

    return re.sub(r'<h([23])>(.*?)</h\1>', replace, body), headings


def shell(title, contents, actions='', subtitle='', show_page_views=False):
    page_views = (
        '    <p><img src="https://hits.sh/yhoriuchi.github.io/preferred-r-coding-guide.svg?label=page%20views" alt="Page views"></p>\n'
        if show_page_views else ''
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <meta name="description" content="Yusaku Horiuchi's source-based guide to readable R analysis with AI.">
  <title>{html.escape(title.replace('<br>', ' '))}</title>
  <link rel="stylesheet" href="assets/site.css">
  <link rel="stylesheet" href="assets/guide.css">
  <script src="assets/guide.js" defer></script>
</head>
<body>
<a class="skip-link" href="#guide-content">Skip to guide</a>
<main class="page-shell">
  <header class="hero">
    <h1>{title}</h1>
    <ul class="metadata">
      <li><strong>Author:</strong> Yusaku Horiuchi</li>
      <li><strong>Affiliation:</strong> Syde P. Deeb Eminent Scholar in Political Science, Florida State University</li>
      <li><strong>Created:</strong> October 24, 2026</li>
      <li><strong>Last revised:</strong> October 24, 2026</li>
    </ul>
{page_views}    <p>{subtitle}</p>
    {actions}
  </header>
  {contents}
  <footer><p>Version 1.0 · Prepared with AI assistance from the supplied Waseda 2026 materials.
  Confirmed preferences, course-derived defaults, and recommendations are distinguished.</p>
  <p><a href="index.html">Guide</a> · <a href="evidence.html">Source evidence</a> ·
  <a href="verification.html">Verification</a> · <a href="PREFERRED_R_STYLE.md" download>Markdown</a></p></footer>
</main>
</body>
</html>
'''


guide = (ROOT / 'PREFERRED_R_STYLE.md').read_text()
prompt = (ROOT / 'APPLY_GUIDE.md').read_text()
body = render_markdown('## 1.' + guide.split('## 1.', 1)[1])
body, headings = add_anchors(body)
body = body.replace('href="analysis/EVIDENCE.md"', 'href="evidence.html"')
body = body.replace('href="analysis/VERIFICATION.md"', 'href="verification.html"')
toc = '<nav class="contents" aria-label="Contents"><h2>Contents</h2><ol>'
for anchor, title in headings:
    clean_title = re.sub(r'^\d+\.\s*', '', title)
    toc += f'<li><a href="#{anchor}">{clean_title}</a></li>'
toc += '</ol></nav>'
cards = '''<section class="summary-grid" aria-label="Guide overview">
<article class="summary-card"><h2>Familiar code, visible decisions</h2>
<p>Readable sections, consistent tidyverse, inspectable data, and figures that explain the comparison.</p></article>
<article class="summary-card"><h2>Evidence you can check</h2>
<p>All 35 supplied R scripts reviewed, plus the course style document and seven Technical Notes.</p></article>
</section>'''
actions = '''<div class="hero-actions">
<button class="button button-primary" type="button" id="copy-guide">Copy Guide + AI Instructions</button>
<a class="button" href="PREFERRED_R_STYLE.md" download>Download Markdown</a>
<a class="button" href="preferred_r_coding_guide.zip" download>Download Guide Package</a>
<span class="copy-status" id="copy-status" role="status" aria-live="polite"></span>
</div>
<details class="copy-fallback" id="copy-fallback" hidden><summary>Select and copy manually</summary>
<textarea id="copy-text" aria-label="Complete guide and AI instructions" readonly></textarea></details>'''
if not (ROOT / 'preferred_r_coding_guide.zip').exists():
    actions = actions.replace(
        '<a class="button" href="preferred_r_coding_guide.zip" download>Download Guide Package</a>\n', '')
payload = json.dumps(prompt + '\n\n---\n\n' + guide).replace('<', '\\u003c')
contents = cards + toc + '<article id="guide-content">' + body + '</article>'
contents += '<script type="application/json" id="guide-text">' + payload + '</script>'
result = shell('My Preferred<br>R Coding Guide', contents, actions,
               'AI can do the analysis. The code should still feel like mine—clear enough '
               'to understand quickly, inspect confidently, and rerun from start to finish.',
               show_page_views=True)
(ROOT / 'index.html').write_text(result)

for source, dest, title in [
    ('analysis/EVIDENCE.md', 'evidence.html', 'Source Evidence'),
    ('analysis/VERIFICATION.md', 'verification.html', 'Verification Record')
]:
    path = ROOT / source
    if path.exists():
        rendered = render_markdown(path.read_text())
        rendered = re.sub(r'<h1>.*?</h1>', '', rendered, count=1)
        rendered, _ = add_anchors(rendered)
        contents = '<p class="return-link"><a href="index.html">← Return to the guide</a></p>'
        contents += '<article id="guide-content">' + rendered + '</article>'
        (ROOT / dest).write_text(shell(title, contents, subtitle='A companion to My Preferred R Coding Guide.'))
print('Built index.html and available companion pages.')
