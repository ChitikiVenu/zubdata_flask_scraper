from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_google_maps(query):
    print(f"🔍 Starting scrape for: {query}")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # ✅ Use the correct Chrome binary path for Render
    options.binary_location = "/usr/bin/google-chrome-stable"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(f"https://www.google.com/maps/search/{query}")
    time.sleep(5)
    print(driver.title)
    driver.quit()
