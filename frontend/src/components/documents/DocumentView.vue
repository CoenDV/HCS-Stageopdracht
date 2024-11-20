<script>
export default {
    name: "AvailableDocuments",
    components: {

    },
    setup() {

    },
    data() {
        return {

        }
    },
    methods: {

    },
    mounted() {
        console.log(this.document);
    },
    props: {
        document: {
            type: Object,
            required: true
        }
    }
};
</script>

<template>
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                :data-bs-target="'#panelsStayOpen-' + this.document.id" aria-expanded="false"
                :aria-controls="'panelsStayOpen-' + this.document.id">
                <h5 class="card-title">{{ this.document.title }}</h5>
            </button>
        </h2>
        <div :id="'panelsStayOpen-' + this.document.id" class="accordion-collapse collapse">
            <div class="accordion-body">
                {{ this.document.content }}
            </div>
        </div>
    </div>
</template>

<style scoped></style>