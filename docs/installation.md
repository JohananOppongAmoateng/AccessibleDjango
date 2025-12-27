# Installation

This guide will help you install and configure AccessibleDjango in your Django project.

## Requirements

- Python 3.10 or higher
- Django 4.2 or higher

## Installation Methods

### Using pip

The simplest way to install AccessibleDjango is via pip:

```bash
pip install accessible-django
```

### Using uv (Recommended for Development)

If you're using [uv](https://github.com/astral-sh/uv) for package management:

```bash
uv add accessible-django
```

### From Source

To install the latest development version from GitHub:

```bash
pip install git+https://github.com/JohananOppongAmoateng/AccessibleDjango.git
```

## Configuration

### 1. Add to Installed Apps

After installation, add `accessible_django` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps
    'myapp',
    
    # Third-party apps
    'accessible_django',  # Add this line
]
```

> [!IMPORTANT]
> Make sure to add `accessible_django` to `INSTALLED_APPS`. The package registers its checks automatically when Django starts.

### 2. Verify Installation

To verify that AccessibleDjango is installed correctly, run:

```bash
python manage.py check
```

If there are any accessibility issues in your templates, you'll see warnings like:

```
System check identified some issues:

WARNINGS:
accessible_django.W001: Missing alt attribute in <img> tag at line 15 in /path/to/template.html
    HINT: Add a descriptive 'alt' attribute to all <img> tags.
```

## Optional Configuration

### Template Directories

AccessibleDjango automatically scans all template directories configured in your `TEMPLATES` setting:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # These will be scanned
        ],
        'APP_DIRS': True,  # App templates will also be scanned
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Development vs Production

You may want to run accessibility checks only in development:

```python
# settings.py
if DEBUG:
    INSTALLED_APPS += ['accessible_django']
```

However, we recommend keeping it enabled in all environments to catch issues early.

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade accessible-django
```

Or with uv:

```bash
uv add --upgrade accessible-django
```

## Troubleshooting

### Check Not Running

If the accessibility checks aren't running:

1. Verify `accessible_django` is in `INSTALLED_APPS`
2. Make sure you're running `python manage.py check` or starting the development server
3. Check that your templates are in directories configured in `TEMPLATES`

### Import Errors

If you encounter import errors:

1. Ensure Django 4.2+ is installed: `pip install "Django>=4.2"`
2. Verify Python version: `python --version` (should be 3.10+)
3. Try reinstalling: `pip uninstall accessible-django && pip install accessible-django`

## Next Steps

Now that you have AccessibleDjango installed, check out the [Quick Start Guide](quickstart.md) to learn how to use it effectively.
