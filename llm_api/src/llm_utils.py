import requests
import json

def generate_llm_response(prompt):

    retrieved_docs = getRelevantDocuments(prompt)

    data = createPayload(prompt, retrieved_docs)
    print("Data: ", json.dumps(data, indent=4))

    response = generateResponse(data)
    
    response.raise_for_status()

    return response.json().get("choices")

### Helper functions ###

def getRelevantDocuments(prompt: str):
    return requests.post(
        "https://milvus-api-v4-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
        json={"query": prompt}
    )

def createPayload(prompt: str, retrieved_docs: str):
    
    # Concatenate the retrieved documents into a single string
    context_text = "No relevant documents found."
    if retrieved_docs.json() != [[]]:
        context_text = "".join(f"{doc}" for doc in retrieved_docs.json()[0][0]['entity']['text'])

    return {
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

def generateResponse(data: str):
    return requests.post(
        # Strange_hopper is auto generated name for podman AI container
        "http://strange_hopper:8000/v1/chat/completions/",
        json=data
    )