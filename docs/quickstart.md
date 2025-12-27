# Quick Start Guide

Get started with AccessibleDjango in just a few minutes!

## Installation

First, install AccessibleDjango:

```bash
pip install accessible-django
```

Add it to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps
    'accessible_django',
]
```

## Your First Accessibility Check

### 1. Create a Template with Issues

Let's create a template with some accessibility issues to see AccessibleDjango in action.

Create `templates/example.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example Page</title>
</head>
<body>
    <h1>Welcome to My Site</h1>
    
    <!-- This image is missing an alt attribute -->
    <img src="/static/logo.png">
    
    <!-- This image has an empty alt attribute -->
    <img src="/static/banner.png" alt="">
    
    <!-- This image is correct -->
    <img src="/static/photo.png" alt="A beautiful sunset over the ocean">
</body>
</html>
```

### 2. Run the Accessibility Check

Run Django's system check:

```bash
python manage.py check
```

You should see output like:

```
System check identified some issues:

WARNINGS:
accessible_django.W001: Missing alt attribute in <img> tag at line 11 in /path/to/templates/example.html
    HINT: Add a descriptive 'alt' attribute to all <img> tags.
accessible_django.W001: Missing alt attribute in <img> tag at line 14 in /path/to/templates/example.html
    HINT: Add a descriptive 'alt' attribute to all <img> tags.

System check identified 2 issues (0 silenced).
```

### 3. Fix the Issues

Update your template to fix the accessibility issues:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example Page</title>
</head>
<body>
    <h1>Welcome to My Site</h1>
    
    <!-- Fixed: Added descriptive alt text -->
    <img src="/static/logo.png" alt="Company Logo">
    
    <!-- Fixed: Added descriptive alt text -->
    <img src="/static/banner.png" alt="Welcome banner with company slogan">
    
    <!-- Already correct -->
    <img src="/static/photo.png" alt="A beautiful sunset over the ocean">
</body>
</html>
```

### 4. Verify the Fixes

Run the check again:

```bash
python manage.py check
```

You should now see:

```
System check identified no issues (0 silenced).
```

🎉 Congratulations! Your template is now more accessible!

## Integration with Development Workflow

### During Development

AccessibleDjango checks run automatically when you start the development server:

```bash
python manage.py runserver
```

Any accessibility issues will be displayed in the console before the server starts.

### In CI/CD Pipelines

Add accessibility checks to your CI/CD pipeline:

```yaml
# .github/workflows/ci.yml
- name: Run Django Checks
  run: |
    python manage.py check --deploy
```

### Pre-commit Hooks

You can also run checks as a pre-commit hook. Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python manage.py check
if [ $? -ne 0 ]; then
    echo "Accessibility checks failed. Please fix the issues before committing."
    exit 1
fi
```

Make it executable:

```bash
chmod +x .git/hooks/pre-commit
```

## Understanding Alt Text

### When to Use Alt Text

Alt text should describe the content and function of an image:

```html
<!-- Good: Describes the content -->
<img src="chart.png" alt="Bar chart showing sales increased 25% in Q4">

<!-- Bad: Too vague -->
<img src="chart.png" alt="Chart">

<!-- Bad: Redundant -->
<img src="chart.png" alt="Image of a chart">
```

### Decorative Images

For purely decorative images, use an empty alt attribute:

```html
<!-- Decorative image that adds no information -->
<img src="decorative-border.png" alt="">
```

> [!NOTE]
> An empty `alt=""` is different from a missing alt attribute. Empty alt tells screen readers to skip the image, which is appropriate for decorative images.

### Functional Images

For images that are links or buttons, describe the action:

```html
<!-- Good: Describes the action -->
<a href="/search">
    <img src="search-icon.png" alt="Search">
</a>

<!-- Bad: Describes the image -->
<a href="/search">
    <img src="search-icon.png" alt="Magnifying glass icon">
</a>
```

## Common Patterns

### Logo Images

```html
<img src="logo.png" alt="Acme Corporation">
```

### Product Images

```html
<img src="product.jpg" alt="Red leather wallet with gold clasp">
```

### Avatar Images

```html
<img src="avatar.jpg" alt="Profile photo of John Doe">
```

### Charts and Graphs

```html
<img src="chart.png" alt="Line graph showing temperature increase from 20°C to 35°C over 7 days">
```

## Next Steps

- Read the [User Guide](user_guide.md) for comprehensive documentation
- Check the [API Reference](api/index.md) for technical details
- Learn about [Contributing](contributing.md) to AccessibleDjango

## Getting Help

If you encounter any issues:

1. Check the [Troubleshooting](installation.md#troubleshooting) section
2. Search [existing issues](https://github.com/JohananOppongAmoateng/AccessibleDjango/issues)
3. Open a [new issue](https://github.com/JohananOppongAmoateng/AccessibleDjango/issues/new) if needed
