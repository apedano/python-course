# Create MKDocs + Material

## Install everything (once)

Use a virtualenv (recommended):

```aiignore
python3 -m venv .venv
source .venv/bin/activate
```

Run the file [activate_virtual_env.sh](activate_virtual_env.sh)

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

See [mkdocs.yml](mkdocs.yml)

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

Example file [index.md](python-cheatsheet/docs/basics/variables.md)

### Add navigation

[mkdocs.yml](mkdocs.yml) (`nav` section)

## Run locally 

Target port can be specified

```bash
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
The result will be

```bash
remote: Resolving deltas: 100% (13/13), done.
remote: 
remote: Create a pull request for 'gh-pages' on GitHub by visiting:
remote:      https://github.com/apedano/python-course/pull/new/gh-pages
remote: 
To github.com:apedano/python-course.git
 * [new branch]      gh-pages -> gh-pages
INFO    -  Your documentation should shortly be available at: https://apedano.github.io/python-course/
```
So the page will be available at the indicated url