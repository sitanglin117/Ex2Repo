# Reproducible Research – Environment Demo

A minimal Python project demonstrating reproducible environments with **uv**.  
It loads a small dataset with **pandas** and fetches live weather data with **requests**.

## Requirements

| Tool | Version |
|------|---------|
| Python | 3.12+ |
| uv | latest |

Install `uv` (if not already):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# or on macOS
brew install uv
```

## Reproduce the environment

```bash
git clone https://github.com/<your-username>/repro-project.git
cd repro-project
uv sync          # installs exact versions from uv.lock
```

> **Never commit `.venv/`** – it is listed in `.gitignore`.  
> `uv sync` re-creates it from `uv.lock` on any machine.

## Run the script

```bash
uv run main.py
```

## Run tests

```bash
uv run pytest
```

## Project structure

```
repro-project/
├── main.py            # main script
├── tests/
│   └── test_main.py   # unit tests
├── pyproject.toml     # project metadata & dependencies
├── uv.lock            # pinned dependency tree (commit this!)
├── .python-version    # pinned Python version
├── .gitignore
└── README.md
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `pandas` | DataFrame creation and summary statistics |
| `requests` | HTTP calls to a public weather API |
| `pytest` *(dev)* | Unit testing |

## Exporting for non-uv users

```bash
uv export --format requirements-txt > requirements.txt
pip install -r requirements.txt
python main.py
```

## Environment management cheat-sheet

```bash
uv add <package>          # add a dependency
uv remove <package>       # remove a dependency
uv sync                   # sync venv to lockfile
uv sync --frozen          # fail if lockfile is outdated (great for CI)
uv run <script>           # run without manual venv activation
```
