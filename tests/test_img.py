import os
import tempfile
from django.test import SimpleTestCase

from accessible_django.validators.img_tag import (
    check_img_alt,
    run_img_alt_check,
    validate_template
)

class TestImgAltChecks(SimpleTestCase):
    def setUp(self):
        # Create a temporary directory for test templates
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Clean up any files created during the test
        for file in os.listdir(self.test_dir):
            os.unlink(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def _create_test_template(self, filename, content):
        """Helper method to create a template file for testing"""
        filepath = os.path.join(self.test_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filepath

    def test_img_tag_with_alt(self):
        """Test that an <img> tag with alt attribute passes"""
        filepath = self._create_test_template('valid_template.html',
                                              '<img src="test.jpg" alt="Valid description">'
                                              )

        warnings = check_img_alt(filepath)
        self.assertEqual(len(warnings), 0, "No warnings should be generated for img with alt")

    def test_img_tag_without_alt(self):
        """Test that an <img> tag without alt attribute generates a warning"""
        filepath = self._create_test_template('missing_alt_template.html',
                                              '<img src="test.jpg">'
                                              )

        warnings = check_img_alt(filepath)
        self.assertEqual(len(warnings), 1, "A warning should be generated")
        self.assertEqual(warnings[0].id, 'accessible_django.W001')

    def test_multiple_img_tags(self):
        """Test multiple img tags with mixed alt attribute presence"""
        filepath = self._create_test_template('mixed_alt_template.html',
                                              '''
                                              <img src="test1.jpg" alt="Description 1">
                                              <img src="test2.jpg">
                                              <img src="test3.jpg" alt="Description 3">
                                              '''
                                              )

        warnings = check_img_alt(filepath)
        self.assertEqual(len(warnings), 1, "Only one warning should be generated")

    def test_validate_template_success(self):
        """Test the validate_template function with a successful check"""
        filepath = self._create_test_template('success_template.html',
                                              '<img src="test.jpg" alt="Description">'
                                              )

        def mock_check(file_path):
            return []

        issues = validate_template(filepath, mock_check)
        self.assertEqual(len(issues), 0, "No issues should be returned")

    def test_validate_template_exception(self):
        """Test validate_template handles exceptions"""
        filepath = self._create_test_template('exception_template.html',
                                              '<img src="test.jpg">'
                                              )

        def mock_check(file_path):
            raise Exception("Test exception")

        issues = validate_template(filepath, mock_check)
        self.assertEqual(len(issues), 1, "An error issue should be returned")
        self.assertTrue("Error processing" in issues[0])

    def test_run_img_alt_check(self):
        """Test the run_img_alt_check wrapper function"""
        filepath = self._create_test_template('run_check_template.html',
                                              '<img src="test.jpg">'
                                              )

        issues = run_img_alt_check(filepath)
        self.assertEqual(len(issues), 1, "One issue should be returned")

    def test_empty_template(self):
        """Test an empty template"""
        filepath = self._create_test_template('empty_template.html', '')

        warnings = check_img_alt(filepath)
        self.assertEqual(len(warnings), 0, "No warnings for empty template")

    def test_complex_html_structure(self):
        """Test img tags within complex HTML structure"""
        filepath = self._create_test_template('complex_template.html',
                                              '''
                                              <div>
                                                  <section>
                                                      <img src="test1.jpg">
                                                      <p>Some text</p>
                                                      <img src="test2.jpg" alt="Description">
                                                  </section>
                                              </div>
                                              '''
                                              )

        warnings = check_img_alt(filepath)
        self.assertEqual(len(warnings), 1, "One warning should be generated")

    def test_non_existent_file(self):
        """Test behavior with a non-existent file"""
        non_existent_path = os.path.join(self.test_dir, 'non_existent.html')

        with self.assertRaises(FileNotFoundError):
            check_img_alt(non_existent_path)