<script>
import axios from 'axios';

export default {
    name: "ChatbotUi",
    data() {
        return {
            question: '',
            answer: '',
            answerGenerating: false
        }
    },
    methods: {
        askQuestion() {
            this.answerGenerating = true;
            this.question = document.getElementById('question').value;
            this.answer = '';
            document.getElementById('question').value = '';

            axios.post("https://saved-ferret-rapid.ngrok-free.app/generate/",
                {
                    "prompt": this.question
                }
            )
                .then(response => {
                    console.log(response.data);
                    this.answer = response.data.response;
                    this.answerGenerating = false;
                })
                .catch(error => {
                    console.log(error);
                    this.answer = 'Sorry, something went wrong. Please try again later.';
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
                    <p class="col-10 text-center">Welkom bij de HCS-Chatbot. Hoe kan ik u helpen?</p>
                    <p v-if="question != ''" class="row col-10 p-2 bg-primary rounded float-end">
                        {{ question }}
                    </p>

                    <p v-if="answer != ''" class="row col-10 p-2 bg-secondary-subtle rounded">
                        {{ answer }}
                    </p>
                    <div v-if="answerGenerating" class="spinner-border mt-5"></div>
                </div>
                <div class="modal-footer">
                    <input id="question" type="text" class="form-control col"
                        placeholder="Type your message here">
                    <button type="button" @click="askQuestion()" class="btn btn-primary col-4">Send Message</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>