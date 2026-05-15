# MkDocs 2.0, Zensical, and why this stack pins `mkdocs<2`

The pinned upper bound on `mkdocs` (and `mkdocs-material<10`) in this skill's
`pyproject.toml.template` is not bit-rot — it is a deliberate guard against
the planned MkDocs 2.0 release. This page captures the situation as of
**2026-04** so future maintainers can decide when to lift the cap.

## TL;DR

- **MkDocs 2.0 will remove the entire plugin system.** Every plugin in this
  stack (`mkdocs-llmstxt`, `mkdocs-static-i18n`, `mkdocs-copy-to-llm`,
  `pymdown-extensions`'s superfences/snippets/tabbed) **stops working**.
- **The Material for MkDocs team has refused to follow MkDocs 2.0.** They
  are shipping a separate replacement called **Zensical**, positioned as a
  drop-in for MkDocs 1.x — *not* for 2.0.
- **No release date for MkDocs 2.0 has been announced** as of writing.
  Material 9.7.5+ has internally capped its dependency range to refuse
  MkDocs 2.0 — but we cap explicitly anyway, so a future Material release
  that drops the cap can't silently break us.
- **Don't migrate to MkDocs 2.0.** The realistic future migration target is
  Zensical (or an alternative framework), not 2.0 itself.

## What changes in MkDocs 2.0

Per the Material team's analysis
([blog post, 2026-02-18](https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/)):

| Change | Impact on this stack |
|---|---|
| Plugin system removed entirely | `llmstxt`, `static-i18n`, `copy-to-llm` all stop working. No 2.0 equivalents exist. |
| Theme system rewritten — nav passed as pre-rendered HTML, not structured data | Material's advanced navigation features become technically impossible. |
| No migration path from 1.x | A 2.0 upgrade is effectively a rewrite. |
| Closed contribution model | Community can't report bugs or contribute fixes. |
| Currently unlicensed | Unsuitable for production. |

The official MkDocs 2.0 dev docs ([encode.io/mkdocs](https://www.encode.io/mkdocs/))
describe the project as "a smart, simple, website design tool" but **do not
publish a feature changelog, performance benchmark, or migration guide**.
There is no documented user-facing benefit; the design choice is
maintainer-driven (simplify codebase by removing extension points), not
user-driven (solve a specific pain).

## Material team's response — Zensical

[Zensical](https://zensical.org/) is a new project from the Material for
MkDocs team, explicitly positioned as a **drop-in replacement for
MkDocs 1.x**.

What's known:

- "Built by the creators of Material for MkDocs."
- Self-described as "seamless compatibility with Material for MkDocs."
- Has a phased rollout strategy (Zensical's compatibility page mentions
  four phases) and a paid tier called Zensical Spark.
- **Plugin compatibility is unconfirmed** — i18n, llmstxt, copy-to-llm,
  and similar plugins are not on a published support list as of writing.
- No stable release; not safe to adopt yet.

The fact that Material's own team rejected forking MkDocs ("impractical
due to ecosystem dependencies") and instead built an alternative is the
strongest signal in the ecosystem about MkDocs 2.0's viability.

## Why we cap explicitly

Material 9.7.5+ already constrains its `mkdocs` dependency to refuse 2.0,
which means *today* a downstream `pip install mkdocs-material` won't
accidentally pull MkDocs 2.0. But:

- A future Material release could relax that constraint.
- `pyproject.toml` here lists `mkdocs` as a direct dependency, so
  `uv sync --extra docs` resolves it independently of Material's pin.
- Belt-and-suspenders: pinning ourselves means we don't depend on someone
  else's defensive pin to stay correct.

The cap is `mkdocs>=1.6,<2` and `mkdocs-material>=9.5,<10`. Both upper
bounds use the **next major** as the boundary, not a specific version, so
patch and minor releases of 1.x / 9.x continue to flow.

## When to re-evaluate

Lift the cap (or migrate off MkDocs entirely) **only when all of the
following are true**:

1. A successor framework reaches **stable release** (semver `1.0+`, or
   equivalent project signal of API stability).
2. That successor publishes **i18n support** equivalent to
   `mkdocs-static-i18n` (suffix or folder layout, fallback-to-default,
   per-language search).
3. That successor publishes **LLM-friendly output** equivalent to
   `mkdocs-llmstxt` + `mkdocs-copy-to-llm` (auto-generated `llms.txt` +
   per-page raw-markdown links).
4. The successor's plugin / extension model is documented and not
   maintainer-only-closed (so we can write a new plugin if we need one).

Until criteria 1–3 are met, **the realistic answer is "stay on 1.x."**
MkDocs 1.x and Material 9.x are mature, low-defect codebases; remaining on
them for 2–3 more years is operationally fine.

## What to avoid

- **Don't bump to MkDocs 2.0 to "see what's new."** There's no documented
  changelog and the plugin loss is total, not partial.
- **Don't fork MkDocs 1.x ourselves.** The Material team explicitly
  considered and rejected this; the maintenance burden is too high for
  individual users.
- **Don't adopt Zensical pre-stable.** It's a paid-tier project from a
  small team with no public release timeline; reserve it for a later
  evaluation when criteria 1–3 above are checkable against its docs.
- **Don't remove `mkdocs-static-i18n` or `mkdocs-llmstxt` to "future-proof"
  the stack.** These work fine today and the bilingual + LLM-friendly
  output are core features of this docs stack, not optional polish.

## Re-checking the situation

A periodic review (every ~6 months) is worth doing. Check, in order:

1. [`squidfunk/mkdocs-material` blog](https://squidfunk.github.io/mkdocs-material/blog/)
   — has the Material team announced a Zensical stable date or revised
   their MkDocs 2.0 stance?
2. [Zensical compatibility page](https://zensical.org/compatibility/) —
   does it now list i18n, llmstxt, copy-to-llm as supported?
3. [`mkdocs/mkdocs` discussions](https://github.com/mkdocs/mkdocs/discussions)
   — has the MkDocs 2.0 plugin decision been reversed or clarified? Has a
   release date been set?
4. The dependency caps in this skill's `assets/pyproject.toml.template`
   and the `pyproject.toml` of the `daviddwlee84/agent-skills` repo —
   if the criteria above are met, both should be lifted in the same
   change, with this reference page updated to record the rationale.

## Source links

- Material's MkDocs 2.0 analysis (2026-02-18):
  <https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/>
- Zensical home: <https://zensical.org/>
- Zensical compatibility: <https://zensical.org/compatibility/>
- MkDocs 2.0 dev docs: <https://www.encode.io/mkdocs/>
- MkDocs 2.0 community discussion (#4077):
  <https://github.com/mkdocs/mkdocs/discussions/4077>
