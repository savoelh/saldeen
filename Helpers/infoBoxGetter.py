def infoBoxGetter(infoBox, questDetails):
    if infoBox:
        list_items = infoBox.find_all("li")

        for item in list_items:
            # Level info
            if "Level:" in item.text:
                level_font = item.find("font", class_="tip")
                if level_font:
                    questDetails["level"] = level_font.text.strip().replace(
                        "Level: ", ""
                    )

            # Required level
            elif "Requires level:" in item.text:
                questDetails["required_level"] = item.text.strip().replace(
                    "Requires level: ", ""
                )

            # Side info
            elif "Side:" in item.text:
                side_span = item.find("span", class_="both-icon")
                if side_span:
                    questDetails["side"] = side_span.text.strip()

            # Start info
            elif item.find("img", src="templates/wowhead/images/quest_start.gif"):
                start_link = item.find("a")
                if start_link:
                    href = start_link.get("href", "")
                    if "?npc=" in href:
                        questDetails["start"]["type"] = "npc"
                    elif "?item=" in href:
                        questDetails["start"]["type"] = "item"
                    questDetails["start"]["name"] = start_link.text.strip()
                    questDetails["start"]["href"] = href

            # End info
            elif item.find("img", src="templates/wowhead/images/quest_end.gif"):
                end_link = item.find("a")
                if end_link:
                    href = end_link.get("href", "")
                    if "?npc=" in href:
                        questDetails["end"]["type"] = "npc"
                    elif "?item=" in href:
                        questDetails["end"]["type"] = "item"
                    elif "?object=" in href:
                        questDetails["end"]["type"] = "object"
                    questDetails["end"]["name"] = end_link.text.strip()
                    questDetails["end"]["href"] = href

    return questDetails
