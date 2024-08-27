# FastAPI with Selenium Example

This project demonstrates how to integrate FastAPI with Selenium for web automation tasks. It includes a FastAPI application that uses Selenium to navigate to a GitHub repository page specified in the query and retrieve the text of an element with a class also specified in the query.


## Prerequisites

1. **Python**: Ensure you have Python 3.7 or later installed on your system.
2. **Google Chrome**: Install the latest version of Google Chrome.

## Installation

1. **Clone the repository** (or download and unzip the project files):

   ```sh
   git clone https://github.com/its-tahir/fastapi-selenium-starter.git
   cd fastapi-selenium-starter
   ```

2. **Create and activate a virtual environment**:
    python -m venv myenv
    myenv\Scripts\activate  # For Command Prompt
    # or
    .\myenv\Scripts\Activate  # For PowerShell


3. **Install the required Python packages:**:
    pip install -r requirements.txt

4. **Download ChromeDriver**:
    Visit the ChromeDriver download page (https://googlechromelabs.github.io/chrome-for-testing/).
    Download the version that matches your Chrome browser.
    Extract chromedriver.exe to a directory

## Run the application

    uvicorn main:app --reload

    The server will start on http://127.0.0.1:8000.

    Send a POST request to the /search endpoint with the search query in JSON format. You can use a tool like Postman or curl. Here’s an example using curl:

    curl -X POST "http://127.0.0.1:8000/search" -H "Content-Type: application/json" -d '{"repo_name": "its-tahir/fastapi-selenium-starter", "search_class": ".f4.my-3"}'

