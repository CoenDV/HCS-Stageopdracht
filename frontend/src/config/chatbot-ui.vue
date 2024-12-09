<script>
import { uuid } from 'vue-uuid';

export default {
    name: "ChatbotUi",
    data() {
        return {
            temporary_question: '',

            temporary_RAG_question: '',
            temporary_RAG_answer: '',

            temporary_without_RAG_question: '',
            temporary_without_RAG_answer: '',

            messageHistoryRAG: [],
            messageHistoryWithoutRAG: [],

            RagResponse: '',
            WithoutRagResponse: '',
        }
    },
    methods: {
        askQuestion() {
            this.temporary_question = document.getElementById('question').value;
            document.getElementById('question').value = '';

            this.RagResponse = '';
            this.WithoutRagResponse = '';

            const correlation_id = uuid.v4();
            this.logRequest(correlation_id);


            this.getChatbotResponse('https://saved-ferret-rapid.ngrok-free.app/generate-without-RAG/', correlation_id);
            this.getChatbotResponse('https://saved-ferret-rapid.ngrok-free.app/generate-with-RAG/', correlation_id);
        },
        async logRequest(correlation_id) {
            await fetch('https://logger-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/frontend_logs', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    correlation_id: correlation_id,
                    prompt: this.temporary_question,
                    time: new Date().toLocaleTimeString(),
                    url: window.location.href
                })
            })
        },
        async getChatbotResponse(url, correlation_id) {
            try {
                this.temporary_RAG_question = this.temporary_question;
                this.temporary_without_RAG_question = this.temporary_question;

                const response = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        prompt: this.temporary_question,
                        correlation_id: correlation_id
                    })
                })

                this.retrieveChunks(response.body.getReader(), new TextDecoder(), url);

            } catch (error) {
                console.error("Streaming error: ", error);
            }
        },
        async retrieveChunks(reader, decoder, url) {
            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                const chunk = decoder.decode(value, { stream: true });
                if (url === 'https://saved-ferret-rapid.ngrok-free.app/generate-without-RAG/')
                    this.temporary_without_RAG_answer += chunk;
                else
                    this.temporary_RAG_answer += chunk;
            }

            // Wait for the stream to finish before saving the messages
            if (this.temporary_RAG_answer !== '' && this.temporary_without_RAG_answer !== '') {
                this.saveMessages();
            }
        },
        saveMessages() {
            // save messages without RAG
            this.messageHistoryWithoutRAG.push({
                question: this.temporary_question,
                answer: this.temporary_without_RAG_answer
            });
            this.temporary_without_RAG_question = '';
            this.temporary_without_RAG_answer = '';

            // save messages with RAG
            this.messageHistoryRAG.push({
                question: this.temporary_question,
                answer: this.temporary_RAG_answer
            });
            this.temporary_RAG_question = '';
            this.temporary_RAG_answer = '';
        }
    }
};
</script>

<template>
    <button class="position-absolute bottom-0 end-0 m-5 z-3" data-bs-toggle="modal" data-bs-target="#exampleModal"
        style="background-color: transparent; border-color: transparent;"><img src="/images/chatbotButton.svg"
            class="img-fluid"></button>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header d-flex justify-content-center align-items-center">
                    <img src="./../../public/images/favicon.svg" class="img-fluid mx-auto d-block" style="width: 50px;">
                    <button type="button" class="btn-close m-0" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="row border-bottom mb-2">
                        <div class="col-6 border-end">
                            <h3>Chatbot with RAG</h3>
                        </div>
                        <div class="col-6">
                            <h3>Chatbot without RAG</h3>
                        </div>
                    </div>
                    <div class="row">
                        <!-- Chat History RAG -->
                        <div class="col-6 border-end">
                            <div v-for="message in messageHistoryRAG">
                                <p class="row col-10 p-2 messageUser rounded float-end">
                                    {{ message.question }}
                                </p>

                                <p class="row col-10 p-2 messageBot rounded">
                                    {{ message.answer }}
                                </p>
                            </div>
                            <div>
                                <p v-if="temporary_RAG_question != ''"
                                    class="row col-10 p-2 messageUser rounded float-end">
                                    {{ temporary_RAG_question }}
                                </p>
                                <p v-if="temporary_RAG_answer != ''" class="row col-10 p-2 messageBot rounded">
                                    {{ temporary_RAG_answer }}
                                </p>
                            </div>
                        </div>
                        <!-- Chat History without RAG -->
                        <div class="col-6">
                            <div v-for="message in messageHistoryWithoutRAG">
                                <p class="row col-10 p-2 messageUser rounded float-end">
                                    {{ message.question }}
                                </p>

                                <p class="row col-10 p-2 messageBot rounded">
                                    {{ message.answer }}
                                </p>
                            </div>
                            <div>
                                <p v-if="temporary_without_RAG_question != ''"
                                    class="row col-10 p-2 messageUser rounded float-end">
                                    {{ temporary_without_RAG_question }}
                                </p>
                                <p v-if="temporary_without_RAG_answer != ''" class="row col-10 p-2 messageBot rounded">
                                    {{ temporary_without_RAG_answer }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <input id="question" type="text" class="form-control col" placeholder="Type your message here"
                        autofocus>
                    <button type="button" @click="askQuestion()" class="btn btn-primary col-4">Send Message</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.messageUser {
    background-color: #FE0000;
    color: #FFF;
}

.messageBot {
    background-color: #000;
    color: #FFF;
}
</style>