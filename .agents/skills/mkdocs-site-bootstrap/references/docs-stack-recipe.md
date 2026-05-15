# Downstream docs stack recipe

If you are building documentation for a project that consumes one of the
skills in this repo (especially [`project-knowledge-harness`](../skills/project-knowledge-harness.md)
or [`quantatitive-factor-researcher`](../skills/quantatitive-factor-researcher.md)),
this is the docs stack we recommend.

It's the same stack this repo uses for its own docs, plus the optional
`mkdocstrings` layer for projects that have a Python API to document.

## TL;DR

```toml
# pyproject.toml
[project.optional-dependencies]
docs = [
  "mkdocs>=1.6",
  "mkdocs-material>=9.5",
  "mkdocstrings[python]>=0.24",   # only if you have a Python API
  "mkdocs-llmstxt>=0.1",
  "mkdocs-copy-to-llm>=0.1",
  "pymdown-extensions>=10.0",
]
```

```bash
# Local preview
uv sync --extra docs
uv run mkdocs serve

# Build static site
uv run mkdocs build --strict
```

## Why this stack

- **MkDocs + Material** — Markdown-first authoring, built-in search, a
  theme that doesn't need overrides for ~90% of projects, GitHub Pages
  deploy is one workflow file.
- **`mkdocstrings[python]`** — render API docs from Python docstrings via
  `::: package.module.symbol` directives in your Markdown. Only relevant
  if your project has a Python API; skip it otherwise.
- **`mkdocs-llmstxt`** — generates `/llms.txt` and `/llms-full.txt` so
  AI agents can discover and consume your docs without scraping HTML.
  Upstream is in maintenance mode but works fine; if it ever stops,
  swap in a hand-rolled post-build script.
- **`mkdocs-copy-to-llm`** — adds "Copy to LLM / Open in ChatGPT / Open
  in Claude" buttons on every page. Pure UX sugar; harmless if your
  audience doesn't use it.

## Why not these?

- **Sphinx + Furo + MyST + autodoc.** Strictly more powerful, but the
  setup and maintenance cost is meaningful. Recommended only if AI-facing
  Markdown output becomes a first-class requirement, or if your project
  has the kind of cross-project reference graph Sphinx is built for.
- **pdoc.** Single-file API doc generator. Great for "I just want HTML
  for my package", but no good story for guides, conventions pages, or
  llms.txt.
- **Rspress.** Best-in-class for AI-native output, but it's
  Node-first / frontend-product-docs-first; Python API reference is a
  bolt-on. Not a fit unless you're already on the Node ecosystem.
- **Quarto.** Excellent for notebook / tutorial / research-report
  workflows; not optimized for Python library documentation.

The longer version of this analysis (with the upstream-vs-inference
distinction made explicit) is preserved in the reference repo
[`mlflow-widgets/notes/docs-stack-evaluation.md`](https://github.com/daviddwlee84/mlflow-widgets/blob/main/notes/docs-stack-evaluation.md).

## Minimum `mkdocs.yml`

```yaml
site_name: Your Project
site_description: One sentence about your project.
site_url: https://yourname.github.io/your-project/
repo_url: https://github.com/yourname/your-project
edit_uri: edit/main/docs/

theme:
  name: material
  features:
    - navigation.instant
    - navigation.sections
    - navigation.indexes
    - search.suggest
    - content.code.copy
    - toc.follow

plugins:
  - search
  - mkdocstrings:        # remove this block if no Python API
      handlers:
        python:
          paths: [src]
          options:
            show_source: true
            show_root_heading: true
            members_order: source
            docstring_style: google
            merge_init_into_class: true
  - llmstxt:
      full_output: llms-full.txt
      sections:
        Guides: [index.md, getting-started.md]
        API Reference: [reference/*.md]
  - copy-to-llm:
      repo_url: "https://yourname.github.io/your-project"

markdown_extensions:
  - admonition
  - tables
  - toc:
      permalink: true
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.snippets:
      base_path: [., docs, docs/_snippets]
      check_paths: true

nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - API Reference:
      - Overview: reference/index.md
```

## GitHub Pages workflow

`.github/workflows/docs.yml`:

```yaml
name: Docs

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
      - 'pyproject.toml'
      - '.github/workflows/docs.yml'
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
      - run: uv sync --extra docs
      - run: uv run mkdocs build --strict
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v5
```

You also need to enable Pages in your repo settings: **Settings → Pages
→ Build and deployment → Source: GitHub Actions**. One-time setup.

## Linking rules inside `docs/`

`mkdocs build --strict` enforces these rules. Knowing them up front
saves an afternoon:

- Links **between files inside `docs/`** → relative paths (e.g.
  `[scripts](../reference/scripts.md)`).
- Links to **`.md` files outside `docs/`** → absolute GitHub URL
  (e.g. `https://github.com/yourname/your-project/blob/main/TODO.md`).
  Relative paths to `.md` files outside `docs/` are rejected by
  `--strict`.
- Links to **directories or non-`.md` files outside `docs/`** → relative
  paths are tolerated (downgraded to INFO).

If you want stricter validation (catch broken anchors too):

```yaml
validation:
  links:
    not_found: warn
    anchors: warn
```

## What this repo skips and why

- **`mkdocstrings[python]`** — there's no Python API to document. We
  installed everything else from the recipe to keep the patterns aligned
  with downstream projects.
- **Versioned docs (e.g. `mike`)** — single-version docs are enough for
  a personal skills collection. Add `mike` if you ever need to keep
  docs for old releases live.
