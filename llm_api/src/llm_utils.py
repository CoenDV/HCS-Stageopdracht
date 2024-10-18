import requests
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_community.llms import LlamaCpp

class HCSInsuranceAssistant:
    def __init__(self, model_path: str):
        self.system_prompt = SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant for HCS-Company car insurance. "
            "Use the provided context to answer the question. "
            "Keep the answer concise with a maximum of 5 sentences. "
            "Answer the question based on the context: {context}. "
            "If you are greeted, respond with a greeting. "
        )

        self.human_prompt = HumanMessagePromptTemplate.from_template(
            "{question} Answer: "
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                self.system_prompt, 
                self.human_prompt
            ]
        )

        self.llm = LlamaCpp(
            model_path=model_path,
            max_tokens=150,
            temperature=0.4
        )

        self.chain = self.prompt | self.llm

    def generate_response(self, question: str) -> str:
        retrieved_docs = self.get_relevant_documents(question)

        # Prepare input for the chain
        response = self.chain.invoke({
            "context": retrieved_docs,
            "question": question
        })
        print(response)

        return response

    def get_relevant_documents(self, prompt: str):
        retrieved_docs = requests.post(
            "https://milvus-api-v3-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
            json={"query": prompt}
        )

        if retrieved_docs.json() != [[]]:
            return retrieved_docs.json()[0][0]['entity']['text']
        return ""