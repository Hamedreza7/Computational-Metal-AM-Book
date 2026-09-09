# Case 5 — PINN Residual for the 1D Heat Equation

**Book link:** Chapter 6, Case 5

## Purpose
Evaluate the stated trial field and PDE residual at the three book collocation points, compare with the exact solution, and explicitly report the executable residual values.

## Run
```bash
python main.py
```

## Expected output
- `residuals.csv`
- `trial_vs_exact.png`

## Scope and limitations
This is a compact educational reference implementation. It is intended to make the mathematical workflow executable and transparent; it is not a validated production solver for safety-critical engineering use.

**Important:** See `../../docs/BOOK_VALIDATION_NOTES.md`. The script follows the governing PDE residual exactly as written in the chapter and reports the discrepancy with the current printed residual table.
