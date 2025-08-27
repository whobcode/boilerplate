import asyncio
import os
from resume_parser import load_resume
from web_agent import WebAgent

async def main():
    """
    Main function to run the agent.
    """
    # Construct absolute paths to data files to ensure the script can be run from anywhere.
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resume_path = os.path.join(project_root, 'data', 'resume.json')
    form_path = os.path.join(project_root, 'data', 'test_form.html')

    # Load resume data
    resume_data = load_resume(resume_path)
    email = resume_data.get("personal_info", {}).get("email")
    # Get a sample message from the first work experience
    message = ""
    work_experience = resume_data.get("work_experience", [])
    if work_experience:
        responsibilities = work_experience[0].get("responsibilities", [])
        if responsibilities:
            message = responsibilities[0]

    if not email:
        print("Email not found in resume.json")
        return

    # Initialize and run the web agent
    agent = WebAgent()
    try:
        await agent.start()

        # Navigate to the local form using the file:// protocol
        form_url = f"file://{form_path}"
        await agent.navigate(form_url)

        # Fill the form fields
        await agent.fill_field("#email", email)
        await agent.fill_field("#message", message)

        # Take a screenshot to verify the result
        screenshot_path = os.path.join(project_root, 'filled_form.png')
        await agent.take_screenshot(screenshot_path)
        print(f"Screenshot of the filled form saved to {screenshot_path}")

    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
