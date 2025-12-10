# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**MyPages** is a GitHub Pages project that hosts and indexes static HTML files (primarily whitepapers and AI-enhanced content from Applied AI Labs). The repository maintains a dynamic or static index page that filters and displays files containing "-AppliedAILabs" in their filenames.

## Architecture

The project consists of three main components:

1. **index.html** - The main entry point, currently configured as a dynamic index page that uses JavaScript and the GitHub API to fetch and display files from the repository. Can be regenerated as a static version using the Python script.

2. **scripts/update_index.py** - A Python utility that generates a static version of `index.html` by reading files from git. This is useful when you want a version that doesn't depend on JavaScript or GitHub API calls.

3. **.github/workflows/update-index.ymx** - GitHub Actions workflow that automatically regenerates `index.html` when code is pushed to the main branch. The workflow prevents infinite loops by only running when pushes are not from the `github-actions[bot]` user.

## Development Workflow

The project uses a **working branch pattern**:
- All edits should be made in the `working` branch
- Push changes to `working` to test locally
- Create a pull request from `working` to `main` when ready
- Once merged to `main`, the GitHub Actions workflow automatically regenerates `index.html` and commits the changes

## Common Commands

### Generate static index.html
```bash
python3 scripts/update_index.py
```
This reads all files tracked by git, filters for those containing "-AppliedAILabs", and regenerates the static HTML file. Only commits changes if content has actually changed.

### Check which files would be indexed
```bash
git ls-files | grep -AppliedAILabs
```

### Test the dynamic index locally
Open `index.html` in a browser. The JavaScript will fetch from the GitHub API and display matching files.

## Key Implementation Details

### File Filtering
Both the dynamic JavaScript version and static Python version filter files the same way:
- Include only files where the filename contains "-AppliedAILabs"
- Exclude `index.html` itself
- Sort results alphabetically

### Dynamic vs Static Index Generation
- **Dynamic (current)**: `index.html` uses JavaScript to call the GitHub API (requires internet, supports real-time updates)
- **Static**: `scripts/update_index.py` generates a hardcoded HTML file with a list of files at the time it's run

### GitHub Actions Automation
The workflow in `.github/workflows/update-index.ymx`:
- Triggers on every push to `main`
- Prevents self-triggered recursion by checking if the actor is not the `github-actions[bot]`
- Runs the Python script to regenerate `index.html`
- Auto-commits and pushes changes if the file was modified (with `[skip ci]` to prevent infinite loops)

## File Structure

```
resources/
├── CLAUDE.md                          # This file
├── index.html                         # Main index page (dynamic)
├── scripts/
│   └── update_index.py               # Static index generator
├── .github/
│   └── workflows/
│       └── update-index.ymx          # GitHub Actions workflow
└── *.pdf                             # Whitepapers and content files
```

## Common Modifications

### Adding a new static file
1. Create or add your file to the repository
2. Ensure the filename contains "-AppliedAILabs" for it to be indexed
3. Commit and push to `main` (or `working` first)
4. The GitHub Actions workflow will automatically regenerate the index

### Changing the file filter pattern
Edit the file pattern check in:
- **Dynamic version**: Line 96 in `index.html` - `files.filter(p => p !== 'index.html' && p.includes('-AppliedAILabs'))`
- **Static version**: Line 58 in `scripts/update_index.py` - `files = [f for f in files if f != 'index.html' and '-AppliedAILabs' in f]`

### Modifying the HTML styling
- For dynamic index: Edit the `<style>` block in `index.html` (lines 7-15)
- For static index: Edit the `header` string in `scripts/update_index.py` (lines 14-38)

### Updating the page title or description
- Dynamic: Edit the content in `index.html` (lines 6, 25-31)
- Static: Edit the header strings in `scripts/update_index.py` (lines 18-19, 33)
