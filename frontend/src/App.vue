<script>

import Navigation from "./components/Navigation.vue";
import { userStore } from "./stores/userstore";

export default {
  name: "App",
  components: {
    Navigation
  },
  setup() {
    const store = userStore();
    store.autoLogin();
  },
};
</script>

<template>
  <Navigation />
  <routerView> </routerView>
</template>

<style scoped></style>
