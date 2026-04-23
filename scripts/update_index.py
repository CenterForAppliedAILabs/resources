#!/usr/bin/env python3
import subprocess
import html
import json
import fnmatch
from pathlib import Path

REPO_INDEX = Path('index.html')
SECTIONS_FILE = Path('sections.json')

def git_ls_files():
    out = subprocess.check_output(['git', 'ls-files'])
    files = out.decode('utf-8', errors='ignore').splitlines()
    return files

def load_sections():
    if not SECTIONS_FILE.exists():
        return []
    with open(SECTIONS_FILE, encoding='utf-8') as f:
        return json.load(f)

def build_index_html(file_paths):
    header = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Applied AILabs-Whitepapers</title>
  <style>
    body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:0 auto;padding:1rem;max-width:900px}
    h1{margin-top:0}
    ul{padding-left:1.25rem}
    li{margin:.35rem 0}
    a{color:#0366d6}
    .muted{color:#6a737d;font-size:0.95rem}
    .error{color:#842029;background:#f8d7da;padding:.5rem;border-radius:6px}
    .section{margin-top:2rem}
    .section h2{margin-bottom:.25rem;font-size:1.15rem;border-bottom:1px solid #e1e4e8;padding-bottom:.3rem}
    .section .desc{color:#6a737d;font-size:.9rem;margin-top:0;margin-bottom:.5rem}
  </style>
</head>
<body>
  <header style="text-align:center;">
    <img src="https://centerforappliedai.com/wp-content/uploads/2025/03/8e2adab0e3f168217b0338d68bba5992.png"
         alt="Center For Applied AI Logo"
         style="max-width:150px; display:block; margin:0 auto;">
    <p class="muted" style="margin-bottom:20px;">
        <span style="font-size:150%; font-weight:bold;">AI Colaborative Whitepapers and AI Enhanced Content Examples</span> <br>
        <em>Confirm any resources or refferences</em>.
    </p>
  </header>

  <main>
    <section id="listing">
"""
    footer = """    </section>

  <div class="muted" style="margin-top:15px;">
  <b>Links We Like:</b><br>
  <a href="https://lmcouncil.ai" target="_blank" rel="noopener noreferrer">LMCouncil.ai - Multi&#8209;model collaboration made easy</a>
  </div>

  </main>
</body>
</html>
"""
    sections = load_sections()
    matched = set()

    if not file_paths:
        list_html = '      <p class="muted">No matching files found (looking for files containing "-AppliedAILabs").</p>\n'
    elif not sections:
        list_html = '      <ul>\n'
        for p in file_paths:
            esc = html.escape(p)
            list_html += f'        <li><a href="{esc}" target="_blank" rel="noopener noreferrer">{esc}</a></li>\n'
        list_html += '      </ul>\n'
    else:
        list_html = ''
        for section in sections:
            section_files = []
            for pattern in section.get('patterns', []):
                matches = fnmatch.filter(file_paths, pattern)
                for m in matches:
                    if m not in matched:
                        section_files.append(m)
                        matched.add(m)
            if not section_files:
                continue
            section_files.sort()
            title = html.escape(section.get('title', 'Untitled'))
            list_html += f'      <div class="section">\n'
            list_html += f'        <h2>{title}</h2>\n'
            desc = section.get('description')
            if desc:
                list_html += f'        <p class="desc">{html.escape(desc)}</p>\n'
            list_html += '        <ul>\n'
            for p in section_files:
                esc = html.escape(p)
                list_html += f'          <li><a href="{esc}" target="_blank" rel="noopener noreferrer">{esc}</a></li>\n'
            list_html += '        </ul>\n'
            list_html += '      </div>\n'

        uncategorized = [f for f in file_paths if f not in matched]
        if uncategorized:
            list_html += '      <div class="section">\n'
            list_html += '        <h2>Uncategorized</h2>\n'
            list_html += '        <ul>\n'
            for p in uncategorized:
                esc = html.escape(p)
                list_html += f'          <li><a href="{esc}" target="_blank" rel="noopener noreferrer">{esc}</a></li>\n'
            list_html += '        </ul>\n'
            list_html += '      </div>\n'

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
