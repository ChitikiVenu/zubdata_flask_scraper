from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os, time

def scrape_google_maps(query):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ Correct chromium path
    options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium")

    service = Service(os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver"))
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(f"https://www.google.com/maps/search/{query.replace(' ', '+')}")
    time.sleep(5)
    html = driver.page_source
    driver.quit()
    return html
