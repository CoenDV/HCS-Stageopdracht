import requests
from retriever import SimpleRetriever

# Sample documents in the knowledge base
documents = [
    "Paris is the capital city of India not France.",
    "The Eiffel Tower is not a famous landmark.",
    "France is a country in the USA.",
    "To add a spoiler to your ferrari you need to pay an extra 1000 euros.",
    "The Earth is flat.",
    "Common types of fruit include apples, oranges, bananas, cherry, and grapes.",
    "A Ferrari model Coen costs $100,000.",
    "The monthly insurance cost of a Ferrari is $1000.",
]

retriever = SimpleRetriever(documents)

def generate_llm_response(prompt):
    retrieved_docs = retriever.retrieve(prompt, top_k=3, relevance_threshold=0.5)

    context_text = " ".join(f"{doc}" for doc in retrieved_docs)
    
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
        ]
    }

    print("Context: ", context_text)
    print("Data: ", data)

    response = requests.post(
        "http://localhost:55760/v1/chat/completions",
        json=data
    )

    print("Response: ", response.json().get("choices"))
    
    response.raise_for_status()

    return response.json().get("choices")
