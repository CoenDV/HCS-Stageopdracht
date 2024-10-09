<script>
export default {
    name: "AccountInfo",
    setup() {

    },
    data() {
        return {

        }
    }
};
</script>

<template>
    <!-- Account Info-->
    <div class="card m-5">
        <div class="card-body">
            <h4 class="card-title">Account Info:</h4>
            <div class="row">
                <div class="col mb-3">
                    <label for="gebruikersnaam" class="form-label">Gebruikersnaam: </label>
                    <input type="text" class="form-control" id="gebruikesnaam">
                </div>
                <div class="col mb-3">
                    <label for="wachtwoord" class="form-label">Wachtwoord: </label>
                    <input type="password" class="form-control" id="wachtwoord">
                </div>
            </div>
            <div class="row">
                <div class="col mb-3">
                    <label for="voornaam" class="form-label">Voornaam: </label>
                    <input type="text" class="form-control" id="voornaam">
                </div>
                <div class="col mb-3">
                    <label for="achternaam" class="form-label">Achternaam: </label>
                    <input type="text" class="form-control" id="achternaam">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>