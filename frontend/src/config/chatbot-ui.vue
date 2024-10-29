<script>
import axios from 'axios';

export default {
    name: "ChatbotUi",
    data() {
        return {
            temporary_question: '',
            answerGenerating: false,

            messageHistory: []
        }
    },
    methods: {
        askQuestion() {
            this.answerGenerating = true;
            this.temporary_question = document.getElementById('question').value;
            document.getElementById('question').value = '';

            axios.post("https://saved-ferret-rapid.ngrok-free.app/generate/",
                {
                    "prompt": this.temporary_question
                }
            )
                .then(response => {
                    this.answerGenerating = false;

                    const result = response.data.response;
                    console.log(result);

                    this.messageHistory.push({
                        question: result.question,
                        answer: result.answer
                    });
                })
                .catch(error => {
                    console.log(error);
                    this.messageHistory.push({
                        question: this.temporary_question,
                        answer: result.answer
                    });
                    this.answerGenerating = false;
                });
        }
    }
};
</script>

<template>
    <button class="position-absolute bottom-0 end-0 m-5" data-bs-toggle="modal" data-bs-target="#exampleModal"
        style="background-color: transparent; border-color: transparent;"><img src="/images/chatbotButton.svg"
            class="img-fluid"></button>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">HCS-Chatbot</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p class="row col-10 p-2 messageBot rounded">Welkom bij de HCS-Chatbot. Hoe kan ik u helpen?</p>

                    <div v-for="message in messageHistory">
                        <p class="row col-10 p-2 messageUser rounded float-end">
                            {{ message.question }}
                        </p>

                        <p class="row col-10 p-2 messageBot rounded">
                            {{ message.answer }}
                        </p>
                    </div>
                    <div v-if="answerGenerating">
                        <p class="row col-10 p-2 messageUser rounded float-end">
                            {{ temporary_question }}
                        </p>
                        <div class="spinner-border mt-5"></div>
                    </div>
                </div>
                <div class="modal-footer">
                    <input id="question" type="text" class="form-control col" placeholder="Type your message here">
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