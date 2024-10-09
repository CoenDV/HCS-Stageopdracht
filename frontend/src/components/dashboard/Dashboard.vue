<script>
export default {
    name: "Dashboard",
    setup() {

    },
    data() {
        return {

        }
    }
};
</script>

<template>
    <div class="container-fluid p-0">
        <img src="/images/header.png" class="img-fluid w-100">
        <img src="/images/decoration.png" class="img-fluid position-absolute bottom-0 start-0 m-5">

        <div class="position-absolute top-50 start-50 translate-middle col-10">
            <h1 class="display-1 text-center text-light">Welkom bij de HCS-Verzekeringen Demo</h1>
            <p class="lead text-center text-light">Deze demo applicatie toont de voordelen van een AI chatbot dat gebruik maakt van het RAG methodiek</p>
            <div class="row justify-content-center">
                <RouterLink to="/available-documents" type="button" class="btn btn-square-md mx-4 row">
                    <img src="/images/file-multiple.png" alt="file-multiple" class="img-fluid col-6 mt-5">
                    <h6> Beschikbare Documenten </h6>
                </RouterLink>

                <RouterLink to="/account" type="button" class="btn btn-square-md mx-4 row">
                    <img src="/images/user-profile.png" alt="file-multiple" class="img-fluid col-6 mt-5">
                    <h6> Account </h6>
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<style scoped></style>