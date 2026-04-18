# Applied AI Labs — Resources (GitHub Pages)

A static site that indexes and links to AI-generated content files hosted on GitHub Pages.

## How It Works

Four components keep the site up to date:

- **`index.html`** — The main landing page. Uses JavaScript to call the GitHub Trees API, filters for filenames containing `-AppliedAILabs`, organizes them into sections using `sections.json`, and renders them as clickable links grouped under headings.

- **`sections.json`** — Config file that defines how files are organized into named sections. Contains section titles, descriptions, and glob patterns for matching filenames. Edit this file to add, remove, or reorder sections.

- **`scripts/update_index.py`** — Generates a static version of `index.html` from `git ls-files` and `sections.json`. Runs automatically via GitHub Actions.

- **`.github/workflows/update-index.ymx`** — GitHub Actions workflow that runs the Python script on every push to `main`. Auto-commits changes with `[skip ci]` to prevent loops. (Note: the `.ymx` extension means GitHub Actions does not currently detect it. Rename to `.yml` to activate.)

## Adding New Content

1. Add your HTML or PDF file to the repo root.
2. Make sure the filename includes `-AppliedAILabs` — only files with that string appear in the index.
3. Check if the filename matches an existing glob pattern in `sections.json`. If it does, you're done.
4. If it doesn't match any pattern, add a new pattern to the appropriate section in `sections.json` (see below).
5. Commit and push to `main`.

## The sections.json File

`sections.json` is an ordered JSON array. Each object defines one section:

```json
{
  "title": "Section Heading",
  "description": "Optional subtitle text shown below the heading",
  "patterns": ["filename-pattern*-AppliedAILabs*"]
}
```

| Field         | Required | Description                                          |
|---------------|----------|------------------------------------------------------|
| `title`       | Yes      | The section heading displayed on the page            |
| `description` | No       | A subtitle shown below the heading                   |
| `patterns`    | Yes      | Array of glob patterns using `*` and `?` wildcards   |

### Glob Pattern Examples

| Pattern                                    | What it matches                                                      |
|--------------------------------------------|----------------------------------------------------------------------|
| `"Vibe Coding*-AppliedAILabs*"`            | Any file starting with "Vibe Coding" and containing "-AppliedAILabs" |
| `"*newcomer*-AppliedAILabs*"`              | Any file containing "newcomer" and "-AppliedAILabs" anywhere         |
| `"10-classroom-challenges-*-AppliedAILabs*"` | Files starting with "10-classroom-challenges-"                     |
| `"ai-feature-comparison-AppliedAILabs*"`   | Exactly that file (no wildcard before the name)                      |

### Current Sections

1. AI Mindset and Leadership (7 files)
2. Vibe Coding (2 files)
3. Newcomer Activity Prompts (7 files)
4. Classroom Challenges (2 files)
5. AI Feature Comparisons (1 file)
6. AI for Detailers (2 files)
7. Governance and Analysis (3 files)

## Prompt: Update sections.json

Use the following prompt with an AI assistant when you need to update sections. Replace the bracketed items with your actual values.

---

**Copy and paste the prompt below:**

> Read the file `sections.json` in this repository. I need to update the section configuration.
>
> **What I want to do:** [describe your change — examples below]
>
> Examples:
> - "Add a new file called `My New Paper-AppliedAILabs.pdf` to section 1 (AI Mindset and Leadership)"
> - "Create a new section called '8. Research Papers' with description 'Academic research and studies' and assign these files: [list filenames]"
> - "Move the file `prompt-best-practices-grok-AppliedAILabs.html` from section 3 to section 7"
> - "Rename section 2 from 'Vibe Coding' to 'AI Coding Tools' and update its description"
> - "Reorder the sections so Classroom Challenges comes before Newcomer Activity Prompts"
>
> After making the change:
> 1. Verify every file containing `-AppliedAILabs` (excluding `index.html`) is matched by exactly one section pattern — no file should appear in "Uncategorized"
> 2. Show me the updated `sections.json`

---

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
- Sort alphabetically within each section

Files not matched by any section pattern appear in an "Uncategorized" section at the bottom of the page.

## Local Testing

Open `index.html` in a browser with a local server:

```bash
python -m http.server
```

Then visit `http://localhost:8000`. The dynamic version requires internet access to reach the GitHub API and `sections.json`.

To generate the static version locally:

```bash
python scripts/update_index.py
```
