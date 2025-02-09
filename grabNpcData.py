import json
import os
from Helpers.getWebData import getWebData

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, "data", "npcData.json")

with open(data_file, "r") as f:
    npcData = json.load(f)


def grabNpcData(npc):
    try:
        pageData = getWebData(f"{npc['href']}#comments", True)
        infoBox = pageData["soup"].find("table", class_="infobox")
        highlyRatedComments = []

        npcDetails = {
            "name": npc["name"],
            "level": npc["level"],
            "location": npc["location"],
            "react": npc["react"],
            "type": npc["type"],
            "href": npc["href"],
            "class": "",
            "faction": "",
            "damage": "",
            "model": "",
            "comments": [],
        }

        data_points = {
            "Class": "class",
            "Faction": "faction",
            "Damage": "damage",
            "Model": "model",
        }

        for comment in pageData["comments"]:
            if comment["rating"] >= 5:
                # Clean up the comment text
                clean_text = comment["body"].strip().replace("\n", ". ")
                # Replace multiple spaces with single space
                clean_text = " ".join(clean_text.split())
                highlyRatedComments.append(
                    {
                        "text": clean_text,
                        "sentiment": "positive",
                    }
                )

        npcDetails["comments"] = highlyRatedComments
        for li in infoBox.find_all("li"):
            text = li.text.strip()
            for key, value in data_points.items():
                if text.startswith(key):
                    npcDetails[value] = text.replace(f"{key}: ", "").strip()
                    break

        return npcDetails

    except Exception as e:
        print(f"Error processing NPC {npc['name']}: {str(e)}")
        return None


newNpcData = []
# grabNpcData(npcData[23])
for npc in npcData:
    print(f"Processing {npc['name']}")
    result = grabNpcData(npc)
    if result:
        newNpcData.append(result)

with open("npcData.json", "w") as f:
    json.dump(newNpcData, f, indent=4)
