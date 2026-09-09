# PINN for the 1D Heat Equation

**Book link:** Chapter 4 PINN framework; same PDE used in Chapter 6 Case 5

## Purpose
Train a compact PyTorch PINN for `T_t = alpha T_xx` on `x∈[0,1]` using the hard-constrained trial form from the book, then compare with the exact sine-mode solution.

## Run
```bash
python main.py
```

## Expected output
- `pinn_vs_exact.png`
- `training_history.csv`

## Scope and limitations
This is a compact educational reference implementation. It is intended to make the mathematical workflow executable and transparent; it is not a validated production solver for safety-critical engineering use.

