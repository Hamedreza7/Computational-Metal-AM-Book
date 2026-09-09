# Neural Surrogate for Melt-Pool Width

**Book link:** Chapter 4 neural-surrogate framework; dataset mirrors Chapter 6 Case 4

## Purpose
Train a very small neural network on the four-point educational LPBF dataset. A monotonicity penalty encourages width to increase with power and decrease with scan speed.

## Run
```bash
python main.py
```

## Expected output
- `training_history.csv`
- `fit.png`

## Scope and limitations
This is a compact educational reference implementation. It is intended to make the mathematical workflow executable and transparent; it is not a validated production solver for safety-critical engineering use.

