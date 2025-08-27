import json

def load_resume(filepath: str) -> dict:
    """
    Loads a resume from a JSON file.

    Args:
        filepath: The path to the resume JSON file.

    Returns:
        A dictionary containing the resume data.
    """
    with open(filepath, 'r') as f:
        return json.load(f)
