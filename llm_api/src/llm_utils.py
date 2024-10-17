import requests
import json
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_huggingface.llms import HuggingFacePipeline

system_prompt = SystemMessagePromptTemplate.from_template(
    "You are a helpful assistant for a car insurance company."
    "Use the provided context to answer the question. If you don't know the answer, say you don't know."
    "Keep the answer concise with a maximum of 5 sentences."
    "Answer the question based on the context: {context}."
)

human_prompt = HumanMessagePromptTemplate.from_template(
    "Answer the following question: {question} Answer: "
)

prompt = ChatPromptTemplate.from_messages(
    [
        system_prompt, 
        human_prompt
    ]
)

hf = HuggingFacePipeline.from_model_id(
    task="text-generation",
    # model_id="meta-llama/Llama-3.2-1B",  
    model_id="meta-llama/Llama-3.2-3B",
    device_map="auto",
    pipeline_kwargs={"max_new_tokens": 50, "temperature": 0.1}
)

chain = prompt | hf

def generate_llm_response(question: str):

    retrieved_docs = getRelevantDocuments(question)
    
    response = chain.invoke({"context": retrieved_docs, "question": question})
    print(json.dumps(response, indent=4))

    return formatResponse(response)

### Helper methods ###

def getRelevantDocuments(prompt: str):
    retrieved_docs = requests.post(
        "https://milvus-api-v3-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
        json={"query": prompt}
    )

    if retrieved_docs.json() != [[]]:
        return retrieved_docs.json()[0][0]['entity']['text']

def formatResponse(response):
    return response.split("Answer: ")[1].strip()