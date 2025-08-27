import unittest
import os
import json
import sys

# Add the src directory to the Python path to allow importing resume_parser
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

from resume_parser import load_resume

class TestResumeParser(unittest.TestCase):

    def test_load_resume(self):
        """
        Tests that the resume file is loaded correctly.
        """
        # Construct path to the resume file
        resume_path = os.path.join(project_root, 'data', 'resume.json')

        # Load the resume data using the function we are testing
        parsed_data = load_resume(resume_path)

        # Load the raw JSON data to compare against
        with open(resume_path, 'r') as f:
            expected_data = json.load(f)

        # Assert that the parsed data is equal to the expected data
        self.assertEqual(parsed_data, expected_data)

        # Also check for a specific value to be more explicit
        self.assertEqual(parsed_data['personal_info']['email'], 'jules.doe@email.com')

if __name__ == '__main__':
    unittest.main()
