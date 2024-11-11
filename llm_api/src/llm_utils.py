import requests
import json
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_community.llms import LlamaCpp
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

class HCSInsuranceAssistant:
    def __init__(self, model_path: str):
        # System prompts
        self.system_prompt = SystemMessagePromptTemplate.from_template(
            "Je bent een assistent voor HCS-Company autoverzekeringen. Beantwoord klantvragen over autoverzekeringen zonder extra labels zoals System: of AI:. Geef directe antwoorden op basis van de context en vraag om verduidelijking als dat nodig is. Antwoorden moeten altijd in het Nederlands zijn."
            "Context: {context}"
        )

        self.system_prompt_without_RAG = SystemMessagePromptTemplate.from_template(
            "Je bent een assistent voor HCS-Company autoverzekeringen. Beantwoord klantvragen over autoverzekeringen zonder extra labels zoals System: of AI:. Geef directe antwoorden op basis van de context en vraag om verduidelijking als dat nodig is. Antwoorden moeten altijd in het Nederlands zijn."
        )

        # Chat history
        self.chat_history = InMemoryChatMessageHistory()

        # Human prompt
        self.human_prompt = HumanMessagePromptTemplate.from_template(
            "Vraag: {question} "
            "Antwoord: "
        )

        # Chat templates
        self.prompt = ChatPromptTemplate.from_messages(
            [
                self.system_prompt,
                ("placeholder", "{history}"),
                self.human_prompt
            ]
        )

        self.prompt_without_RAG = ChatPromptTemplate.from_messages(
            [
                self.system_prompt_without_RAG,
                self.human_prompt
            ]
        )

        # AI Model
        self.llm = LlamaCpp(
            model_path=model_path,
            max_tokens=150,          # max tokens: the maximum number of tokens that the model can generate
            n_ctx=2048,             # context length: decides the maximum number of tokens that can be processed by the model
            temperature=0.0,        # temperature: controls the creativity of the model
            n_gpu_layers= 1024,     # number of layers the GPU uses
            n_batch=128,            # batch size: the number of samples that the model processes at once
        )

        # Chains
        self.chain_without_RAG = self.prompt_without_RAG | self.llm

        # Chain with message history
        self.chain_with_message_history = RunnableWithMessageHistory(
            self.prompt | self.llm,                 # steps in the chain
            lambda session_id: self.chat_history,   # function to get the chat history
            input_messages_key="question",          # what variables to use as input
            history_messages_key="history",         # what variables to use as history
)

    def generate_response(self, question: str) -> str:
        retrieved_docs = self.get_relevant_documents(question)
        print("Retrieved docs: ", json.dumps(retrieved_docs, indent=4))

        response_without_context = self.chain_without_RAG.invoke(input = { "question": question } )
        response = self.chain_with_message_history.invoke(
            { "context": retrieved_docs, "question": question },
            config= { "session_id": "1" }
            )
        
        print("Response: \n", self.chat_history)
        print("Response without context: \n", response_without_context)

        return self.return_json(question, response, response_without_context)

    def get_relevant_documents(self, prompt: str):
        retrieved_docs = requests.post(
            "https://milvus-api-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
            json={"query": prompt}
        )

        if retrieved_docs.json() != [[]]:
            formatted_docs = []
            for doc in retrieved_docs.json()[0]:
                formatted_docs.append(doc['entity']['text'])
            return formatted_docs
        return ""
    
    def return_json(self, question: str, answer: str, answer_without_context: str):
        labels = ["AI:", "System:", "Human:", "Assistant:"]
        for label in labels:
            if label in answer:
                answer = answer.replace(label, "")
            if label in answer_without_context:
                answer_without_context = answer_without_context.replace(label, "")

        return {
            "question": question,
            "answer": answer,
            "answer_without_context": answer_without_context,
            "metadata": {
                "source": "HCS-Insurance-Assistant",
                "model": "granite-7b-lab-Q4_K_M.gguf",
                "status": "success"
            }
        }