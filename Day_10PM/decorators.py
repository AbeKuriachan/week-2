"""
Custom Decorators Module

Implements three decorators:

1. @timer  -> Measures execution time
2. @logger -> Logs function calls and results
3. @retry  -> Retries function on failure

Concepts used:
- Closures
- functools.wraps
- *args and **kwargs
"""

import time
import functools
from typing import Callable, Any



# Timer Decorator


def timer(func: Callable) -> Callable:
    """
    Measure execution time of a function.

    Args:
        func: Function to wrap

    Returns:
        Wrapped function

    Example:
        >>> @timer
        >>> def slow():
        >>>     time.sleep(1)
        >>> slow()
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        elapsed = end - start

        print(f"[TIMER] {func.__name__} executed in {elapsed:.4f} seconds")

        return result

    return wrapper



# Logger Decorator


def logger(func: Callable) -> Callable:
    """
    Log function name, arguments, and return value.

    Args:
        func: Function to wrap

    Returns:
        Wrapped function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"[LOGGER] Calling {func.__name__}")
        print(f"[LOGGER] args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"[LOGGER] {func.__name__} returned {result}")

        return result

    return wrapper



# Retry Decorator


def retry(max_attempts: int = 3) -> Callable:
    """
    Retry a function if it raises an exception.

    Args:
        max_attempts: Number of retry attempts

    Returns:
        Decorator

    Example:
        >>> @retry(max_attempts=3)
        >>> def unstable():
        >>>     ...
    """

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:

            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    attempts += 1
                    print(
                        f"[RETRY] {func.__name__} failed "
                        f"(attempt {attempts}/{max_attempts})"
                    )

                    if attempts >= max_attempts:
                        print("[RETRY] Max attempts reached")
                        raise

        return wrapper

    return decorator



# Example Usage


if __name__ == "__main__":

    import random

    print("\n=== Decorator Demo ===\n")

    # Example 1: Timer
    @timer
    def slow_function():
        time.sleep(1)
        return "Finished"

    print(slow_function())


    # Example 2: Logger
    @logger
    def add(a, b):
        return a + b

    print("\nAdd result:", add(5, 3))


    # Example 3: Retry
    @retry(max_attempts=3)
    def unstable_function():
        if random.random() < 0.7:
            raise ValueError("Random failure")
        return "Success!"

    print("\nRetry demo:")
    try:
        print(unstable_function())
    except Exception as e:
        print("Final failure:", e)
