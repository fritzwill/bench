from collections.abc import Callable


def bisect(
    func: Callable[[float], float], low: float, high: float, tol: float, N: int
) -> float:
    if low > high:
        low, high = high, low
    if func(low) * func(high) > 0:
        raise ValueError(
            "Check input for low and high guess (f(low) and f(high) must have different signs)"
        )

    for i in range(N):
        mid = (high + low) / 2.0
        if func(mid) == 0 or (high - low) / 2.0 < tol:
            return mid
        if func(mid) * func(low) > 0:
            low = mid
        else:
            high = mid
    raise ValueError(f"Method failed after {N} iterations")
