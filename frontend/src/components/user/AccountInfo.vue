<script>
export default {
    name: "AccountInfo",
    data() {
        return {
            user: JSON.parse(localStorage.getItem('user')),
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
                    <input type="text" class="form-control" id="gebruikesnaam" :value="user.username" disabled>
                </div>
            </div>
            <div class="row">
                <div class="col mb-3">
                    <label for="voornaam" class="form-label">Voornaam: </label>
                    <input type="text" class="form-control" id="voornaam" :value="user.firstname" disabled>
                </div>
                <div class="col mb-3">
                    <label for="achternaam" class="form-label">Achternaam: </label>
                    <input type="text" class="form-control" id="achternaam" :value="user.lastname" disabled>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>