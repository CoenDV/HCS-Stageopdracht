CREATE TABLE frontend_logs (
    correlation_id varchar(36) NOT NULL, -- UUID length of python uuid
    time time NOT NULL,
    url varchar(255) NOT NULL
);

CREATE TABLE backend_logs (
    correlation_id varchar(36) NOT NULL, -- UUID length of python uuid
    retrieved_document_id int,
    similarity_score float,
    time time NOT NULL,
    url varchar(255) NOT NULL
);

CREATE TABLE llm_logs (
    correlation_id varchar(36) NOT NULL, -- UUID length of python uuid
    without_RAG_answer varchar(255) NOT NULL,
    without_RAG_duration time NOT NULL,
    with_RAG_answer varchar(255) NOT NULL,
    with_RAG_duration time NOT NULL,
    url varchar(255) NOT NULL
);