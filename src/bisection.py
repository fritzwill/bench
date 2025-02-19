from collections.abc import Callable


def bisect(
    f: Callable[[float], float], low: float, high: float, tol: float, N: int
) -> float:
    if low > high:
        low, high = high, low
    if f(low) * f(high) > 0:
        raise ValueError(
            "Check input for low and high guess (f(low) and f(high) must have different signs)"
        )

    for _ in range(N):
        mid = (high + low) / 2.0
        f_mid = f(mid)
        if f_mid == 0 or (high - low) / 2.0 < tol:
            return mid
        if f_mid * f(low) > 0:
            low = mid
        else:
            high = mid
    raise ValueError(f"Method failed after {N} iterations")
