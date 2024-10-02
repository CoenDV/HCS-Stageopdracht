<script>
import axios from 'axios';

export default {
  name: 'App',
  components: {},
  data() {
    return {
      msg: 'Welcome to Red Hat AI Chatbot',
      question: '',
      aiMsg: '',
    };
  },
  mounted() {
    this.getBackendMessage();
  },
  methods: {
    getBackendMessage() {
      axios.get("https://openshift-test-git-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/api/")
        .then(response => {
          this.msg = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

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
    <p class="text-center">{{ msg }}</p>

    <h1>Ask a question: </h1>
    <input type="text" class="form-control m-1" v-model="question" />
    <button @click="askQuestion" class="btn btn-primary">Ask</button>
    <h1>AI response:</h1>
    <p>{{ aiMsg }}</p>
  </main>
</template>

<style scoped></style>
