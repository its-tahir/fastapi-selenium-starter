from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pydantic import BaseModel

app = FastAPI()


class SearchQuery(BaseModel):
    repo_name: str
    search_class: str


@app.post("/search")
def search(query: SearchQuery):
    chrome_service = Service(executable_path=r"./chromedriver-win64/chromedriver.exe")
    chrome_options = Options()

    # Uncomment the line below if you want to run in headless mode
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Navigate to the GitHub page for the provided repository
    url = f"https://github.com/{query.repo_name}"
    driver.get(url)

    try:
        # Wait for the element with the specified class to be present
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, query.search_class))
        )
        element_text = element.text
    except Exception as e:
        element_text = f"Error: {str(e)}"
    finally:
        driver.quit()

    return {"element_text": element_text}
