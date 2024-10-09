<script>
export default {
    name: "CarInfo",
    setup() {

    },
    data() {
        return {

        }
    }
};
</script>

<template>
    <!-- Car(s) Info-->
    <div class="card m-5">
        <div class="card-body">
            <h4 class="card-title"> 1. Car Info: </h4>
            <div class="row">
                <div class="col mb-3">
                    <label for="merk" class="form-label">Merk: </label>
                    <input type="text" class="form-control" id="merk">
                </div>
                <div class="col mb-3">
                    <label for="model" class="form-label">Model: </label>
                    <input type="text" class="form-control" id="model">
                </div>
            </div>
            <div class="row">
                <div class="col mb-3">
                    <label for="bouwjaar" class="form-label">Bouwjaar: </label>
                    <input type="text" class="form-control" id="bouwjaar">
                </div>
                <div class="col mb-3">
                    <label for="kenteken" class="form-label">Kenteken: </label>
                    <input type="text" class="form-control" id="kenteken">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>