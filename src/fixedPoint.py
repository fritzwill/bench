from collections.abc import Callable


def fixed_point(
    f: Callable[[float], float], approx: float, tol: float, n: int
) -> float:
    for i in range(n):
        p = f(approx)
        if abs(p - approx) < tol:
            return p
        approx = p
    raise ValueError(f"Method failed after {n} iterations")
