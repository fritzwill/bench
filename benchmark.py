import timeit
from collections.abc import Callable
from src.secant import secant
from src.newtons import newtons
from src.fixedPoint import fixed_point
from src.bisection import bisect


# Define functions and their derivatives
def easy_func(x: float) -> float:
    return x**2 - 4


def easy_func_prime(x: float) -> float:
    return 2 * x


def hard_func(x: float) -> float:
    return x**3 - 2 * x + 2


def hard_func_prime(x: float) -> float:
    return 3 * x**2 - 2


def really_hard_func(x: float) -> float:
    return x**5 - x**4 + x**3 - x**2 + x - 1


def really_hard_func_prime(x: float) -> float:
    return 5 * x**4 - 4 * x**3 + 3 * x**2 - 2 * x + 1


# Benchmark settings
APPROX = 0.1
TOL = 10**-5
N = 100
A = -2
B = 2


def benchmark_method(
    method, func: Callable[[float], float], func_prime: Callable[[float], float]
):
    if method == secant:
        return lambda: secant(func, APPROX, APPROX - 0.01, TOL, N)
    elif method == newtons:
        return lambda: newtons(func, func_prime, APPROX, TOL, N)
    elif method == fixed_point:
        return lambda: fixed_point(func, APPROX, TOL, N)
    elif method == bisect:
        return lambda: bisect(func, A, B, TOL, N)
    else:
        raise ValueError("Invalid method")


if __name__ == "__main__":
    methods = {
        "Secant Method": secant,
        "Newton's Method": newtons,
        # "Fixed-Point Method": fixed_point,
        "Bisection Method": bisect,
    }

    functions = {
        "Easy Function": (easy_func, easy_func_prime),
        # "Hard Function": (hard_func, hard_func_prime),
        "Really Hard Function": (really_hard_func, really_hard_func_prime),
    }

    results = []

    for func_name, (func, func_prime) in functions.items():
        for method_name, method in methods.items():
            print(f"running {method_name} on {func_name} ... ", end="")
            timer = timeit.Timer(benchmark_method(method, func, func_prime))
            print("done")
            time_taken = timer.timeit(number=100)
            results.append((method_name, func_name, time_taken))

    print()
    print(f"{'Method':<20} {'Function':<25} {'Time (s) for 100 runs':<25}")
    print("=" * 80)
    for method_name, func_name, time_taken in results:
        print(f"{method_name:<20} {func_name:<25} {time_taken:<25.8f}")
