# AccessibleDjango Development Commands
# https://github.com/casey/just

# Install dependencies with uv
install:
    uv sync

# Run tests with Django test runner
test:
    uv run python runtests.py

# Run tests with coverage
test-cov:
    uv run coverage run runtests.py
    uv run coverage report
    uv run coverage html

# Run linters
lint:
    uv run ruff check src/ tests/
    uv run mypy src/

# Format code
format:
    uv run ruff format src/ tests/
    uv run ruff check --fix src/ tests/

# Build documentation
docs:
    uv run sphinx-build -b html docs docs/_build/html

# Serve documentation locally
docs-serve:
    @echo "Building documentation..."
    uv run sphinx-build -b html docs docs/_build/html
    @echo "Documentation built in docs/_build/html"
    @echo "Open docs/_build/html/index.html in your browser"

# Clean build artifacts
clean:
    -rm -rf dist/ build/ *.egg-info .pytest_cache .coverage htmlcov/ docs/_build/
    -find . -type d -name __pycache__ -exec rm -rf {} +
    -find . -type f -name "*.pyc" -delete

# Build distribution packages
build: clean
    uv build

# Update uv.lock file
lock:
    uv lock

# Show available commands
help:
    @just --list
