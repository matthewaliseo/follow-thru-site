"""Builds the site's HTML pages from the Markdown in _src.

Run from the repository root: python3 _src/build.py (needs `pip install markdown`).
"""
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [
    ("privacy", "Privacy Policy", "How CounterWait handles your information."),
    ("terms", "Terms of Use", "The terms for using CounterWait."),
    ("support", "Support", "Help with CounterWait."),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site">
  <a class="brand" href="./"><img src="icon.svg" alt="" width="32" height="32">CounterWait</a>
  <nav>
    <a href="support.html"{support}>Support</a>
    <a href="privacy.html"{privacy}>Privacy</a>
    <a href="terms.html"{terms}>Terms</a>
  </nav>
</header>
<main>
{body}
</main>
<footer class="site">
  <p>CounterWait is made by Matthew Aliseo in North Carolina. <a href="mailto:matthewaliseo@steppingstonegroup.net">matthewaliseo@steppingstonegroup.net</a></p>
</footer>
</body>
</html>
"""


def render(name, md_text, title, description):
    body = markdown.markdown(md_text, extensions=["tables", "md_in_html"])
    # Wide tables scroll on their own instead of the page.
    body = re.sub(r"<table>", '<div class="table"><table>', body)
    body = body.replace("</table>", "</table></div>")
    current = {key: (' aria-current="page"' if key == name else "") for key in ("support", "privacy", "terms")}
    return TEMPLATE.format(title=title, description=description, body=body, **current)


for name, title, description in PAGES:
    text = (ROOT / "_src" / f"{name}.md").read_text()
    (ROOT / f"{name}.html").write_text(render(name, text, f"{title} | CounterWait", description))
