from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def run_scraper(query):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.binary_location = "/usr/bin/google-chrome"  # 👈 Important

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(f"https://www.google.com/maps/search/{query}")
        data = driver.page_source
        driver.quit()
        return data
    except Exception as e:
        print("❌ ERROR in scraper:", e)
        return str(e)
