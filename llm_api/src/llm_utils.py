import requests
import json

def generate_llm_response(prompt):

    # Retrieve the documents relevant to the prompt
    retrieved_docs = requests.post(
        "https://milvus-api-v4-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
        json={"query": prompt}
    )

    # Concatenate the retrieved documents into a single string
    context_text = "".join(f"{doc}" for doc in retrieved_docs.json()[0][0]['entity']['text'])

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

    # Send the request to the LLM
    response = requests.post(
        "http://localhost:55760/v1/chat/completions",
        json=data
    )

    print("Response: ", json.dumps(response.json().get("choices"), indent=4))
    
    response.raise_for_status()

    return response.json().get("choices")
