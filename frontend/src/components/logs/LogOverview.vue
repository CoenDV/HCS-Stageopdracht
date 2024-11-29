<script>
import ChatbotUi from '@/config/chatbot-ui.vue';
import axios from './../../config/axios-auth';
import LogAccordion from './LogAccordion.vue';

export default {
    name: "AvailableDocuments",
    components: {
        ChatbotUi,
        LogAccordion
    },
    setup() {

    },
    data() {
        return {
            logs: []
        }
    },
    methods: {
        getDocuments() {
            axios.get('http://logger/logs')
                .then(response => {
                    this.logs = response.data;
                    console.log(this.logs);
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    mounted() {
        this.getDocuments();
    }
};
</script>

<template>
    <ChatbotUi />

    <div class="container-fluid p-0 d-flex justify-content-center">
        <img src="/images/decoration.png" class="img-fluid position-absolute bottom-0 start-0 m-5 z-0">

        <div class="accordion col-8 mt-5 z-3" id="accordionPanelsStayOpenExample">
            <LogAccordion v-for="log in logs" :log="log" />
        </div>

    </div>
</template>

<style scoped></style>