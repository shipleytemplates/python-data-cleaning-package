# type: ignore
"""Pre project generation script"""

import re
import sys


functions = []


def register(func):
    functions.append(func)
    return func


def run_all():
    for func in functions:
        func()
    sys.exit(0)


@register
def check_project_slug():
    """
    Check that the project_slug is composed of letters, numbers, or underscores
    and starts with either an underscore or a letter.
    """
    project_slug = "{{ cookiecutter.project_slug }}"
    if not re.match(r"^[_a-zA-Z][_a-zA-Z0-9]+$", project_slug):
        print(f"ERROR: {project_slug} is not a valid Python module name!")
        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == "__main__":
    run_all()
