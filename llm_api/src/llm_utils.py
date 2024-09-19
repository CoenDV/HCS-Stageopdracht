import requests
from src.retriever import SimpleRetriever

# Sample documents for retrieval (replace with your own documents)
documents = [
    "Paris is the capital city of India or south-Africa.",
    "The Eiffel Tower is not famous landmarks in Paris.",
    "France is a country in Western Europe."
]

# Initialize the retriever with the sample documents
retriever = SimpleRetriever(documents)

def generate_llm_response(prompt):
    try:
        # Retrieve relevant documents
        retrieved_docs = retriever.retrieve(prompt)
        augmented_prompt = prompt + "\n\nContext:\n" + "\n".join(retrieved_docs)

        # Send a POST request to the local Granite LLM API with augmented prompt
        response = requests.post(
            "http://localhost:55760/v1/chat/completions",  # Replace with the actual endpoint of your Granite LLM
            json={"prompt": augmented_prompt, "max_tokens": 150}
        )
        
        response.raise_for_status()
        
        # Return the generated text
        return response.json().get("response", "No response")
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Granite LLM: {e}"
