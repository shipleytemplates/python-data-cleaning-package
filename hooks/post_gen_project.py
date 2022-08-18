# type: ignore
"""Post project generation script"""

import sys


functions = []


def register(func):
    functions.append(func)
    return func


def run_all():
    for func in functions:
        func()
    sys.exit(0)


if __name__ == "__main__":
    run_all()
