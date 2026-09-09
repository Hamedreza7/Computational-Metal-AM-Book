# Case 6 — AEPB Absorptivity Correction

**Book link:** Chapter 6, Case 6

## Purpose
Demonstrate a bounded state-dependent absorptivity closure inside a thermal-source calculation and reproduce the book source multiplier and one-step temperature rise.

## Run
```bash
python main.py
```

## Expected output
- `aepb_summary.csv`
- `absorptivity_vs_temperature.png`

## Scope and limitations
This is a compact educational reference implementation. It is intended to make the mathematical workflow executable and transparent; it is not a validated production solver for safety-critical engineering use.

**Closure note:** The chapter specifies the baseline state `(T=1200 K, alpha0=0.35, alpha=0.53)` but does not give a unique analytical correction law. The script uses the simplest bounded linear temperature correction passing through that worked point; it is labeled as an educational closure.
