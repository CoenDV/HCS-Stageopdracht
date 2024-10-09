<script>
import { RouterView } from 'vue-router';
import Navigation from './components/Navigation.vue';

export default {
  name: 'App',
  components: {
    Navigation
  },
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
  <Navigation />
  <RouterView />
</template>

<style scoped></style>