# accessible_django/validators/img_tag.py
from bs4 import BeautifulSoup
from django.core.checks import Warning
from  django.template.exceptions import TemplateDoesNotExist
from .base import validate_template

def check_img_alt(file_path):
    """
    Check if all <img> tags in the template have 'alt' attributes.
    Includes line number for each error.
    """
    warnings = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            for img_tag in soup.find_all("img"):
                if not img_tag.get("alt"):
                    line_number = img_tag.sourceline
                    warnings.append(Warning(
                        f'Missing alt attribute in <img> tag at line {line_number} in {file_path}',
                        hint="Add a descriptive 'alt' attribute to all <img> tags.",
                        id='accessible_django.W001',
                    ))

    except TemplateDoesNotExist:

        warnings.append(

            Warning(

                "Template 'base.html' could not be found.",

                hint="Ensure the template exists in your templates directory.",

                id='accessible_django.W002',

            )

    )
    return warnings

def run_img_alt_check(file_path):
    return validate_template(file_path, check_img_alt)
