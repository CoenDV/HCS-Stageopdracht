import axios from './../config/axios-auth'

export const userStore = defineStore('store', {
    state: () => ({
        user: '',
        username: ''
    }),
    getters: {
        isLoggedIn: (state) => state.user !== null,
    },
    actions: {
        login(username) {
            return new Promise((resolve, reject) => {
                axios
                    .post("/login", { username: username })
                    .then(response => {
                        this.username = username
                        if (response.data.username == this.username) {
                            this.user = response.data
                            resolve();
                            localStorage.setItem("user", JSON.stringify(this.user))
                        }
                        else {
                            reject("Invalid username")
                        }
                    })
                    .catch((error) => reject(error));
            }
            )
        },
        autoLogin() {
            const user = localStorage.getItem("user")

            if (user) {
                this.user = JSON.parse(user);
            }
        }
    },
}
)