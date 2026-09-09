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
- `tests/` — automated smoke tests and full example test runner

## Book release and reproducibility

The release tagged `v1.0.0-book` will correspond to the software snapshot associated with the published book. The live GitHub repository may later receive corrections, documentation improvements, and additional examples.

The archived Version 1.0 software release associated with the book has been assigned the following reserved Zenodo DOI:

**DOI:** [10.5281/zenodo.22668105](https://doi.org/10.5281/zenodo.22668105)

This DOI is reserved for the book-associated software release and will become publicly registered when the corresponding Zenodo record is published.

Readers seeking exact reproducibility of the book-associated software should use the archived Version 1.0 release rather than a later development version of the repository.

## Installation

Recommended Python version: **3.10 or newer**.

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
