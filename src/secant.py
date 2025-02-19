from collections.abc import Callable


def secant(
    f: Callable[[float], float], p0: float, p1: float, tol: float, N: int
) -> float:
    for i in range(N):
        p = p1 - ((f(p1) * (p1 - p0)) / (f(p1) - f(p0)))
        if abs(p - p1) < tol:
            return p
        p0 = p1
        p1 = p
    raise ValueError(f"The method failed after {N} iterations")
