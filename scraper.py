from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_google_maps(query, limit=10):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(f"https://www.google.com/maps/search/{query}")

    time.sleep(5)
    results = []

    elements = driver.find_elements(By.CLASS_NAME, "Nv2PK")[:limit]
    for el in elements:
        try:
            name = el.find_element(By.CLASS_NAME, "qBF1Pd").text
        except:
            name = ""
        try:
            rating = el.find_element(By.CLASS_NAME, "MW4etd").text
        except:
            rating = ""
        try:
            address = el.find_element(By.CLASS_NAME, "W4Efsd").text
        except:
            address = ""
        results.append({"Name": name, "Rating": rating, "Address": address})

    driver.quit()

    df = pd.DataFrame(results)
    output_path = "results.csv"
    df.to_csv(output_path, index=False)
    return output_path
