<script>
import axios from 'axios';

export default {
  name: 'App',
  components: {},
  data() {
    return {
      question: '',
      aiMsg: '',
    };
  },
  mounted() {
    
  },
  methods: {
    askQuestion() {
      axios.post("https://saved-ferret-rapid.ngrok-free.app/generate/",
        {
          "prompt": this.question
        }
      )
        .then(response => {
          console.log(response.data);
          this.aiMsg = response.data.response[0].message.content;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
}
</script>

<template>
  <main class="d-flex justify-content-center row col-3">
    <img alt="red hat Logo" src="/images/redhat.webp" class="img-fluid">
    <p class="text-center">Welcome to Red Hat AI Chatbot</p>

    <h1>Ask a question: </h1>
    <input type="text" class="form-control m-1" v-model="question" />
    <button @click="askQuestion" class="btn btn-primary">Ask</button>
    <h1>AI response:</h1>
    <p>{{ aiMsg }}</p>
  </main>
</template>

<style scoped></style>