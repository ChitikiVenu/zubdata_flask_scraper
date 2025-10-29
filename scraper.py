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
    chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
    options.binary_location = chrome_bin

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(f"https://www.google.com/maps/search/{query.replace(' ', '+')}")
        time.sleep(5)
        page_source = driver.page_source
        driver.quit()
        return page_source
    except Exception as e:
        return str(e)
