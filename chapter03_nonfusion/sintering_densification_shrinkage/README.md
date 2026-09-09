# Sintering Densification and Isotropic Shrinkage

**Book link:** Chapter 3, Sections 3.6 and 3.8

## Purpose
Integrate a simple Arrhenius densification law and convert relative-density evolution to isotropic linear shrinkage using the chapter relation.

## Run
```bash
python main.py
```

## Expected output
- `densification_shrinkage.png`
- `history.csv`

## Scope and limitations
This is a compact educational reference implementation. It is intended to make the mathematical workflow executable and transparent; it is not a validated production solver for safety-critical engineering use.

**Modeling note:** Chapter 3 intentionally leaves the kinetic function `F(rho_rel)` general. For an executable demonstration this script chooses `F=1-rho_rel`; that closure is an educational choice, not a universal sintering law. The shrinkage relation itself follows the chapter's isotropic mass-conservation expression.
