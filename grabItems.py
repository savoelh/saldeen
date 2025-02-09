import json
import os
from Helpers.getWebData import getWebData

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, "data", "npcData.json")
item_file = os.path.join(current_dir, "data", "itemData.json")

with open(data_file, "r") as f:
    npcData = json.load(f)
with open(item_file, "r") as f:
    currItemData = json.load(f)


def format_name(name):
    # Replace escaped quotes with apostrophes
    if name.find('\\"s') != -1:
        name = name.replace('/"s', "'s")
    # Add spaces before capitals, except first letter
    formatted = name[0]
    for char in name[1:]:
        if char.isupper():
            formatted += " " + char
        else:
            formatted += char

    return formatted.strip()


def create_item_id(name):
    # Remove special characters and spaces
    name = name.replace("'", "").replace(" ", "")
    # Convert to camelCase
    return name[0].lower() + name[1:]


def grabItemData(npc):
    try:
        pageData = getWebData(f"{npc['href']}", False, True)
        items = pageData["items"]

        # Check if items is already a list
        if isinstance(items, list):
            items_data = items
        else:
            if "side:" in items:
                print("Skipping.....................................")
                return False

            npcDetails = {
                "name": npc["name"],
                "level": npc["level"],
                "location": npc["location"],
                "react": npc["react"],
                "type": npc["type"],
                "href": npc["href"],
                "class": npc["class"],
                "faction": npc["faction"],
                "damage": npc["damage"],
                "model": npc["model"],
                "comments": npc["comments"],
            }
            # Clean and format items JSON
            items = (
                items.replace("'", '"')
                .replace("name:", '"name":')
                .replace("reqlevel:", '"reqLevel":')
                .replace("level:", '"level":')
                .replace("classs:", '"classs":')
                .replace("subclass:", '"subclass":')
                .replace("percent:", '"percent":')
                .replace("group:", '"group":')
                .replace("id:", '"id":')
                .replace("phaseval:", '"phaseval":')
                .replace("stack:", '"stack":')
                .replace("\n", "")
                .replace(" ", "")
            )
            # Remove number prefix from item names
            items = items.replace('"7', '"').replace('"6', '"').replace('"5', '"')
            # Parse JSON string into Python objects
            items_data = json.loads(items)

        # Get existing item IDs
        with open(item_file, "r") as f:
            existing_items = json.load(f)
            existing_ids = {item["itemId"] for item in existing_items}
        npc_items = []
        # Filter and process new items
        for item in items_data:
            item["name"] = format_name(item["name"])
            item["itemId"] = create_item_id(item["name"])
            npc_items.append(item["itemId"])
            # Only add items that don't exist
            if item["itemId"] not in existing_ids:
                existing_items.append(item)

            # Save updated items back to file

        with open(item_file, "w") as f:
            json.dump(existing_items, f, indent=4)

        npcDetails["items"] = npc_items
        return npcDetails

    except AttributeError as e:
        print(f"Error processing items: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# Main execution
if __name__ == "__main__":
    for npc in npcData:
        try:
            result = grabItemData(npc)
            if result:
                print(f"Processed NPC: {npc['name']}")
        except Exception as e:
            print(f"Error processing NPC {npc['name']}: {e}")
            continue
