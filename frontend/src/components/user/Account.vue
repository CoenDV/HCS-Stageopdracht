<script>
import ChatbotUi from '@/config/chatbot-ui.vue';
import AccountInfo from './AccountInfo.vue';
import ActiveInsurance from './ActiveInsurance.vue';
import CarInfo from './CarInfo.vue';

export default {
    name: "AvailableDocuments",
    components: {
        AccountInfo,
        CarInfo,
        ActiveInsurance,
        ChatbotUi
    },
    setup() {

    },
    data() {
        return {
            
        }
    },
    methods: {
        
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

                <CarInfo />
                <CarInfo />
            </div>

            <div class="col-8">
                <ActiveInsurance />
            </div>
        </div>
    </div>
</template>

<style scoped></style>