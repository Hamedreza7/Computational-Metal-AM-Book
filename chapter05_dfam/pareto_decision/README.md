# Pareto-Front and Weighted Design Decision

**Book link:** Chapter 5, Section 5.6

## Purpose
Identify non-dominated designs for three minimization objectives (mass, distortion, support volume), normalize the objectives, and select a preferred Pareto design using user-visible weights.

## Run
```bash
python main.py
```

## Expected output
- `pareto_designs.csv`
- `pareto_mass_distortion.png`

## Scope and limitations
This is a compact educational reference implementation. It is intended to make the mathematical workflow executable and transparent; it is not a validated production solver for safety-critical engineering use.

**Data note:** Chapter 5 presents the Pareto and weighted-sum framework but no fixed numerical design table. The small dataset in `designs.csv` is synthetic and exists only to demonstrate the book method.
