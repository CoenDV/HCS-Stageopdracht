import requests
import json
from langchain_core.prompts import PromptTemplate
from langchain_huggingface.llms import HuggingFacePipeline

hf = HuggingFacePipeline.from_model_id(
    task="text-generation",
    model_id="meta-llama/Llama-3.2-1B",    
    device_map="auto",
    pipeline_kwargs={"max_new_tokens": 100, "temperature": 0.1}
)

def generate_llm_response(question: str):

    retrieved_docs = getRelevantDocuments(question)
    prompt = formatTemplate()
    chain = prompt | hf
    response = chain.invoke({"context": retrieved_docs, "question": question})
    return formatResponse(response)

### Helper methods ###

def getRelevantDocuments(prompt: str):
    docs = "No relevant documents found."

    retrieved_docs = requests.post(
        "https://milvus-api-v3-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
        json={"query": prompt}
    )

    if retrieved_docs.json() != [[]]:
        docs = retrieved_docs.json()[0][0]['entity']['text']

    return docs

def formatTemplate():
    template = """ 
    Question: {question}
    Context: {context}
    Answer:
     """
    return PromptTemplate.from_template(template)

def formatResponse(response):
    return response.split("Answer:", 1)[1].strip("Answer:")