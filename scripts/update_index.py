#!/usr/bin/env python3
import subprocess
import html
from pathlib import Path

REPO_INDEX = Path('index.html')

def git_ls_files():
    out = subprocess.check_output(['git', 'ls-files'])
    files = out.decode('utf-8', errors='ignore').splitlines()
    return files

def build_index_html(file_paths):
    header = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>html-content — Files</title>
  <style>
    body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:0 auto;padding:1rem;max-width:900px}
    h1{margin-top:0}
    ul{padding-left:1.25rem}
    li{margin:.35rem 0}
    a{color:#0366d6}
    .muted{color:#6a737d;font-size:0.95rem}
    .error{color:#842029;background:#f8d7da;padding:.5rem;border-radius:6px}
  </style>
</head>
<body>
  <header>
    <h1>Repository files — html-content</h1>
    <p class=\"muted\">Files in <strong>toddwmac/html-content</strong> containing "-AppliedAILabs" (this index file is excluded).</p>
  </header>

  <main>
    <section id=\"listing\">
"""
    footer = """    </section>
  </main>
</body>
</html>
"""
    # Build list markup
    if not file_paths:
        list_html = '      <p class=\"muted\">No matching files found (looking for files containing "-AppliedAILabs").</p>\n'
    else:
        list_html = '      <ul>\n'
        for p in file_paths:
            esc = html.escape(p)
            list_html += f'        <li><a href=\"{esc}\">{esc}</a></li>\n'
        list_html += '      </ul>\n'

    return header + list_html + footer

def main():
    files = git_ls_files()
    files = [f for f in files if f != 'index.html' and '-AppliedAILabs' in f]
    files.sort()

    new_content = build_index_html(files)

    if REPO_INDEX.exists():
        old = REPO_INDEX.read_text(encoding='utf-8')
        if old == new_content:
            print("index.html up-to-date; no changes.")
            return

    REPO_INDEX.write_text(new_content, encoding='utf-8')
    print("index.html updated.")

if __name__ == "__main__":
    main()
