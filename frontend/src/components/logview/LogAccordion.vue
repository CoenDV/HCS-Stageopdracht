<script>
export default {
    name: "LogAccordion",
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
            <div class="accordion-body row justify-content-center">
                <!-- Frontend -->
                <div class="col-12 d-flex justify-content-center">
                    <table v-if="!log.frontend_log.url" class="table table-bordered table-striped table-hover mx-5"
                        style="width: 40%;">
                        <thead>
                            <tr>
                                <th>Frontend</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Geen Logs gevonden... </td>
                            </tr>
                        </tbody>
                    </table>

                    <table v-else class="table table-bordered table-striped table-hover " style="width:40%;">
                        <thead>
                            <tr>
                                <th scope="col"></th>
                                <th>Frontend</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Prompt</td>
                                <td>{{ log.frontend_log.prompt }}</td>
                            </tr>
                            <tr>
                                <td>Tijd</td>
                                <td>{{ log.frontend_log.time }}</td>
                            </tr>
                            <tr>
                                <td>Bron</td>
                                <td class="text-primary">{{ log.frontend_log.url }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor"
                    class="bi bi-arrow-down-left w-25 m-3" viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M2 13.5a.5.5 0 0 0 .5.5h6a.5.5 0 0 0 0-1H3.707L13.854 2.854a.5.5 0 0 0-.708-.708L3 12.293V7.5a.5.5 0 0 0-1 0z" />
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor"
                    class="bi bi-arrow-down-right w-25 m-3" viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M14 13.5a.5.5 0 0 1-.5.5h-6a.5.5 0 0 1 0-1h4.793L2.146 2.854a.5.5 0 1 1 .708-.708L13 12.293V7.5a.5.5 0 0 1 1 0z" />
                </svg>

                <!-- LLM without RAG -->
                <table v-if="!log.llm_without_rag_log.url" class="table table-bordered table-striped table-hover mx-5"
                    style="width: 40%;">
                    <thead>
                        <tr>
                            <th>LLM zonder RAG</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Geen Logs gevonden... </td>
                        </tr>
                    </tbody>
                </table>

                <table v-else class="table table-bordered table-striped table-hover mx-5" style="width: 40%;">
                    <thead>
                        <tr>
                            <th scope="col"></th>
                            <th>LLM zonder RAG</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Antwoord zonder context</td>
                            <td>{{ log.llm_without_rag_log.without_rag_answer }}</td>
                        </tr>
                        <tr>
                            <td>Tijd zonder context</td>
                            <td>{{ log.llm_without_rag_log.without_rag_duration }}</td>
                        </tr>
                        <tr>
                            <td>Model</td>
                            <td>{{ log.llm_without_rag_log.model }}</td>
                        </tr>
                        <tr>
                            <td>Bron</td>
                            <td class="text-primary">{{ log.llm_without_rag_log.url }}</td>
                        </tr>
                    </tbody>
                </table>

                <!-- LLM with RAG -->
                <table v-if="!log.llm_with_rag_log.url" class="table table-bordered table-striped table-hover mx-5"
                    style="width: 40%;">
                    <thead>
                        <tr>
                            <th>LLM met RAG</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Geen Logs gevonden... </td>
                        </tr>
                    </tbody>
                </table>

                <table v-else class="table table-bordered table-striped table-hover mx-5" style="width: 40%;">
                    <thead>
                        <tr>
                            <th scope="col"></th>
                            <th>LLM met RAG</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Antwoord met context</td>
                            <td>{{ log.llm_with_rag_log.with_rag_answer }}</td>
                        </tr>
                        <tr>
                            <td>Tijd met context</td>
                            <td>{{ log.llm_with_rag_log.with_rag_duration }}</td>
                        </tr>
                        <tr>
                            <td>Model</td>
                            <td>{{ log.llm_with_rag_log.model }}</td>
                        </tr>
                        <tr>
                            <td>Bron</td>
                            <td class="text-primary">{{ log.llm_with_rag_log.url }}</td>
                        </tr>
                    </tbody>
                </table>

                <div class="col-12">
                    <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor"
                        class="bi bi-arrow-down mt-3 col-6 float-end" viewBox="0 0 16 16">
                        <path fill-rule="evenodd"
                            d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1" />
                    </svg>
                </div>

                <!-- Backend -->
                <div class="col-12 p-5">
                    <table v-if="!log.backend_log.url"
                        class="table table-bordered table-striped table-hover mx-5 float-end" style="width: 40%;">
                        <thead>
                            <tr>
                                <th>Backend</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Geen Logs gevonden... </td>
                            </tr>
                        </tbody>
                    </table>

                    <table v-else class="table table-bordered table-striped table-hover col-12 float-end me-5"
                        style="width:42%;">
                        <thead>
                            <tr>
                                <th scope="col"></th>
                                <th>Backend</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Context</td>
                                <td>
                                    <textarea class="form-control"
                                        rows="10">{{ log.backend_log.retrieved_documents }}</textarea>
                                </td>
                            </tr>
                            <tr>
                                <td>Relevantie Score</td>
                                <td>{{ log.backend_log.similarity_score }}</td>
                            </tr>
                            <tr>
                                <td>Tijd</td>
                                <td>{{ log.backend_log.time }}</td>
                            </tr>
                            <tr>
                                <td>Bron</td>
                                <td class="text-primary">{{ log.backend_log.url }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>