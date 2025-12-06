# MyPages

A simple project to easily host and index static HTML files using GitHub Pages.

**-AppliedAILabs** in the file name required for display toggle
**Workflow:** >>  edit in **working** and then push to main so a deployment action can run


## Overview

MyPages generates an index page that automatically lists files containing "-AppliedAILabs" in your GitHub repository, making it easy to access specific static documents (like whitepapers, documentation, or other web content) hosted on GitHub Pages.

## Features

- **Filtered File Listing**: Dynamically displays only files containing "-AppliedAILabs"
- **GitHub Pages Integration**: Designed to work seamlessly with GitHub Pages hosting
- **Responsive Design**: Clean, mobile-friendly interface
- **Two Generation Methods**:
  - **Dynamic**: JavaScript-based index that fetches files via GitHub API
  - **Static**: Python-generated static HTML index using git commands

## Files

- `index.html`: The main index page (can be either dynamic or static)
- `scripts/update_index.py`: Python script to generate a static version of the index

## Usage

### Dynamic Index (Default)

The `index.html` file uses JavaScript to fetch and display the file list from the GitHub API. Simply upload your files (with "-AppliedAILabs" in the filename) to the repository and they'll appear in the index automatically.

### Static Index

To generate a static version of the index:

```bash
python scripts/update_index.py
```

This creates a static HTML file that doesn't require JavaScript or API calls.

## Setup

1. Fork or clone this repository
2. Add your files (with "-AppliedAILabs" in the filename) to the repository root
3. Enable GitHub Pages in your repository settings
4. Access your files via the generated index at your GitHub Pages URL

## Requirements

- For dynamic index: Modern browser with JavaScript enabled
- For static index: Python 3 and git

## Notes

- The index excludes `index.html` itself from the file listing
- Files are sorted alphabetically
- Error handling is included for API failures in the dynamic version
