import requests
import json
from transformers import pipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

llm_pipeline = pipeline(
    task="text-generation",
    model="liminerity/Phigments12",
    trust_remote_code=True,
    torch_dtype="auto",
    device_map="auto",
    max_new_tokens=5
)

hf = HuggingFacePipeline(pipeline=llm_pipeline)

def generate_llm_response(prompt):

    retrieved_docs = getRelevantDocuments(prompt)

    data = createPayload(prompt, retrieved_docs)
    print("Data: ", json.dumps(data, indent=4))

    #response = generateResponse(data)
    response = hf.invoke("What is full covearge insurance?")
    print("Response: ", response)
    
    response.raise_for_status()

    return response.json().get("choices")

### Helper functions ###

def getRelevantDocuments(prompt: str):
    return requests.post(
        "https://milvus-api-v3-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
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
    return hf.invoke(data)