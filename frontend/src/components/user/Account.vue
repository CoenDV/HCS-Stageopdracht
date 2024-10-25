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
            cars: [],
            insurances: []
        }
    },
    mounted() {
        console.log(this.user);
        this.insurances = this.getInsurancesFromUser();
    },
    methods: {
        getInsurancesFromUser() {
            axios.get("/customer_policies/" + this.user.id)
                .then(response => {
                    console.log(response.data);
                    this.insurances = response.data;
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

                <CarInfo v-for="insurance in insurances" v-bind:car="insurance.car" />
            </div>

            <div class="col-8">
                <div class="accordion col-11 mt-5" id="accordionPanelsStayOpenExample">
                    <ActiveInsurance v-for="insurance in insurances" v-bind:insurance="insurance" />
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>