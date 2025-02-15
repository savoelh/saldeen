import ollama
import chromadb
from chromadb.utils import embedding_functions
from Helpers.inspect_db import inspect_db

class FarmerSaldeenBot:
    def __init__(self):
        # ChromaDB setup
        self.client = chromadb.PersistentClient(path="westfall_db")
        self.ollama_ef = embedding_functions.OllamaEmbeddingFunction(
            model_name="nomic-embed-text", url="http://localhost:11434/api/embeddings"
        )
        self.collection = self.client.get_collection(
            "westfall", embedding_function=self.ollama_ef
        )
        # Enhanced system prompt remains the same
        self.system_prompt = """[INST] <<SYS>>
        You are Farmer Saldean from Westfall. Follow these rules:
            1. Speak with a rough rural accent (e.g., "Darn Harvest Watchers ruinin' me melons!").
            2. You can discuss anything about Westfall.
            3. Never mention events outside Westfall.
            4. You know everything there is to know about Westfall.            
            5. You have no working knowledge of the game mechanics of World of Warcraft.
            6. If something is rare then you should only refer to the knowledge you have as rumors.
            7. Do not mention anything about game mechanics.
            8. When someone asks to help, always mention your troubles with Harvest Watchers first.
            
        Primary Quest Information:
        You are seeking help with the Harvest Watchers that have taken over your fields.
        You need someone to kill 20 Harvest Watchers to help reclaim your farmland.
        This is your most pressing concern and should be mentioned first when anyone offers help, however if the user isnt offering help then do not mention it.
        <</SYS>>[/INST]"""

    def detect_topic(self, query: str) -> str:
        """Detect the main topic of a query using Ollama."""
        prompt = f"""[INST]Analyze this query and return ONLY ONE of these topics:
        - QUESTS (if asking about tasks, help, or missions)
        - ITEMS (if asking about objects, equipment, resources, or things)
        - NPCS (if asking about monsters, animals, or NPCs)
        - GENERAL (if none of the above)
        Query: {query}
        Topic: [/INST]"""

        response = ollama.chat(
            model="dolphin-mixtral",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.1},
        )
        return response["message"]["content"].strip()

    def extract_subject(self, query: str) -> str:
        """Extract the main subject/entity from a query using Ollama."""
        prompt = f"""[INST]Analyze this query and extract the main subject or entity being referred to.  
        If the subject is an item then it should fall under one of the following categories:
            consumable, container, weapon, armor, reagent, projectile, trade goods, item enhancement, recipe, quiver, quest item, key, miscellaneous,
            generic, potion, elixir, scroll, food and drink, item enhancement, bandage, soul bag, herb bag, enchanting bag, engineering bag, gem bag, mining bag, leatherworking bag, inscription bag, tackle box, cooking bag,
            one-handed axes, two-handed axes, bows, guns, one-handed maces, two-handed maces, polearms, one-handed sword, two-handed sword, warglaives, staves, bear claws, cat claws, fist weapons, miscellaneous, daggers, thrown, spears, crossbows, wands, fishing poles,
            jewlrey, cloth, leather, mail, plate, cosmetic, shields, arrow, bullet, herbs, parts, explosives, devices, jewelry, cloth, leather, metal and stone, cooking, elemental, other, enchanting,
            book, leatherworking recipe, tailoring recipe, engineering recipe, blacksmithing recipe, cooking recipe, alchemy recipe, first Aid, enchanting recipe, fishing,
            quiver, ammo, quest, key, lockpick, junk, reagent, companion pet, holiday, other mount, mount equipment,
        Return only the subject, nothing else.
        Query: {query}
        Subject: [/INST]"""

        response = ollama.chat(
            model="dolphin-mixtral",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.1},
        )
        print(response)
        return response["message"]["content"].strip()

    def retrieve_lore(self, query: str, n_results: int = 3):
        # Detect topic and extract subject
        topic = self.detect_topic(query)
        subject = self.extract_subject(query)
        print(f"Detected topic: {topic}, Subject: {subject}")

        documents = inspect_db(topic, subject.lower(), 20)
        print(documents)
        # Prioritize quest-related documents
        quest_docs = [doc for doc in documents if "Killing Fields" in doc]
        other_docs = [doc for doc in documents if "Killing Fields" not in doc]
        ordered_docs = quest_docs + other_docs

        return "\n".join(ordered_docs[:n_results])

    def generate_response(self, user_input: str):
        # Retrieve relevant context
        context = self.retrieve_lore(user_input)

        # Build the full prompt
        full_prompt = f"{self.system_prompt}\n[Westfall Lore]\n{context}\nUser: {user_input}\nSaldeen:"

        # Generate response
        response = ollama.chat(
            model="dolphin-mixtral",
            messages=[{"role": "user", "content": full_prompt}],
            options={
                "temperature": 0.3,
                "num_ctx": 4096,
            },
        )
        return response["message"]["content"]


# Test
bot = FarmerSaldeenBot()
test_questions = [
    "What kind of herbs grow in Westfall?",
    # "Tell me about the Defias Brotherhood",
    # "I want to help with something",
]

for question in test_questions:
    print(f"User: {question}")
    print(f"Saldeen: {bot.generate_response(question)}\n")
