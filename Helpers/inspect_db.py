import chromadb
from chromadb.utils import embedding_functions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

item_sub_types = [
    "consumable",
    "container",
    "weapon",
    "armor",
    "reagent",
    "projectile",
    "trade goods",
    "item enhancement",
    "recipe",
    "quiver",
    "quest item",
    "key",
    "miscellaneous",
    "generic",
    "potion",
    "elixir",
    "scroll",
    "food and drink",
    "item enhancement",
    "bandage",
    "soul bag",
    "herb bag",
    "enchanting bag",
    "engineering bag",
    "gem bag",
    "mining bag",
    "leatherworking bag",
    "inscription bag",
    "tackle box",
    "cooking bag",
    "one-handed axes",
    "two-handed axes",
    "bows",
    "guns",
    "one-handed maces",
    "two-handed maces",
    "polearms",
    "one-handed sword",
    "two-handed sword",
    "warglaives",
    "staves",
    "bear claws",
    "cat claws",
    "fist weapons",
    "miscellaneous",
    "daggers",
    "thrown",
    "spears",
    "crossbows",
    "wands",
    "fishing poles",
    "jewelry",
    "cloth",
    "leather",
    "mail",
    "plate",
    "cosmetic",
    "shields",
    "arrow",
    "bullet",
    "herbs",
    "parts",
    "explosives",
    "devices",
    "jewelry",
    "cloth",
    "leather",
    "metal and stone",
    "cooking",
    "elemental",
    "other",
    "enchanting",
    "book",
    "leatherworking recipe",
    "tailoring recipe",
    "engineering recipe",
    "blacksmithing recipe",
    "cooking recipe",
    "alchemy recipe",
    "first aid",
    "enchanting recipe",
    "fishing",
    "quiver",
    "ammo",
    "quest",
    "key",
    "lockpick",
    "junk",
    "reagent",
    "companion pet",
    "holiday",
    "other mount",
    "mount equipment",
]


def inspect_db(source, sub_type, results_n):
    print(source, sub_type)
    # Initialize Chroma
    client = chromadb.PersistentClient(path="westfall_db")
    ollama_ef = embedding_functions.OllamaEmbeddingFunction(
        model_name="nomic-embed-text", url="http://localhost:11434/api/embeddings"
    )

    # Get the collection
    collection = client.get_collection(name="westfall", embedding_function=ollama_ef)

    # Query the collection to retrieve all documents
    query_params = {
        "query_texts": ["*"],  # Use a wildcard to retrieve all documents
        "n_results": 1000,  # Adjust the number of results as needed
        "include": ["documents", "metadatas"],
    }

    def check_sub_type(sub_type):
        if sub_type in item_sub_types:
            return sub_type
        else:
            return False

    def create_query(filter_type, filter_value, search_in_documents=False):
        # Initialize the vectorizer and fit it on the filter_value
        vectorizer = TfidfVectorizer().fit([filter_value])
        filter_value_vec = vectorizer.transform([filter_value])

        # Iterate over documents and their corresponding metadata
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            if search_in_documents:
                # Compute the similarity between the filter_value and the document content
                doc_vec = vectorizer.transform([doc])
                similarity = cosine_similarity(filter_value_vec, doc_vec).flatten()[0]
                # Define a threshold for similarity (e.g., 0.5)
                if similarity >= 0.5:
                    print(doc, meta, "Searched docs... hit the similarity threshold:", similarity)
                    # If it matches, add the document and metadata as a tuple to the filtered results
                    filtered_results.append((doc, meta))
            else:
                # Check if the metadata's filter_type matches the filter_value
                if meta.get(filter_type) == filter_value:
                    print(doc, meta, "hit the else statement inside create query")
                    # If it matches, add the document and metadata as a tuple to the filtered results
                    filtered_results.append((doc, meta))

    try:
        results = collection.query(**query_params)
        # Initialize an empty list to store filtered results
        filtered_results = []
        verified_sub_type = check_sub_type(sub_type)
        if verified_sub_type:
            create_query("subType", sub_type)
        else:
            create_query("source", sub_type, search_in_documents=True)
        # Print the filtered results
        for doc, meta in filtered_results:
            print(f"Document: {doc}")
            print(f"Metadata: {meta}")
            print("-" * 80)
        return filtered_results
    except RuntimeError as e:
        print(f"An error occurred during the query: {e}")


if __name__ == "__main__":
    inspect_db()
