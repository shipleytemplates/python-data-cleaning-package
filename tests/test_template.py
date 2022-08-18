import json
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter  # type: ignore

TEMPLATE_DIRECTORY = Path(__file__).parent.parent
TEST_CONTEXT = {
    "project_name": "Test Project",
    "project_slug": "test_project",
    "full_name": "Garrett Shipley",
    "email": "myemail@email.com",
    "description": "Some words about this project.",
}


def get_paths(directory: Path):
    """Get all the paths from the directory."""
    jinja_var = "{{ cookiecutter.project_slug }}"
    paths = [path.relative_to(directory) for path in directory.rglob("*")]
    return {str(path).replace(jinja_var, TEST_CONTEXT["project_slug"]) for path in paths}


def run_cookiecutter_and_check_paths(tmpdir: Path, context: dict[str, str]):
    cookiecutter(
        template=str(TEMPLATE_DIRECTORY),
        output_dir=str(tmpdir),
        no_input=True,
        extra_context=context,
    )
    true_paths = get_paths(TEMPLATE_DIRECTORY.joinpath("{{ cookiecutter.project_slug }}"))
    test_paths = get_paths(tmpdir.joinpath(context["project_slug"]))
    assert true_paths == test_paths


def test_cookiecutter_json():
    file = TEMPLATE_DIRECTORY.joinpath("cookiecutter.json")
    data = json.loads(file.read_text())
    assert sorted(TEST_CONTEXT) == sorted(data)


def test_cookiecutter_template_runs(tmpdir: Path):
    run_cookiecutter_and_check_paths(Path(tmpdir), TEST_CONTEXT)


def test_pre_hooks(tmpdir: Path):
    context = dict(TEST_CONTEXT)
    context["project_slug"] = "????"
    with pytest.raises(FailedHookException):
        run_cookiecutter_and_check_paths(Path(tmpdir), context)
