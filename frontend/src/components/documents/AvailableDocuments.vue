<script>
import ChatbotUi from '@/config/chatbot-ui.vue';
import axios from './../../config/axios-auth';
import DocumentView from './DocumentView.vue';

export default {
    name: "AvailableDocuments",
    components: {
        ChatbotUi,
        DocumentView
    },
    setup() {

    },
    data() {
        return {
            documents: []
        }
    },
    methods: {
        getDocuments() {
            axios.get('/insurance_policies')
                .then(response => {
                    this.documents = response.data;
                    console.log(this.documents);
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
        <img src="/images/decoration.png" class="img-fluid position-absolute bottom-0 start-0 m-5">

        <div class="accordion col-8 mt-5 z-3" id="accordionPanelsStayOpenExample">
            <DocumentView v-for="document in documents" :document="document" />
        </div>

    </div>
</template>

<style scoped></style>