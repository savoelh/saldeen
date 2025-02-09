from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import random
import json


def getWebData(href, comment=False, item=False):
    # Clear Chrome cache directory first
    import shutil
    import os
    
    # WSL Ubuntu Chrome cache location
    cache_dir = os.path.expanduser('~/.cache/google-chrome')
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        os.makedirs(cache_dir)
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--incognito")  # Use incognito mode
    options.add_argument(f"--disk-cache-dir={cache_dir}")  # Set cache directory
    options.add_argument("--disable-application-cache")
    options.add_argument("--media-cache-size=0")
    print("options set")
    # Specify the path to chromedriver in your project folder
    driver_path = "/home/ai/drivers/chromedriver-linux64/chromedriver"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    url = f"https://classicdb.ch/{href}"

    items_data = []
    comments_data = []

    try:
        print(f"Getting Driver {url}")
        driver.get(url)
        print("Got the driver")

        scripts = driver.find_elements(By.TAG_NAME, "script")
        for script in scripts:
            script_content = script.get_attribute("innerHTML")

            if item:
                if "data:[" in script_content:
                    # Find start of data array
                    items_start = script_content.find("data:[") + len("data:[")
                    # Find end of data array (looking for "]});" which ends the Listview initialization)
                    items_end = script_content.find("]});", items_start)

                    if items_start > -1 and items_end > -1:
                        items_json = "[" + script_content[items_start:items_end] + "]"
                        items_data = items_json

            if comment:
                # Find comments data
                if "var wh_comments = " in script_content:
                    comments_start = script_content.find("var wh_comments = ") + len(
                        "var wh_comments = "
                    )
                    comments_end = script_content.find("];", comments_start) + 1
                    comments_json = script_content[comments_start:comments_end]
                    try:
                        comments_data = json.loads(comments_json)
                        print("Comments found")
                    except json.JSONDecodeError as e:
                        print(f"Error parsing comments JSON: {e}")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        sleep_time = random.uniform(1, 7)
        print(f"Sleeping for {sleep_time:.2f} seconds")
        time.sleep(sleep_time)
        return {"soup": soup, "comments": comments_data, "items": items_data}

    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    finally:
        driver.quit()
