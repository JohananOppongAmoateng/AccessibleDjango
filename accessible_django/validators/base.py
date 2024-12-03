def validate_template(file_path, check_function):
    """
    Run a provided check function on a template file.
    """
    issues = []
    try:
        issues = check_function(file_path)
    except Exception as e:
        issues.append(f"Error processing {file_path}: {str(e)}")
    return issues
