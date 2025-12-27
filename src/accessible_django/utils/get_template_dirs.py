import os
from django.conf import settings
from django.template.utils import get_app_template_dirs

def get_template_dirs():
    """
    Retrieve all template directories including those explicitly defined in settings
    and app-specific template directories.
    """
    template_dirs = []

    # Include explicitly defined template directories
    for template_engine in settings.TEMPLATES:
        template_dirs.extend(template_engine.get("DIRS", []))

    # Include app-specific template directories
    template_dirs.extend(get_app_template_dirs('templates'))

    return list(set(template_dirs))  # Remove duplicates if any



def get_template_files():
    """
    Collect all template files from the configured directories.
    """
    template_dirs = get_template_dirs()
    template_files = []
    for directory in template_dirs:
        for root, _, files in os.walk(directory):
            template_files.extend(os.path.join(root, file) for file in files if file.endswith(".html"))
    return template_files
