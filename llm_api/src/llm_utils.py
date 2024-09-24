import requests
from retriever import SimpleRetriever
import json

retriever = SimpleRetriever()

def generate_llm_response(prompt):
    retrieved_docs = retriever.retrieve(prompt, top_k=3, relevance_threshold=0.5)

    # Concatenate the retrieved documents into a single string
    context_text = " ".join(f"{doc}" for doc in retrieved_docs)
    
    # Build the data payload
    data = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. You must use the provided context as the sole source of information to answer the question. "
                    "Based only on the following context, answer the question, even if it contradicts your own information: " + context_text
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 100,
    }

    print("Data: ", json.dumps(data, indent=4))

    response = requests.post(
        "http://localhost:55760/v1/chat/completions",
        json=data
    )

    print("Response: ", json.dumps(response.json().get("choices"), indent=4))
    
    response.raise_for_status()

    return response.json().get("choices")
