import os
import json
import chromadb
from chromadb.utils import embedding_functions
from Helpers.itemClassAssign import item_class_assign

current_dir = os.path.dirname(os.path.abspath(__file__))


def process_data():
    # Get data into chroma db
    # Initialize Chroma
    client = chromadb.PersistentClient(path="westfall_db")
    try:
        ollama_ef = embedding_functions.OllamaEmbeddingFunction(
            model_name="nomic-embed-text",
            url="http://localhost:11434/api/embeddings"
        )
        # Test connection
        test_result = ollama_ef(["Test connection"])
        if not test_result:
            raise ConnectionError("Could not connect to Ollama service")
    except Exception as e:
        print("Error initializing Ollama:", str(e))
        return
    try:
        client.delete_collection(name="westfall")
    except chromadb.errors.CollectionNotFoundError:
        pass

    collection = client.create_collection(name="westfall", embedding_function=ollama_ef)

    documents = []
    metadatas = []
    ids = []

    # Process NPC Data
    with open(os.path.join(current_dir, "data", "npcData.json"), "r") as f:
        npcs = json.load(f)
        for npc in npcs:
            if npc.get("location", "").lower() == "westfall":
                comments = " ".join([c["text"] for c in npc.get("comments", [])])
                doc_text = (
                    f"NPC {npc['name']} (Level {npc['level']} {npc.get('class', '')}): "
                    f"{comments} Faction: {npc.get('faction', '')}. "
                    f"Location: {npc.get('location', 'Westfall')}"
                )
                metadata = {
                    "source": "npc",
                    "name": npc["name"],
                    "faction": npc.get("faction", ""),
                    "location": "Westfall",
                    "class": npc["class"],
                }
                documents.append(doc_text)
                metadatas.append(metadata)

    # Process Item Data
    with open(os.path.join(current_dir, "data", "itemData.json"), "r") as f:
        items = json.load(f)
        for item in items:
            try:
                percent = item.get("percent", 0)
                if percent >= 10:
                    rarity = "common"
                elif 1 <= percent < 10:
                    rarity = "uncommon"
                else:
                    rarity = "rare"
                doc_text = (
                    f"Item {item['name']}: Level {item.get('level', 'N/A')}. {item.get('description', '')}"
                )
                item_classes = item_class_assign(item)
                metadata = {
                    "source": "item",
                    "name": item["name"],
                    "type": item_classes["item_type"],
                    "rarity": rarity,
                    "subType": item_classes["item_sub_type"],
                }
                documents.append(doc_text)
                metadatas.append(metadata)
            except Exception as e:
                print(f"Skipping item {item.get('name', 'unknown')} due to error: {e}")

    # Process Quest Data
    with open(os.path.join(current_dir, "data", "questData.json"), "r") as f:
        quests = json.load(f)
        for quest in quests:
            if quest.get("category", "").lower() == "westfall":
                comments = " ".join([c["text"] for c in npc.get("comments", [])])
                doc_text = (
                    f"Quest {quest['name']}: {quest['objective']}. Reward: {', '.join(quest['rewards'])}"
                    f"{comments}"
                )
                metadata = {
                    "source": "quest",
                    "name": quest["name"],
                    "level": quest.get("level", ""),
                    "giver": quest["start"]["name"] if quest.get("start") else "",
                }
                documents.append(doc_text)
                metadatas.append(metadata)

    # Check embeddings
    try:
        embeddings = ollama_ef(documents)        
        if not embeddings:
            raise ValueError("Embeddings are empty")
    except Exception as e:
        print("Error generating embeddings:", e)
        return

    # Add to ChromaDB with unique IDs
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=[f"id_{i}" for i in range(len(documents))],
        )
        print("Finished processing documents")
    except Exception as e:
        print("Error adding to collection:", e)


if __name__ == "__main__":
    process_data()
