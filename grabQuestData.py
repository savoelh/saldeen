import json
from saleen.Helpers.getWebData import getWebData
from Helpers.infoBoxGetter import infoBoxGetter
from Helpers.questTextGetter import questTextGetter

with open("questData.json", "r") as f:
    questData = json.load(f)


def getQuestData(quest):
    pageData = getWebData(f"{quest["href"]}")
    infoBox = pageData.find("table", class_="infobox")
    mainBody = pageData.find("div", class_="text")
    comments = pageData.find("div", class_="listview-mode-div")
    green_comments = comments.find_all("div", class_="comment-body comment-green")

    # Initialize quest details dictionary with existing data
    questDetails = {
        "name": quest["name"],
        "href": quest["href"],
        "category": quest.get("category", ""),
        "level": None,
        "required_level": None,
        "side": None,
        "start": {"type": None, "name": None, "href": None},
        "end": {"type": None, "name": None, "href": None},
        "rewards": quest.get("rewards", []),
        "objective": None,
        "description": None,
        "completion": None,
        "comments": [],
    }

    questDetails = infoBoxGetter(infoBox, questDetails)
    questDetails = questTextGetter(mainBody, questDetails)

    for comment in green_comments:
        comment_data = {
            "text": comment.text.strip(),
            "sentiment": "positive",
        }
        questDetails["comments"].append(comment_data)

    return questDetails


newQuestData = []
for quest in questData:
    newQuestData.append(getQuestData(quest))

with open("questData.json", "w") as f:
    json.dump(newQuestData, f, indent=4)
