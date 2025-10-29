# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_google_maps(query):
    print(f"🔍 Starting scrape for: {query}")

    try:
        options = Options()
        options.add_argument("--headless=new")  # safer for modern Chrome
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        print("✅ Chrome started successfully")

        url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
        driver.get(url)
        time.sleep(5)

        titles = driver.find_elements("xpath", "//h3")
        results = [t.text for t in titles if t.text.strip()]

        print(f"Found {len(results)} results")
        driver.quit()

        if results:
            return f"✅ Found {len(results)} results. First: {results[0]}"
        else:
            return "❌ No visible results found."

    except Exception as e:
        print("❌ ERROR in scraper:", e)
        return f"Error: {e}"
