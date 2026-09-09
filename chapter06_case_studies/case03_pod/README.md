# Case 3 — POD Reduced-Order Thermal Model

**Book link:** Chapter 6, Case 3

## Purpose
Construct the book snapshot matrix, compute its SVD, report energy capture, and reconstruct the snapshots with rank 1 and rank 2.

## Run
```bash
python main.py
```

## Expected output
- `pod_energy.csv`
- `reconstruction_errors.csv`
- `rank2_reconstruction.png`

## Scope and limitations
This is a compact educational reference implementation. It is intended to make the mathematical workflow executable and transparent; it is not a validated production solver for safety-critical engineering use.

