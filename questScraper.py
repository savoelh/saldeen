import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

# Specify the path to chromedriver in your project folder
driver_path = "/home/ai/drivers/chromedriver-linux64/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
print("0")
# Fetch the webpage
url = "https://classicdb.ch/?zone=40#quests"
driver.get(url)
print("1")
# Wait for the table to be loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
print("2")
# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
print("3")
driver.quit()

print(f"Page fetched successfully! {soup.title.string}")

# Find the table
table = soup.find("table", class_="listview-mode-default")
quest_data = []

# Iterate through each row in the table
for row in table.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) == 0:
        continue  # Skip header or empty rows

    quest = {
        "name": "",
        "level": "",
        "req": "",
        "side": "",
        "rewards": [],
        "category": "",
    }

    # Extract data from each cell
    for i, cell in enumerate(cells):
        if i == 0:  # Name
            a_tag = cell.find("a")
            if a_tag:
                quest["name"] = a_tag.text.strip()
                quest["href"] = a_tag.get("href", "")
            else:
                quest["name"] = cell.text.strip()
        elif i == 1:  # Level
            quest["level"] = cell.text.strip()
        elif i == 2:  # Req
            quest["req"] = cell.text.strip()
        elif i == 3:  # Side
            quest["side"] = cell.text.strip()
        elif i == 4:  # Rewards
            divs = cell.find_all("div")
            for div in divs:
                a_tag = div.find("a")
                if a_tag:
                    quest["rewards"].append(a_tag.get("href", ""))
        elif i == 5:  # Category
            quest["category"] = cell.text.strip()

    quest_data.append(quest)

# Write the quest data to data.json
with open("data.json", "w") as f:
    json.dump(quest_data, f, indent=4)

print("Quest data saved to data.json")
