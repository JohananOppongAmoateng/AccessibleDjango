# AccessibleDjango Documentation

Welcome to **AccessibleDjango**, a Django package designed to help you build accessible web applications that comply with WCAG standards.

```{toctree}
:maxdepth: 2
:caption: Contents

installation
quickstart
user_guide
api/index
contributing
changelog
```

## What is AccessibleDjango?

AccessibleDjango is a Django package that integrates accessibility checks directly into your Django project's development workflow. It uses Django's system check framework to automatically validate your templates for common accessibility issues during development.

### Key Features

- **🔍 Automated Accessibility Checks**: Automatically scans your Django templates for accessibility issues
- **🎯 WCAG Compliance**: Helps ensure your application meets WCAG 2.1 standards
- **⚡ Django Integration**: Seamlessly integrates with Django's system check framework
- **📊 Detailed Reports**: Provides clear, actionable feedback with line numbers and hints
- **🔧 Easy to Use**: Simple installation and minimal configuration required

### Current Capabilities

Version 1.0.0 focuses on image accessibility:
- Detects missing `alt` attributes in `<img>` tags
- Identifies empty `alt` attributes
- Reports exact line numbers for easy fixing

### Future Roadmap

We're actively developing additional accessibility checks:
- Form accessibility validation
- ARIA role verification
- Color contrast analysis
- Heading hierarchy validation
- Keyboard navigation checks
- And much more!

## Quick Links

- [Installation Guide](installation.md) - Get started with AccessibleDjango
- [Quick Start](quickstart.md) - Your first accessibility check in 5 minutes
- [User Guide](user_guide.md) - Comprehensive usage documentation
- [API Reference](api/index.md) - Detailed API documentation
- [Contributing](contributing.md) - Help improve AccessibleDjango
- [GitHub Repository](https://github.com/JohananOppongAmoateng/AccessibleDjango)

## Why Accessibility Matters

Web accessibility ensures that people with disabilities can use your web applications. This includes:
- Visual impairments (blindness, low vision, color blindness)
- Hearing impairments
- Motor impairments
- Cognitive impairments

By integrating accessibility checks into your development workflow, you can catch and fix issues early, making your applications more inclusive for everyone.

## License

AccessibleDjango is released under the MIT License. See the [LICENSE](https://github.com/JohananOppongAmoateng/AccessibleDjango/blob/main/LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/JohananOppongAmoateng/AccessibleDjango/issues)
- **Discussions**: [GitHub Discussions](https://github.com/JohananOppongAmoateng/AccessibleDjango/discussions)
- **Email**: johananoppongamoateng2001@gmail.com
