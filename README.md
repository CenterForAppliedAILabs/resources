# Applied AI Labs — Resources (GitHub Pages)

A static site that indexes and links to AI-generated content files hosted on GitHub Pages.

## How It Works

Three components keep the site up to date:

- **`index.html`** — The main landing page. Uses JavaScript to call the GitHub Trees API, filters for filenames containing `-AppliedAILabs`, and renders them as clickable links. No build step required.

- **`scripts/update_index.py`** — Generates a static fallback version of `index.html` from `git ls-files`. Not currently in use but available if a no-JavaScript version is needed.

- **`.github/workflows/update-index.ymx`** — GitHub Actions workflow that runs the Python script on every push to `main`. Auto-commits changes with `[skip ci]` to prevent loops. (Note: the `.ymx` extension means GitHub Actions does not currently detect it. Rename to `.yml` to activate.)

## Adding New Content

1. Add your HTML or PDF file to the repo root.
2. Make sure the filename includes `-AppliedAILabs` — only files with that string appear in the index.
3. Commit and push to `main`.
4. The dynamic index picks it up immediately via the GitHub API.

## Adding a Launch Page

Launch pages (like `Newcomers-activity-prompt-examples-AppliedAILabs.html`) group related files behind a single entry point.

1. Create the HTML file in the repo root.
2. Include `-AppliedAILabs` in the filename so it appears in the main index.
3. Link to the individual content files using relative paths.
4. Add `target="_blank" rel="noopener"` to open links in new tabs.
5. Commit and push to `main`.

## File Filtering

Both the dynamic JavaScript and static Python versions filter the same way:

- Include files where the filename contains `-AppliedAILabs`
- Exclude `index.html`
- Sort alphabetically

To change the filter, update both:
- **Dynamic**: `index.html` line ~97 — `files.filter(p => p !== 'index.html' && p.includes('-AppliedAILabs'))`
- **Static**: `scripts/update_index.py` line ~58 — `files = [f for f in files if f != 'index.html' and '-AppliedAILabs' in f]`

## Local Testing

Open `index.html` directly in a browser. The dynamic version requires internet access to reach the GitHub API.
