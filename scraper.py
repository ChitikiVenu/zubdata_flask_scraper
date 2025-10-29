# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_google_maps(query):
    # Chrome options for Render/Headless
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # ✅ Corrected driver initialization
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Open Google Maps search
    search_url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
    driver.get(search_url)
    time.sleep(5)

    # Simple demo — capture the first result title
    try:
        first_result = driver.find_element("xpath", '(//h3)[1]').text
        print(f"First result: {first_result}")
    except Exception as e:
        print("No result found:", e)

    driver.quit()
    return "Scraping completed!"
