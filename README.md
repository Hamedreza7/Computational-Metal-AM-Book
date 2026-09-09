# Computational Metal AM Book — Companion Code

Companion educational source code for the Springer book **Computational Metal Additive Manufacturing: Advanced Multiphysics and AI-Enhanced Simulation**.

## Purpose

This repository provides compact, transparent implementations of selected computational workflows presented in the book. The examples are intended to help students and researchers connect governing equations and modeling concepts to executable code. They are educational reference implementations rather than validated production software for safety-critical engineering use.

## Repository organization

- `chapter02_multiphysics/` — fusion-based metal AM multiphysics examples
- `chapter03_nonfusion/` — Binder Jetting and electrochemical AM examples
- `chapter04_ai/` — neural surrogates, PINNs, and AI-enhanced physics-based examples
- `chapter05_dfam/` — design-for-AM and optimization examples
- `chapter06_case_studies/` — executable versions of selected worked case studies
- `data/` — small example datasets created for the companion code
- `docs/` — repository documentation and book-to-code mapping

## Book release and reproducibility

The release tagged `v1.0.0-book` will correspond to the software snapshot associated with the published book. The live GitHub repository may later receive corrections, documentation improvements, and additional examples.

A permanent Zenodo archival DOI will be added before publication of the book.

## Installation

Recommended Python version: **3.10 or newer**.

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Citation

The final software citation and Zenodo DOI will be added in `CITATION.cff` and in Appendix H of the book before the `v1.0.0-book` release is frozen.

## License

The companion source code is released under the MIT License. The Springer book itself is not covered by this software license.
