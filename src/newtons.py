from collections.abc import Callable


def newtons(
    f: Callable[[float], float],
    fprime: Callable[[float], float],
    approx: float,
    tol: float,
    n: int,
) -> float:
    p0 = approx
    for _ in range(n):
        p = p0 - (f(p0) / fprime(p0))
        if abs(p - p0) < tol:
            return p
        p0 = p
    raise ValueError(f"The method failed after {n} iterations")
