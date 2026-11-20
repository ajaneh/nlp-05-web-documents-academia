# Project 05: arXiv Web Documents

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

- **Author:** Alex Heyert
- **Date:** November 2026

## Project Overview

This project requests an arXiv page and processes its contents
using a Python ETVL pipeline.

## Run the Project

From the project root, run the pipeline:

```shell
uv run python -m nlp_custom.pipeline_web_html
```

## Verification

Run the automated tests:

```shell
uv run python -m pytest
```

## Project Documentation

The [hosted documentation site](https://ajaneh.github.io/nlp-05-web-documents-academia/)
contains the project report and supporting materials.

## CI/CD and GitHub Actions

GitHub Actions run [Python and documentation checks](https://github.com/ajaneh/nlp-05-web-documents-academia/actions/workflows/ci-python-zensical.yml)
and [deploy the documentation](https://github.com/ajaneh/nlp-05-web-documents-academia/actions/workflows/deploy-zensical.yml).

## Developer Reference

Follow the
[Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
for **detailed instructions and troubleshooting**.

### Initialize and Update the Python Environment

With the project open in VS Code, open a VS Code terminal.
Paste each command and hit Enter or Return after to run it.

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the git hooks to perform
basic checks automatically before
any changes get pushed to GitHub.

In the VS Code terminal,
paste each command and hit Enter or Return after to run it.

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
# repeat if changes were made
uvx prek run --all-files
```

### Run Common Chores

Run linters, formatters, type checks, tests, and
build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Developer Tools

This project uses professional Python tools to support development,
testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [Hosted Documentation](https://ajaneh.github.io/nlp-05-web-documents-academia/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
