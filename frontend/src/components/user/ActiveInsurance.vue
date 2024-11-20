<script>
export default {
    name: "ActiveInsurance",
    props: {
        insurance: {
            type: Object,
            required: true
        }
    },
    mounted() {
        console.log(this.insurance);
    }
};
</script>

<template>
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                :data-bs-target="'#panelsStayOpen-' + insurance.id" aria-expanded="false"
                :aria-controls="'panelsStayOpen-' + insurance.id">
                <h5 class="card-title">{{ insurance.id }}. {{ insurance.insurance_policy.title }} {{ insurance.car.licenseplate }}</h5>
            </button>
        </h2>
        <div :id="'panelsStayOpen-' + insurance.id" class="accordion-collapse collapse">
            <div class="accordion-body">
                <div class="row">
                    <div class="col mb-3">
                        <label for="insurance" class="form-label">Insurance: </label>
                        <input type="text" class="form-control" id="insurance" :value="insurance.insurance_policy.title" disabled>
                    </div>
                </div>
                <div class="row">
                    <div class="col mb-3">
                        <label for="insurance" class="form-label">Start date: </label>
                        <input type="text" class="form-control" id="insurance" :value="insurance.date_start" disabled>
                    </div>
                    <div class="col mb-3">
                        <label for="insuranceType" class="form-label">Price per month: </label>
                        <input type="text" class="form-control" id="insuranceType" :value="insurance.price_per_month" disabled>
                    </div>
                </div>
                <div class="col mb-3">
                    <label for="summary" class="form-label">Summary: </label>
                    <textarea type="text" class="form-control" id="insuranceCompany" rows="3">
                        {{ insurance.insurance_policy.content }}
                    </textarea>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>