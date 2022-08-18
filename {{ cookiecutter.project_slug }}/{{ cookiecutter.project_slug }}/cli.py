"""Commandline interface."""
import typing as t
from pathlib import Path

import typer



app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="""{{ cookiecutter.project_slug }} commandline tool for pre-processing data.""",
)


@app.command()
def clean(
    input_files: list[Path] = typer.Argument(None, help="Raw data file to clean."),
    output_directory: t.Optional[Path] = typer.Option(Path.cwd(), help="Directory to write the pre-processed data."),    
):
    """Clean input data with the defined ``clean`` function."""

    from .clean import clean
    
    clean(input_files, output_directory)

if __name__ == '__main__':
    app()