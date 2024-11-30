# AccessibleDjango 🌟  

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.0.1-green.svg)](https://github.com/Area-25/webrover/releases)

AccessibleDjango is a Django package focused on checking your web applications for accessibility compliance. It ensures your app adheres to accessibility standards, making your web interfaces usable for everyone, including individuals with disabilities. AccessibleDjango currently checks for missing or empty `alt` attributes in `<img>` tags, with plans for further accessibility features in future releases.

---

## 🌟 Features  

- **Accessibility Checks**:  
  Automatically evaluates views and templates for common accessibility issues, such as missing or empty `alt` attributes in `<img>` tags.  

- **Detailed Reports**:  
  Generates comprehensive accessibility reports highlighting issues found in your templates and views.  

- **Developer-Friendly Tools**:  
  Easily integrate AccessibleDjango into your project and CI pipelines.  

- **Customizable Rules**:  
  Tailor the accessibility checks to suit your application’s needs, including enabling/disabling checks for specific issues.  

---

## ⚠️ Important Notes  

AccessibleDjango currently focuses exclusively on checking `alt` attributes for `<img>` tags. Future releases may include features such as:  
- Prebuilt accessible templates.  
- Enhanced form generation tools.  
- Real-time accessibility validation in the development environment.  

---

## 🚀 Quick Start  

### Installation  

To install AccessibleDjango, run:  
```bash  
pip install accessible-django  
```  

### Basic Usage  

#### Add to Installed Apps  
In your `settings.py`, add `'accessible_django'` to the `INSTALLED_APPS` list:  
```python  
INSTALLED_APPS = [  
    ...,  
    'accessible_django',  
]  
```  

#### Run Accessibility Checks  
Run the following command to check for accessibility issues in your templates:  
```bash  
python manage.py check_accessibility  
```  

---

## 📖 Documentation  

### Running Checks  

AccessibleDjango evaluates templates and views for common accessibility pitfalls, including:  
- Missing or empty `alt` attributes in `<img>` tags.  
- Poor color contrast.  
- Missing or incorrect ARIA attributes.  
- Improper heading structure.  
- Missing labels for form inputs.  

Run the command to generate a report:  
```bash  
python manage.py check_accessibility --output=report.json  
```  

### 📊 Output Files  

- **`accessibility_report.json`**: A structured JSON report detailing the accessibility issues found.  
- **`error_summary.log`**: A simplified log highlighting critical issues and warnings.  

---

## 🚧 Limitations  

- AccessibleDjango currently focuses only on identifying accessibility issues related to `alt` attributes in `<img>` tags.  
- It does not yet provide prebuilt accessible templates, form enhancements, or real-time validation in development.  
- Manual testing may be required for third-party components.  

---

## 🗺️ Roadmap  

We are actively working to expand AccessibleDjango to include additional accessibility features. Future releases may include:  

1. **Prebuilt Accessible Templates**: Ready-to-use templates that adhere to WCAG 2.1 standards.  
2. **Enhanced Form Generation Tools**: Tools for generating accessible forms and validating form input accessibility.  
3. **Real-Time Accessibility Validation**: A live testing mode to validate accessibility as you develop.  
4. **Comprehensive Accessibility Checks**: Full support for various accessibility issues, such as ARIA roles, color contrast, form validation, and more.  

For more details, see `ROADMAP.md`.  

---

## 🤝 Contributing  

We welcome contributions to AccessibleDjango! Please feel free to submit a Pull Request or open an issue on GitHub.  

---

## 📜 License  

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

## 🙏 Acknowledgments  

Built with ❤️ by the Accessible Django Team. Special thanks to all contributors and the accessibility community for their support.  

---

AccessibleDjango: Ensuring web applications are inclusive for everyone. 💡  
``` 
