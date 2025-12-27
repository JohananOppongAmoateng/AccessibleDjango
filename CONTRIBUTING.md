# Contributing to AccessibleDjango

Thank you for your interest in contributing to AccessibleDjango! This document provides guidelines and instructions for contributing to the project.

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JohananOppongAmoateng/AccessibleDjango.git
   cd AccessibleDjango
   ```

2. **Install uv** (if not already installed)
   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   pip install uv
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
just test

# Or directly with Django
uv run python runtests.py

# Run with coverage
just test-cov
```

### Code Quality

We use `ruff` for linting and formatting:

```bash
# Check code style
just lint

# Format code
just format

# Type checking
uv run mypy src/
```

### Building Documentation

```bash
# Build documentation
just docs

# Serve documentation locally
just docs-serve
# Then open docs/_build/html/index.html in your browser
```

## Coding Standards

- Follow PEP 8 style guidelines (enforced by ruff)
- Write descriptive commit messages
- Add docstrings to all public functions and classes
- Include type hints where appropriate
- Write tests for new features and bug fixes
- Keep line length to 100 characters

## Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Add tests for new functionality
   - Update documentation as needed

3. **Run quality checks**
   ```bash
   make lint
   make test
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Provide a clear description of the changes
   - Reference any related issues
   - Ensure all CI checks pass

## Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

## Reporting Issues

When reporting issues, please include:

- Python version
- Django version
- AccessibleDjango version
- Steps to reproduce the issue
- Expected vs actual behavior
- Any relevant error messages or logs

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## Questions?

Feel free to open an issue for any questions or concerns about contributing.

Thank you for contributing to AccessibleDjango! 🎉
