"""Minimal exact MLN inference (Python standard library only).
Two atoms A=smokes(alice), B=smokes(bob).
Soft formula: A => B, with weight 1.5.
Evidence A=True. Enumerate possible values of B.
"""
from itertools import product
from math import exp

weight = 1.5
worlds = []
for a, b in product((False, True), repeat=2):
    formula_true = (not a) or b  # a => b
    score = exp(weight * int(formula_true))
    worlds.append((a, b, score))

conditioned = [(b, score) for a, b, score in worlds if a]
z = sum(score for _, score in conditioned)
p_b = sum(score for b, score in conditioned if b) / z
print(f"P(smokes(bob) | smokes(alice)) = {p_b:.6f}")
print("Expected: 0.817574")
