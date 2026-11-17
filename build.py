#!/usr/bin/env python3
"""Project ACX website (Detritus78.github.io): turns the join guide's page source into a standalone page.

The source is ~/Work/ac/wiki-drafts/acx-join-guide.html, which is also the claude.ai preview: a page body without
<html>/<head>, as the artifact host adds those. This wraps it in a full document at join/index.html. Run it after
editing the source, then commit and push.

    python3 -I build.py
"""
import pathlib

SOURCE = pathlib.Path.home() / "Work/ac/wiki-drafts/acx-join-guide.html"
OUT = pathlib.Path(__file__).resolve().parent / "join/index.html"

page = SOURCE.read_text()
cut = page.index('<div class="page">')
head, body = page[:cut].rstrip(), page[cut:].strip()

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
""")
print(f"wrote {OUT}")
