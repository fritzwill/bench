import math
from src.bisection import bisect
from src.fixedPoint import fixed_point
from src.newtons import newtons
from src.secant import secant

# This file is meant to contain examples of using each function in src/


def bisect_example():
    """Bisection method example usage."""
    # globals for the algorithm
    TOL = 10**-5
    A = 0
    B = 10
    N = 100

    def solve_func(x: float) -> float:
        return math.pow(x, 3) - x - 2

    result = bisect(solve_func, A, B, TOL, N)
    print(f"Bisection method solution: x = {result}")


def fixed_point_example():
    """Fixed point method example usage."""
    # globals for the algorithm
    APPROX = 4.6
    TOL = 10**-4
    N = 100

    def solve_func(x: float) -> float:
        return (1 / math.tan(x)) - (1 / x) + x

    result = fixed_point(solve_func, APPROX, TOL, N)
    print(f"Fixed point solution: x = {result}")


def newtons_example():
    """Newton's method example usage."""
    # globals for the algorithm
    APPROX = 0.1
    TOL = 10**-5
    N = 100

    def solve_func(x: float) -> float:
        return math.pow((1 + x), 204) - 440 * x - 1

    def solve_func_prime(x: float) -> float:
        return 204 * math.pow((x + 1), 203) - 440

    result = newtons(solve_func, solve_func_prime, APPROX, TOL, N)
    print(f"Newton's method solution: x = {result}")


def secant_example():
    """Secant method example usage."""
    # globals for the algorithm
    TOL = 10**-5
    N = 100

    def solve_func(x: float) -> float:
        return math.pow((1 + x), 204) - 440 * x - 1

    result = secant(solve_func, 0.1, 0.09, TOL, N)
    print(f"Secant method solution: x = {result}")


# Main execution of the example script uses above
if __name__ == "__main__":
    bisect_example()
    fixed_point_example()
    newtons_example()
    secant_example()
