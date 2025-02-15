import chromadb
from chromadb.utils import embedding_functions


def inspect_db(source, sub_type, results_n):
    print(source, sub_type, )
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

    def create_query(filter_type, filter_value):
        # Iterate over documents and their corresponding metadata
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            # Check if the metadata's subType matches the desired sub_type
            if meta.get(filter_type) == filter_value:
                # If it matches, add the document and metadata as a tuple to the filtered results
                filtered_results.append((doc, meta))

    try:
        results = collection.query(**query_params)
        print()
        # Initialize an empty list to store filtered results
        filtered_results = []
        if sub_type:
            create_query("subType", sub_type)
        else:
            create_query("source", source)
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
