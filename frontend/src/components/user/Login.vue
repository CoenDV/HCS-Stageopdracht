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
    <img src="/images/decoration.png" class="img-fluid position-absolute bottom-0 start-0 m-5">

    <div class="container d-flex justify-content-center vh-100 align-items-center">
        <form class="card col-3 p-3 py-5">
            <img src="/images/user-profile-black.svg" class="img-fluid col-3 mx-auto mb-3">

            <div class="col mb-3">
                <label for="gebruikersnaam" class="form-label">Gebruikersnaam: </label>
                <input type="text" class="form-control" id="gebruikesnaam">
            </div>
            <div class="col mb-3">
                <label for="wachtwoord" class="form-label">Wachtwoord: </label>
                <input type="password" class="form-control" id="wachtwoord">
            </div>

            <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
        </form>
    </div>
</template>

<style scoped></style>