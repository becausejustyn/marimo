# marimo
Testing out marimo

```bash
uv venv
.venv\Scripts\activate
uv pip install

uv pip install . # this uses the pyproject.toml
```

```bash
marimo edit

ruff check .
# ruff check my_notebook.py

# Auto-fixing (many issues):
ruff check . --fix

# Formatting your code:
ruff format .
```