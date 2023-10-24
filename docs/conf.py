"""Sphinx configuration."""
project = "cookiecutter-django-package-instance"
author = "Jack Linke"
copyright = "2023, Jack Linke"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
