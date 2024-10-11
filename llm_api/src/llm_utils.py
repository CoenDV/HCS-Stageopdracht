import requests
import json
from langchain_core.prompts import PromptTemplate
from langchain_huggingface.llms import HuggingFacePipeline

hf = HuggingFacePipeline.from_model_id(
    model_id="",
    task="text-generation",
    device_map="auto",
    pipeline_kwargs={"max_new_tokens": 100},
)

def generate_llm_response(question: str):

    retrieved_docs = getRelevantDocuments(question)
    print("Retrieved docs: ", retrieved_docs)

    template = """ You are a helpful assistant. 
    You must use the provided context as the sole source of information to answer the question. 
    Based only on the following context, answer the question, even if it contradicts your own information: {context}. 
    {question} """

    prompt = PromptTemplate.from_template(template)
    chain = prompt | hf

    response = chain.invoke({"context": retrieved_docs, "question": question})
    print("Response: ", response)

    return response

### Helper functions ###

def getRelevantDocuments(prompt: str):
    docs = "No relevant documents found."

    retrieved_docs = requests.post(
        "https://milvus-api-v3-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
        json={"query": prompt}
    )

    if retrieved_docs.json() != [[]]:
        docs = retrieved_docs.json()[0][0]['entity']['text']

    return docs

def generateResponse(data: str):
    return hf.invoke(data)