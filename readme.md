# Run locally
flask run

# Run the tests locally
pytest

# Explanation of the Code

- Flask Application: The Flask app handles the web server, routes, and rendering of HTML templates.
- File Upload and Text Processing: The `/upload`` route processes the uploaded text or file, creates a PPTX file, and either sends it via email (if an email address is provided) or provides a download link.
- PPTX Creation: The `create_pptx` function uses the `python-pptx` library to create a PowerPoint file with each word on a new line.
- Email Sending: The `send_email` function uses Flask-Mail to send the generated PPTX file to the provided email address.
- HTML Templates: The HTML templates provide a user interface for uploading text or files and downloading the generated PPTX file.
- Environment Variables: Sensitive information is stored in environment variables, which are securely managed in the Vercel dashboard.
- Automated Testing: The `test_app.py` file contains tests to ensure the application works as expected.
- Continuous Deployment: The GitHub Actions workflow file automates the deployment process to Vercel whenever changes are pushed to the `main` branch.

# Explanation of test for send_email

- Mocking the `send_email` function: The `@patch('app.send_email')` decorator is used to replace the send_email function with a mock during the test. This allows us to verify that the function is called without actually sending an email.
- Testing the email functionality: The `test_upload_with_email` function tests the upload route with an email provided. It asserts that the response status code is 200 and that the `send_email` function is called exactly once.

Yes, you can definitely run the app locally to test it. Here are the steps to set up and run your Flask app locally:
Steps to Run the App Locally

    Clone the Repository:
        If you haven’t already, clone your GitHub repository to your local machine:

        git clone https://github.com/your-username/your-repo-name.git
        cd your-repo-name

    Create a Virtual Environment:
        It’s a good practice to create a virtual environment to manage your project’s dependencies:

        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    Install Dependencies:
        Install the required packages listed in requirements.txt:

        pip install -r requirements.txt

    Set Up Environment Variables:
        Create a .env file in the root of your project directory and add your environment variables:

        MAIL_SERVER=smtp.example.com
        MAIL_PORT=587
        MAIL_USERNAME=your_email@example.com
        MAIL_PASSWORD=your_email_password
        MAIL_USE_TLS=True
        MAIL_USE_SSL=False

    Run the Flask App:

        Start the Flask development server:

        flask run

        If you encounter an error, you might need to set the FLASK_APP environment variable:

        export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
        flask run

Testing the App

    Access the App:
        Open your web browser and go to http://127.0.0.1:5000/ to see the home page.

    Upload Text or File:
        Use the form on the home page to upload text or a file and optionally provide an email address.

    Check the Output:
        If you provided an email, check your inbox for the PPTX file.
        If you didn’t provide an email, you should be redirected to a page with a download link for the PPTX file.

Running Tests

    Run the Tests:
        Ensure your virtual environment is activated and run the tests using pytest:

        pytest

This setup allows you to develop and test your application locally before deploying it to Vercel. Let me know if you encounter any issues or need further assistance!

