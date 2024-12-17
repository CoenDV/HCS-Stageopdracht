CREATE DATABASE logs;
\c logs;

CREATE TABLE frontend_logs (
    correlation_id varchar(36) NOT NULL,
    prompt varchar(255) NOT NULL,
    time time NOT NULL,
    url varchar(255) NOT NULL
);

CREATE TABLE backend_logs (
    correlation_id varchar(36) NOT NULL,
    retrieved_documents TEXT,
    similarity_score float,
    time time NOT NULL,
    url varchar(255) NOT NULL
);

CREATE TABLE llm_without_RAG_logs (
    correlation_id varchar(36) NOT NULL,
    without_RAG_answer TEXT NOT NULL,
    without_RAG_duration time NOT NULL,
    model varchar(255) NOT NULL,
    url varchar(255) NOT NULL
);

CREATE TABLE llm_with_RAG_logs (
    correlation_id varchar(36) NOT NULL,
    with_RAG_answer TEXT NOT NULL,
    with_RAG_duration time NOT NULL,
    model varchar(255) NOT NULL,
    url varchar(255) NOT NULL
);

ALTER TABLE frontend_logs OWNER TO hcsuser;
ALTER TABLE backend_logs OWNER TO hcsuser;
ALTER TABLE llm_without_RAG_logs OWNER TO hcsuser;
ALTER TABLE llm_with_RAG_logs OWNER TO hcsuser;