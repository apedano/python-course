# Create MKDocs + Material

## Install everything (once)

Use a virtualenv (recommended):

```aiignore
python3 -m venv .venv
source .venv/bin/activate
```

Install MkDocs + Material:

```bash
pip install mkdocs mkdocs-material
```
Verify:
```aiignore
mkdocs --version
```

## Create the project

```aiignore
mkdocs new python-cheatsheet
```

## Minimal project

See [mkdocs.yml](python-cheatsheet/mkdocs.yml)

This already gives you:

* dark/light mode
* copy button on code blocks
* great Python syntax highlighting
* collapsible sections

## Create structure

Inside the `/doc` folder create folders for sections

```aiignore
mkdir basics collections itertools async typing gotchas
```

Example file [index.md](python-cheatsheet/docs/basics/index.md)

### Add navigation

[mkdocs.yml](python-cheatsheet/mkdocs.yml) (`nav` section)

## Run locally 

Target port can be specified
```
mkdocs serve -a 127.0.0.1:8001 
```

## Deploy for free (GitHub Pages)

```bash
pip install mkdocs-material[imaging]
```
Deploy 

```bash
mkdocs gh-deploy
```
https://chatgpt.com/c/69874d93-3930-8325-bed8-c30179cd8b3f