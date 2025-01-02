def check_security_risks(project_name):
    """
    Perform basic security checks on a project.
    
    Args:
        project_name (str): The name of the project to analyze.
    
    Returns:
        str: The result of the security check.
    """
    # Example check (expand with more complex checks as needed)
    if "malicious" in project_name:
        return "This project has potential security risks!"
    else:
        return "No immediate security risks detected."
