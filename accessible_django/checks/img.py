from accessible_django.utils.get_template_dirs import (get_template_files)
from accessible_django.validators.img_tag import run_img_alt_check


def check_img_alt(app_configs, **kwargs):
    """
    Custom Django system check to validate <img> tags in templates for alt attributes.
    """
    errors = []
    template_files = get_template_files()

    for file_path in template_files:
        errors.append(run_img_alt_check(file_path))
    return  errors