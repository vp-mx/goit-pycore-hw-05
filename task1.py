from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """Returns a function that calculates the nth Fibonacci number using a cache to store intermediate results."""

    cache = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        """Calculates the nth Fibonacci number."""

        if n < 0 or not isinstance(n, int):
            raise ValueError("Number must be a positive integer")
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
