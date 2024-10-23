import { defineStore } from 'pinia'
import axios from './../config/axios-auth'

export const userStore = defineStore('store', {
    state: () => ({
        username: ''
    }),
    getters: {
        isLoggedIn: (state) => state.username !== '',
    },
    actions: {
        login(username, password) {
            return new Promise((resolve, reject) => {
                this.user = {
                    username: username,
                    password: password
                }
                axios
                    .post("customers/login", this.user)
                    .then(response => {

                        this.username = response.data.username;
                        resolve();

                        if (this.user != "") {
                            localStorage.setItem("username", JSON.stringify(this.username))
                            localStorage.setItem("user", JSON.stringify(response.data))
                        }
                    })
                    .catch((error) => reject(error));
            }
            )
        },
        autoLogin() {
            const username = localStorage.getItem("username")

            if (username) {
                this.username = JSON.parse(username)
            }
        },
        logout() {
            this.username = '';
            localStorage.removeItem("username");
            localStorage.removeItem("user");
        }
    },
}
)