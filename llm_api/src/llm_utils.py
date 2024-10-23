import requests
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_community.llms import LlamaCpp
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

class HCSInsuranceAssistant:
    def __init__(self, model_path: str):
        # System prompt
        self.system_prompt = SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant for HCS-Company car insurance. "
            "Use the provided context to answer the question, if you don't know the answer, say so. "
            "Keep the answer concise with a maximum of 5 sentences. "
            "Answer the question based on the context: {context}. "
            "If you are greeted, respond with a greeting. "
        )

        # Chat history
        self.chat_history = InMemoryChatMessageHistory()

        # Human prompt
        self.human_prompt = HumanMessagePromptTemplate.from_template(
            "{question} Answer: "
        )

        # Chat template
        self.prompt = ChatPromptTemplate.from_messages(
            [
                self.system_prompt,
                ("placeholder", "{history}"),
                self.human_prompt
            ]
        )

        # AI Model
        self.llm = LlamaCpp(
            model_path=model_path,
            max_tokens=150,         # max tokens: the maximum number of tokens that the model can generate
            n_ctx=2048,             # context length: decides the maximum number of tokens that can be processed by the model
            temperature=0.4         # temperature: controls the creativity of the model
        )

        # Chain
        self.chain = self.prompt | self.llm

        # Chain with message history
        self.chain_with_message_history = RunnableWithMessageHistory(
            self.chain,
            lambda session_id: self.chat_history,
            input_messages_key="question",
            history_messages_key="history",
)

    def generate_response(self, question: str) -> str:
        retrieved_docs = self.get_relevant_documents(question)

        response = self.chain_with_message_history.invoke(
            { "context": retrieved_docs, "question": question },
            config= { "session_id": "1" }
            )
        print("Response: \n", self.chat_history)

        return self.return_json(question, response)

    def get_relevant_documents(self, prompt: str):
        retrieved_docs = requests.post(
            "https://milvus-api-v3-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/search/",
            json={"query": prompt}
        )

        if retrieved_docs.json() != [[]]:
            return retrieved_docs.json()[0][0]['entity']['text']
        return ""
    
    def return_json(self, question: str, answer: str):
        return {
            "question": question,
            "answer": answer,
            "metadata": {
                "source": "HCS-Insurance-Assistant",
                "model": "granite-7b-lab-Q4_K_M.gguf",
                "status": "success"
            }
        }