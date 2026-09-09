"""Fast CI checks for the book-linked equations and repository syntax."""

from pathlib import Path
import compileall
import math

import numpy as np


ROOT = Path(__file__).resolve().parents[1]

# Check Python syntax throughout the repository.
assert compileall.compile_dir(ROOT, quiet=1), "Python syntax check failed"


# Chapter 6, Case 1: final 6-node thermal vector
rho = 7800.0
cp = 500.0
k = 25.0
L = 5e-4
N = 6
dx = L / (N - 1)
dt = 1e-4
v = 0.5
sig = 1e-4
q0 = 1.25e13
x0 = 2e-4
Tamb = 300.0

alpha = k / (rho * cp)
Fo = alpha * dt / dx**2
x = np.arange(N) * dx

T = np.full(N, Tamb)

for n in range(4):
    xl = x0 + v * n * dt

    S = (
        dt
        * q0
        * np.exp(-((x - xl) ** 2) / (2 * sig**2))
        / (rho * cp)
    )

    old = T.copy()

    for i in range(1, N - 1):
        T[i] = (
            old[i]
            + Fo * (old[i + 1] - 2 * old[i] + old[i - 1])
            + S[i]
        )

    T[0] = Tamb
    T[-1] = Tamb


book = np.array(
    [300.00, 656.66, 1134.64, 1336.70, 946.38, 300.00]
)

assert np.max(np.abs(T - book)) < 0.02


# Chapter 6, Case 2: thermo-mechanical anchors
weights = np.array([0.5, 1, 1, 1, 1, 0.5])

Tbar = (weights @ book) / 5

assert abs(Tbar - 874.876) < 0.01

sigma = -200e9 * 12e-6 * (Tbar - 300) / 1e6

assert abs(sigma + 1379.7) < 0.2


# Chapter 6, Case 3: POD energy capture
Ts = np.array(
    [
        [300, 494.40, 620.51, 494.40, 343.38, 300],
        [300, 594.08, 887.20, 775.65, 454.33, 300],
        [300, 637.39, 1055.66, 1082.72, 659.44, 300],
        [300, 656.66, 1134.64, 1336.70, 946.38, 300],
    ],
    dtype=float,
).T

_, s, _ = np.linalg.svd(Ts - 300, full_matrices=False)

ce = np.cumsum(s * s / np.sum(s * s))

assert abs(ce[0] - 0.9802) < 3e-4
assert abs(ce[1] - 0.9996) < 3e-4


# Chapter 6, Case 4: neural-surrogate forward result
h = 1 / (1 + np.exp(-0.3))

pred = 35 * h + 5

assert abs(pred - 25.104) < 0.01


# Chapter 6, Case 5:
# mathematically consistent heat-equation PINN residual
coef = -1 + 0.1 * 0.9 * math.pi**2

R = coef * np.sin(
    math.pi * np.array([0.25, 0.50, 0.75])
)

assert np.mean(R * R) < 0.009


# Chapter 6, Case 6
assert abs((0.53 / 0.35) * 1.6 - 2.422857) < 1e-5


# Chapter 6, Case 7
ig = 220 / 350 + 240 / 1100

assert abs((1 - ig) - 0.153) < 0.002


# Chapter 6, Case 8
sres = -200 + 0.30 * 1450 + 1e-5 * 2.1e6

margin = 1 - (
    180 / 450
    + (60 + sres) / 840
)

assert abs(sres - 256) < 1e-9
assert abs(margin - 0.224) < 0.002


print(
    "Smoke tests passed: syntax + Chapter 6 numerical anchors."
)
