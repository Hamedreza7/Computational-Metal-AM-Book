# Book Validation Notes

This file records numerical and implementation checks performed while preparing the companion computational repository for the Springer book.

## Chapter 6, Case 5 — Resolved

The PINN collocation-point residuals, physics loss, and summary table were corrected in the manuscript so that they are consistent with the stated one-dimensional heat equation and the executable companion implementation.

For the three collocation points used in the worked example, the corrected residual values are approximately:

- \(R(0.25,0.1) = -0.0790\)
- \(R(0.50,0.1) = -0.1117\)
- \(R(0.75,0.1) = -0.0790\)

The corresponding mean squared physics residual is:

\[
L_r \approx 0.00832
\]

The manuscript and companion implementation are therefore consistent for this example.

## Release Status

No unresolved numerical discrepancy is currently recorded for Chapter 6, Case 5.

Additional validation notes may be added here if issues are identified during final testing of the Version 1.0 book companion code.
