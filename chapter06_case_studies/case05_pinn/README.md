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

**Book consistency:** This implementation corresponds to the corrected Chapter 6, Case 5 formulation. The collocation-point residuals, physics loss, and summary values are consistent with the one-dimensional heat equation and the updated manuscript. The corrected residual values are approximately $-0.0790$, $-0.1117$, and $-0.0790$, with $L_r \approx 0.00832$.
