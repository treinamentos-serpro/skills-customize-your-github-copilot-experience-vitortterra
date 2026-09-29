"""Starter code for comparing numerical root-finding methods."""

import math


def bisection(function, left, right, tolerance=1e-6, max_iterations=100):
    """Return (root, iterations) using the bisection method."""
    raise NotImplementedError("Implement the bisection method")


def newton_raphson(
    function, derivative, initial_guess, tolerance=1e-6, max_iterations=100
):
    """Return (root, iterations) using the Newton-Raphson method."""
    raise NotImplementedError("Implement the Newton-Raphson method")


def main():
    square_root_function = lambda value: value**2 - 2
    square_root_derivative = lambda value: 2 * value
    cosine_function = lambda value: math.cos(value) - value
    cosine_derivative = lambda value: -math.sin(value) - 1

    # Call both methods for each function and compare their iteration counts.
    raise NotImplementedError("Run and compare the required examples")


if __name__ == "__main__":
    main()