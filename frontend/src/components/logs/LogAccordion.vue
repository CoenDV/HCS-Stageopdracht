<script>
export default {
    name: "LogAccordion",
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

    },
    props: {
        log: {
            type: Object,
            required: true
        }
    }
};
</script>

<template>
    <div class="accordion-item z-3">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse"
                :data-bs-target="'#panelsStayOpen-' + this.log.correlation_id" aria-expanded="false"
                :aria-controls="'panelsStayOpen-' + this.log.correlation_id">
                <h5 class="card-title"> Log: {{ this.log.correlation_id }}</h5>
            </button>
        </h2>
        <div :id="'panelsStayOpen-' + this.log.correlation_id" class="accordion-collapse collapse">
            <div class="accordion-body">
                <h3> Frontend: </h3>
                <hr>
                <div class="row">
                    <div class="col mb-3">
                        <label for="merk" class="form-label">Tijd gestart: </label>
                        <input type="text" class="form-control" id="merk" :value="log.frontend_log.time" disabled>
                    </div>
                    <div class="col mb-3">
                        <label for="model" class="form-label">Url: </label>
                        <input type="text" class="form-control" id="model" :value="log.frontend_log.url" disabled>
                    </div>
                </div>

                <h3> Backend: </h3>
                <hr>
                <div class="row">
                    <div class="col mb-3">
                        <label for="merk" class="form-label">Context: </label>
                        <input type="text" class="form-control" id="merk" :value="log.backend_log.retrieved_document_id"
                            disabled>
                    </div>
                    <div class="col mb-3">
                        <label for="model" class="form-label">Relevantie Score: </label>
                        <input type="text" class="form-control" id="model" :value="log.backend_log.similarity_score"
                            disabled>
                    </div>
                </div>
                <div class="row">
                    <div class="col mb-3">
                        <label for="merk" class="form-label">Tijd gestart: </label>
                        <input type="text" class="form-control" id="merk" :value="log.backend_log.time" disabled>
                    </div>
                    <div class="col mb-3">
                        <label for="model" class="form-label">Url: </label>
                        <input type="text" class="form-control" id="model" :value="log.backend_log.url" disabled>
                    </div>
                </div>

                <h3> LLM: </h3>
                <hr>
                <div class="row">
                    <div class="col-9 mb-3">
                        <label for="merk" class="form-label">Antwoord met Context: </label>
                        <textarea type="text" class="form-control" id="merk" :value="log.llm_log.with_rag_answer"
                            disabled rows="5"> </textarea>
                    </div>
                    <div class="col mb-3">
                        <label for="model" class="form-label">Tijd met Context: </label>
                        <input type="text" class="form-control" id="model" :value="log.llm_log.with_rag_duration"
                            disabled>
                    </div>
                </div>
                <div class="row">
                    <div class="col-9 mb-3">
                        <label for="merk" class="form-label">Antwoord zonder Context: </label>
                        <textarea type="text" class="form-control" id="merk" :value="log.llm_log.without_rag_answer"
                            disabled rows="5"> </textarea>
                    </div>
                    <div class="col mb-3">
                        <label for="model" class="form-label">Tijd zonder Context: </label>
                        <input type="text" class="form-control" id="model" :value="log.llm_log.without_rag_duration"
                            disabled>
                    </div>
                </div>
                <div class="row">
                    <div class="col mb-3">
                        <label for="model" class="form-label">Url: </label>
                        <input type="text" class="form-control" id="model" :value="log.llm_log.url" disabled>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>