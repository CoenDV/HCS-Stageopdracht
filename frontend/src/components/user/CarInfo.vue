<script>
export default {
    name: "CarInfo",
    props: {
        car: {
            type: Object,
            required: true
        }
    },
    mounted() {
        console.log(this.car);
    }
};
</script>

<template>
    <!-- Car(s) Info-->
    <div class="card m-5">
        <div class="card-body">
            <h4 class="card-title"> Car Info: </h4>
            <div class="row">
                <div class="col mb-3">
                    <label for="merk" class="form-label">Merk: </label>
                    <input type="text" class="form-control" id="merk" :value="car.brand" disabled>
                </div>
                <div class="col mb-3">
                    <label for="model" class="form-label">Model: </label>
                    <input type="text" class="form-control" id="model" :value="car.model" disabled>
                </div>
            </div>
            <div class="row">
                <div class="col mb-3">
                    <label for="bouwjaar" class="form-label">Bouwjaar: </label>
                    <input type="text" class="form-control" id="bouwjaar" :value="car.year" disabled>
                </div>
                <div class="col mb-3">
                    <label for="kenteken" class="form-label">Kenteken: </label>
                    <input type="text" class="form-control" id="kenteken" :value="car.licenseplate" disabled>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>