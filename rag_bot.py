import ollama
import chromadb
from chromadb.utils import embedding_functions
from Helpers.inspect_db import inspect_db
import json

rule_set = """ "You are Farmer Saldean from Westfall. Follow these rules:
            1. Speak with a rough rural accent (e.g., "Darn Harvest Watchers ruinin' me melons!").
            2. You can discuss anything about Westfall.
            3. Never mention events outside Westfall.
            4. You know everything there is to know about Westfall.            
            5. You have no working knowledge of the game mechanics of World of Warcraft.
            6. If something is rare then you should only refer to the knowledge you have as rumors.
            7. Do not mention anything about game mechanics.
            8. When someone asks to help, mention your troubles with Harvest Watchers.
            
        Quest Information:
        You are seeking help with the Harvest Watchers that have taken over your fields.
        You need someone to kill 20 Harvest Watchers to help reclaim your farmland.
        This is your most pressing concern and should be mentioned first when anyone offers help, however if the user isnt offering help then do not mention it."""

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
        self.system_prompt = f"[INST] <<SYS>> {rule_set} <</SYS>>[/INST]"

    def detect_topic(self, query: str) -> str:
        print("Started topic detection")
        """Detect the main topic of a query using Ollama."""
        prompt = f"""[INST]Analyze this query and return ONLY ONE of these topics:
        - QUESTS (if asking about tasks, help, or missions)
        - ITEMS (if asking about objects, equipment, resources, or things)
        - NPCS (if asking about monsters, animals, or NPCs)
        - GENERAL (if none of the above)
        Query: {query}
        Topic: [/INST]"""

        response = ollama.chat(
            # model="deepseek-r1:70b",
            model="deepseek-r1:14b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.1},
        )
        result = response["message"]["content"].strip()
        result = result.replace("<think>", "").replace("</think>", "")        
        result = result.split("\n")[-1] if "\n" in result else result

        return result

    def extract_subject(self, query: str) -> str:
        print("Started subject extraction")
        """Extract the main subject/entity from a query using Ollama."""
        prompt = f"""[INST]Analyze this query and extract the main subject or entity being referred to.  
        Return only the subject, nothing else.
        Query: {query}
        Subject: [/INST]"""
        
        response = ollama.chat(
            # model="dolphin-mixtral",
            model="deepseek-r1:14b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.1},
        )
        # Clean up response by removing any thinking
        result = response["message"]["content"].strip()
        result = result.replace("<think>", "").replace("</think>", "")        
        result = result.split("\n")[-1] if "\n" in result else result
        
        return result

    def retrieve_lore(self, query: str, n_results: int = 3):
        print("Started retrieving lore")
        # Detect topic and extract subject
        topic = self.detect_topic(query)
        subject = self.extract_subject(query)
        print(f"Detected topic: {topic}, Subject: {subject}")
    
        documents = inspect_db(topic, subject.lower(), 20)
        formatted_documents = json.dumps(documents, indent=2)
        print(formatted_documents)

        return formatted_documents

    def generate_response(self, user_input: str):
        context = self.retrieve_lore(user_input)
        full_prompt = f"""{self.system_prompt}
        
    [Context Information (Remember to speak in character)]\n{context}

    User: {user_input}

    {rule_set}
        
    Saldeen:"""

        response = ollama.chat(
            model="wizardlm2",
            messages=[{"role": "user", "content": full_prompt}],
            options={
                "temperature": 0.7,  # Increased for more creative responses
                "num_ctx": 1000,
                # "top_p": 0.9,
            },
        )
        return response["message"]["content"]

# Test
bot = FarmerSaldeenBot()
test_questions = [
    "I am looking for a new belt. Where might I find one?"
]

for question in test_questions:
    print(f"User: {question}")
    print(f"Saldeen: {bot.generate_response(question)}\n")
