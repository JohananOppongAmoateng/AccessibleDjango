# Changelog

All notable changes to AccessibleDjango are documented here.

This page references the main changelog: [CHANGELOG.md](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CHANGELOG.md)

## Version History

### [1.0.0] - 2024-12-25

**Initial Release** 🎉

#### Added
- Accessibility checks for missing or empty `alt` attributes in `<img>` tags
- Django system checks integration
- Template scanning for all configured template directories
- Basic validators and utilities for template processing
- Comprehensive documentation with Sphinx
- MIT License
- Support for Python 3.10+
- Support for Django 4.2+

#### Features
- Automatic template discovery from `TEMPLATES` settings
- Line number reporting for accessibility issues
- Integration with Django's check framework
- Clear, actionable warning messages with hints

#### Documentation
- Installation guide
- Quick start tutorial
- Comprehensive user guide
- Complete API reference
- Contributing guidelines

## Upgrade Guide

### Upgrading to 1.0.0

This is the initial release. To install:

```bash
pip install accessible-django
```

Add to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'accessible_django',
]
```

## Future Releases

See our [roadmap](index.md#future-roadmap) for planned features:

- Form accessibility validation
- ARIA role verification
- Color contrast analysis
- Heading hierarchy validation
- Keyboard navigation checks

## Release Notes Format

We follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format:

- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security fixes

## Versioning

AccessibleDjango follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality (backwards compatible)
- **PATCH** version for backwards compatible bug fixes

## Stay Updated

- Watch the [GitHub repository](https://github.com/JohananOppongAmoateng/AccessibleDjango) for releases
- Check the [changelog](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CHANGELOG.md) regularly
- Subscribe to release notifications on GitHub

## Links

- [Full Changelog](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/CHANGELOG.md)
- [Releases](https://github.com/JohananOppongAmoateng/AccessibleDjango/releases)
- [GitHub Repository](https://github.com/JohananOppongAmoateng/AccessibleDjango)
