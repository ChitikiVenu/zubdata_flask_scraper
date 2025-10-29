from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os, time

def scrape_google_maps(query):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ Tell Selenium where Render installed Chromium
    chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium")
    options.binary_location = chrome_bin

    try:
        # ✅ Use system chromedriver if available
        chromedriver_path = os.getenv("CHROMEDRIVER_PATH", ChromeDriverManager().install())
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(f"https://www.google.com/maps/search/{query.replace(' ', '+')}")
        time.sleep(5)
        html = driver.page_source
        driver.quit()
        return html
    except Exception as e:
        return str(e)
