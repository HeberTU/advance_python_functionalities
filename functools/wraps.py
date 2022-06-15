# -*- coding: utf-8 -*-
"""wraps function case study.

Created on: 15/6/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from typing import Callable
from functools import wraps


def regular_decorator(func: Callable) -> Callable:
    """This is a regular decorator example.

    Args:
        func: Function to b e decorated.

    Returns:
        wrapper: Decorated function.
    """
    def wrapper(*args, **kwargs):
        """A wrapper function"""

        func()
    return wrapper


@regular_decorator
def first_function() -> None:
    """This is the first function docstring."""
    print("First Function.")


def wrap_decorator(func: Callable) -> Callable:
    """This is a decorator using the wrap functionality example.

    Args:
        func: Function to b e decorated.

    Returns:
        wrapper: Decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function"""

        func()
    return wrapper

@wrap_decorator
def second_function() -> None:
    """This is the second function docstring."""
    print("Second Function.")


print("***************** Regular Decorator *****************")
print(f"First function name: {first_function.__name__}")
print(f"First function Docstring: {first_function.__doc__}")
help(first_function)

print("***************** Wrap Decorator *****************")
print(f"Second function name: {second_function.__name__}")
print(f"Second function Docstring: {second_function.__doc__}")
help(second_function)
