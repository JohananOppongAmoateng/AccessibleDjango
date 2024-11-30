# AccessibleDjango Roadmap

This is the roadmap for the AccessibleDjango project, detailing the current features, planned improvements, and future enhancements.

---

## 🎯 Current Features (v1.0.0)

AccessibleDjango focuses on making web applications more accessible by checking for compliance with accessibility standards. The first version primarily checks for missing or empty `alt` attributes in `<img>` tags.

- **Accessibility Checks for `alt` in `<img>` Tags**:  
  Ensures that all `<img>` tags in your Django templates contain valid `alt` attributes for accessibility.

---

## 🔜 Planned Features

### 1. **Prebuilt Accessible Templates**
   - **Goal**: Provide ready-to-use Django templates that comply with WCAG 2.1 standards.
   - **Benefit**: Enables developers to quickly build accessible applications without needing to manually create compliant templates.

### 2. **Enhanced Form Generation Tools**
   - **Goal**: Assist in generating accessible forms that comply with best practices for labels, structure, and ARIA roles.
   - **Benefit**: Simplifies the creation of accessible forms, ensuring they are usable by individuals with disabilities.

### 3. **Real-Time Accessibility Validation**
   - **Goal**: Implement live accessibility validation while developers are building their applications.
   - **Benefit**: Instant feedback on accessibility issues during development to improve the quality of your app’s accessibility.

### 4. **Comprehensive Accessibility Checks**
   - **Goal**: Expand the accessibility checks to include:
     - ARIA roles and attributes validation.
     - Color contrast checks.
     - Heading structure and hierarchy validation.
     - Form validation for labels, inputs, and error handling.
   - **Benefit**: A more thorough accessibility auditing system covering a broader range of accessibility concerns.

---

## 🛠️ Ongoing Improvements

- **Performance Optimization**:  
  Enhance the performance of the accessibility checks to handle larger projects and more complex templates efficiently.

- **Expanded Reporting Features**:  
  Provide additional reporting options such as HTML reports, more detailed error logs, and integration with CI/CD tools.

- **Internationalization Support**:  
  Introduce support for multiple languages, allowing the accessibility checks and reports to be available in various languages.

---

## 📅 Timeline

- **Q1 2025**: Focus on expanding accessibility checks to cover more areas (e.g., ARIA, color contrast, etc.) and prebuilt accessible templates.
- **Q2 2025**: Begin implementing real-time validation and accessibility feedback tools during development.
- **Q3 2025**: Further optimizations for performance and scalability, and integration with CI/CD pipelines.

For more information, feel free to reach out via our [GitHub Issues](https://github.com/JohananOppongAmoateng/AccessibleDjango) or [discussions](https://github.com/JohananOppongAmoateng/AccessibleDjango/discussions).
