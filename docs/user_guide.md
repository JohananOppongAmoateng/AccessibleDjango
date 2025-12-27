# User Guide

This comprehensive guide covers all aspects of using AccessibleDjango in your Django projects.

## Overview

AccessibleDjango integrates with Django's system check framework to automatically validate your templates for accessibility issues. It runs during development and can be integrated into your CI/CD pipeline.

## How It Works

### System Check Integration

AccessibleDjango registers custom system checks that run automatically when:

1. You start the development server (`python manage.py runserver`)
2. You run `python manage.py check`
3. You run `python manage.py check --deploy`
4. Django performs system checks before migrations

### Template Scanning

The package scans all HTML templates in:

- Directories specified in `TEMPLATES[]['DIRS']`
- App-specific template directories (when `APP_DIRS=True`)

### Issue Detection

Currently, AccessibleDjango detects:

- Missing `alt` attributes on `<img>` tags
- Empty `alt` attributes on `<img>` tags (when they should have content)

## Running Checks

### Manual Checks

Run accessibility checks manually:

```bash
# Basic check
python manage.py check

# Deployment check (includes all checks)
python manage.py check --deploy

# Check specific apps
python manage.py check myapp

# Show all issues (don't silence any)
python manage.py check --deploy --fail-level WARNING
```

### Automatic Checks

Checks run automatically when starting the development server:

```bash
python manage.py runserver
```

Output will show any accessibility issues before the server starts:

```
Performing system checks...

System check identified some issues:

WARNINGS:
accessible_django.W001: Missing alt attribute in <img> tag at line 42 in /path/to/template.html
    HINT: Add a descriptive 'alt' attribute to all <img> tags.

System check identified 1 issue (0 silenced).
```

## Understanding Check Results

### Warning Format

Each accessibility warning includes:

- **Check ID**: `accessible_django.W001` (for tracking and silencing)
- **Message**: Description of the issue and location
- **Hint**: Suggestion for fixing the issue

Example:

```
accessible_django.W001: Missing alt attribute in <img> tag at line 15 in /path/to/template.html
    HINT: Add a descriptive 'alt' attribute to all <img> tags.
```

### Check IDs

| Check ID | Description |
|----------|-------------|
| `accessible_django.W001` | Missing or empty alt attribute in `<img>` tag |
| `accessible_django.W002` | Template file not found |

## Writing Accessible Alt Text

### General Guidelines

1. **Be Descriptive**: Describe what the image shows
2. **Be Concise**: Keep it under 125 characters when possible
3. **Avoid Redundancy**: Don't start with "Image of" or "Picture of"
4. **Context Matters**: Consider how the image is used

### Examples by Use Case

#### Informative Images

Images that convey information:

```html
<!-- Good -->
<img src="warning.png" alt="Warning: System maintenance scheduled">

<!-- Bad -->
<img src="warning.png" alt="Warning icon">
```

#### Decorative Images

Images that are purely decorative:

```html
<!-- Correct: Empty alt for decorative images -->
<img src="decorative-line.png" alt="">

<!-- Incorrect: Missing alt -->
<img src="decorative-line.png">
```

> [!NOTE]
> Use `alt=""` for decorative images. This tells screen readers to skip the image.

#### Functional Images

Images used as links or buttons:

```html
<!-- Good: Describes the action -->
<a href="/home">
    <img src="home-icon.png" alt="Go to homepage">
</a>

<!-- Bad: Describes the image -->
<a href="/home">
    <img src="home-icon.png" alt="House icon">
</a>
```

#### Complex Images

Charts, graphs, and diagrams:

```html
<!-- Provide a summary in alt, detailed description elsewhere -->
<img src="sales-chart.png" alt="Sales chart showing 30% growth in Q4">
<p>Detailed description: Sales increased from $100K in Q3 to $130K in Q4...</p>
```

#### Text in Images

Avoid text in images, but if necessary:

```html
<!-- Include the text in alt -->
<img src="sale-banner.png" alt="50% Off Sale - This Weekend Only">
```

## Best Practices

### 1. Fix Issues Early

Run checks frequently during development:

```bash
# Add to your development workflow
python manage.py check && python manage.py runserver
```

### 2. Use Pre-commit Hooks

Prevent commits with accessibility issues:

```bash
# .git/hooks/pre-commit
#!/bin/bash
python manage.py check
```

### 3. Integrate with CI/CD

Add to your CI pipeline:

```yaml
# .github/workflows/ci.yml
- name: Accessibility Checks
  run: python manage.py check --deploy --fail-level WARNING
```

### 4. Document Exceptions

If you need to silence a check, document why:

```python
# settings.py
SILENCED_SYSTEM_CHECKS = [
    'accessible_django.W001',  # Silenced because: [reason]
]
```

> [!WARNING]
> Only silence checks when absolutely necessary. Document the reason clearly.

### 5. Team Education

Ensure your team understands accessibility:

- Share this documentation
- Conduct accessibility training
- Review accessibility in code reviews

## Advanced Usage

### Custom Template Directories

If you have templates in non-standard locations, add them to `TEMPLATES`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'custom_templates',  # Custom location
            BASE_DIR / 'third_party' / 'templates',
        ],
        'APP_DIRS': True,
    },
]
```

### Silencing Specific Checks

To silence specific checks:

```python
# settings.py
SILENCED_SYSTEM_CHECKS = [
    'accessible_django.W001',  # Silence alt attribute warnings
]
```

To silence checks for specific apps:

```python
# myapp/apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'
    
    def ready(self):
        # Silence checks for this app only
        from django.core.checks import registry
        registry.unregister('accessible_django.W001')
```

### Programmatic Access

You can run checks programmatically:

```python
from django.core.checks import run_checks

# Run all checks
issues = run_checks()

# Run only accessibility checks
issues = run_checks(tags=['accessibility'])

# Process issues
for issue in issues:
    print(f"{issue.id}: {issue.msg}")
```

## Troubleshooting

### Checks Not Running

**Problem**: Accessibility checks don't appear when running `python manage.py check`

**Solutions**:
1. Verify `accessible_django` is in `INSTALLED_APPS`
2. Check that the app is loaded: `python manage.py shell -c "import accessible_django"`
3. Ensure templates exist in configured directories

### False Positives

**Problem**: Warnings for decorative images with `alt=""`

**Solution**: Empty alt attributes are correct for decorative images. This is not a false positive - the current version flags all missing/empty alt attributes. Future versions will distinguish between decorative and informative images.

### Performance Issues

**Problem**: Checks take too long with many templates

**Solutions**:
1. Limit template directories in `TEMPLATES['DIRS']`
2. Exclude third-party templates
3. Run checks only in development (not in production)

### Template Not Found Errors

**Problem**: `accessible_django.W002: Template could not be found`

**Solutions**:
1. Verify template paths in `TEMPLATES` settings
2. Check file permissions
3. Ensure templates have `.html` extension

## Migration Guide

### From Manual Testing

If you're currently testing accessibility manually:

1. Install AccessibleDjango
2. Run initial check: `python manage.py check`
3. Fix reported issues
4. Add to CI/CD pipeline
5. Continue with automated checks

### From Other Tools

If you're using other accessibility tools:

- AccessibleDjango complements (not replaces) browser-based tools
- Use AccessibleDjango for template-level checks
- Use browser tools for runtime checks
- Combine both for comprehensive coverage

## Future Features

Upcoming accessibility checks (planned):

- Form label validation
- ARIA role verification
- Heading hierarchy checks
- Color contrast analysis
- Keyboard navigation validation
- Link text validation
- Language attribute checks

## Getting Help

- **Documentation**: You're reading it!
- **Issues**: [GitHub Issues](https://github.com/JohananOppongAmoateng/AccessibleDjango/issues)
- **Discussions**: [GitHub Discussions](https://github.com/JohananOppongAmoateng/AccessibleDjango/discussions)
- **Email**: johananoppongamoateng2001@gmail.com

## Next Steps

- Explore the [API Reference](api/index.md) for technical details
- Learn how to [contribute](contributing.md) to the project
- Check the [changelog](changelog.md) for recent updates
