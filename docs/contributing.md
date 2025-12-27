# Contributing to AccessibleDjango

Thank you for your interest in contributing to AccessibleDjango!

This guide is also available in the repository: [CONTRIBUTING.md](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CONTRIBUTING.md)

For detailed contribution guidelines, development setup, and coding standards, please refer to the main contributing guide in the repository.

## Quick Links

- [Development Setup](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CONTRIBUTING.md#development-setup)
- [Running Tests](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CONTRIBUTING.md#running-tests)
- [Code Quality](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CONTRIBUTING.md#code-quality)
- [Pull Request Process](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CONTRIBUTING.md#pull-request-process)

## Overview

We welcome contributions in the form of:

- 🐛 Bug reports
- 💡 Feature requests
- 📝 Documentation improvements
- 🔧 Code contributions
- ✅ Test coverage improvements

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/JohananOppongAmoateng/AccessibleDjango.git
cd AccessibleDjango

# Install dependencies
uv sync

# Run tests
just test

# Check code quality
just lint
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Write clean, readable code
- Add tests for new functionality
- Update documentation as needed

### 3. Run Quality Checks

```bash
# Format code
just format

# Lint code
just lint

# Run tests
just test

# Build docs
just docs
```

### 4. Submit Pull Request

- Push your branch to GitHub
- Create a pull request
- Ensure CI checks pass
- Respond to review feedback

## Code Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write descriptive commit messages
- Add docstrings to all public functions
- Keep line length to 100 characters

## Testing

All new features should include tests:

```bash
# Run all tests
just test

# Run with coverage
just test-cov

# Run specific test
uv run python runtests.py tests.test_img
```

## Documentation

Update documentation for any user-facing changes:

```bash
# Build documentation
just docs

# View documentation
# Open docs/_build/html/index.html in your browser
```

## Questions?

- Open an [issue](https://github.com/JohananOppongAmoateng/AccessibleDjango/issues)
- Start a [discussion](https://github.com/JohananOppongAmoateng/AccessibleDjango/discussions)
- Email: johananoppongamoateng2001@gmail.com

Thank you for contributing! 🎉
