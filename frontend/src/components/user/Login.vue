<script>
import { userStore } from './../../stores/userstore';
import router from '@/config/router';
import { errorMessages } from 'vue/compiler-sfc';

export default {
    name: "Login",
    setup() {
        const store = userStore();
        return { store };
    },
    data() {
        return {
            username: null,
            password: null,
            errorMessage: "",
        }
    },
    methods: {
        login(username, password) {
            this.store.login(username, password)
                .then(() => {
                        router.push('/dashboard');
                })
                .catch(error => {
                    this.errorMessage = error.response.data.error;
                });
        }
    }
};
</script>

<template>
    <img src="/images/decoration.png" class="img-fluid position-absolute bottom-0 start-0 m-5">

    <div class="container d-flex justify-content-center vh-100 align-items-center">
        <!-- Error message -->
        <div class="alert alert-danger" role="alert" v-if="this.errorMessage != ''">
            {{ this.errorMessage }}
        </div>

        <!-- Login form -->
        <form class="card col-3 p-3 py-5">
            <img src="/images/user-profile-black.svg" class="img-fluid col-3 mx-auto mb-3">

            <div class="col mb-3">
                <label for="gebruikersnaam" class="form-label">Gebruikersnaam: </label>
                <input v-model="username" type="text" class="form-control" id="gebruikesnaam">
            </div>
            <div class="col mb-3">
                <label for="wachtwoord" class="form-label">Wachtwoord: </label>
                <input v-model="password" type="password" class="form-control" id="wachtwoord">
            </div>

            <button class="btn btn-primary w-100 py-2" type="button" @click="login(username, password)">Sign in</button>
        </form>
    </div>
</template>

<style scoped></style>