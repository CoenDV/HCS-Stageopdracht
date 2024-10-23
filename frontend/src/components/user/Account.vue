<script>
import ChatbotUi from '@/config/chatbot-ui.vue';
import AccountInfo from './AccountInfo.vue';
import ActiveInsurance from './ActiveInsurance.vue';
import CarInfo from './CarInfo.vue';

import axios from './../../config/axios-auth';

export default {
    name: "AvailableDocuments",
    components: {
        AccountInfo,
        CarInfo,
        ActiveInsurance,
        ChatbotUi
    },
    data() {
        return {
            user: JSON.parse(localStorage.getItem('user')),
            cars: []
        }
    },
    mounted() {
        console.log(this.user);
        this.cars = this.getCarsFromUser();
    },
    methods: {
        getCarsFromUser() {
            axios.get("/customer/cars/" + this.user.username)
                .then(response => {
                    console.log(response.data);
                    this.cars = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    }
};
</script>

<template>
    <div class="container-fluid p-0">
        <img src="/images/decoration.png" class="img-fluid position-absolute bottom-0 start-0 m-5">
        <ChatbotUi />

        <div class="row m-0">

            <div class="col-4">
                <AccountInfo />

                <CarInfo v-for="car in cars" v-bind:car="car" />
            </div>

            <div class="col-8">
                <ActiveInsurance />
            </div>
        </div>
    </div>
</template>

<style scoped></style>