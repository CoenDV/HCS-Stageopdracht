from src.logrepository import Repository
from models import Frontend_log, Backend_log, Llm_log

import time

class LogService:
    def get_all_logs():
        frontend_logs = Repository.get_all_frontend_logs()
        backend_logs = Repository.get_all_backend_logs()
        llm_logs = Repository.get_all_llm_logs()

        return LogService.format_logs(frontend_logs, backend_logs, llm_logs)
    
    def get_all_frontend_logs():
        return Repository.get_all()
    
    def save_frontend_log(frontend_log):
        frontend_log = Frontend_log(
            correlation_id=frontend_log["correlation_id"],
            time=frontend_log["time"],
            url=frontend_log["url"],
        )
        return Repository.save_frontend_log(frontend_log)
    
    def get_all_backend_logs():
        return Repository.get_all()
    
    def save_backend_log(backend_log):
        docs = []
        for doc in backend_log["retrieved_documents"]:
            docs.append(
                "title: " + doc["title"] + "content: " + doc["content"]
            )

        backend_log = Backend_log(
            correlation_id=backend_log["correlation_id"],
            retrieved_documents=docs,
            similarity_score=backend_log["similarity_score"],
            time=backend_log["time"],
            url=backend_log["url"],
        )
        return Repository.save_backend_log(backend_log)
    
    def get_all_llm_logs():
        return Repository.get_all()
    
    def save_llm_log(llm_log):
        llm_log = Llm_log(
            correlation_id=llm_log["correlation_id"],
            without_rag_answer=llm_log["without_rag_answer"],
            without_rag_duration=llm_log["without_rag_duration"],
            with_rag_answer=llm_log["with_rag_answer"],
            with_rag_duration=llm_log["with_rag_duration"],
            url=llm_log["url"],
        )
        return Repository.save_llm_log(llm_log)
    
    def format_logs(frontend_logs, backend_logs, llm_logs):
        logs = []
        for frontend_log in frontend_logs:
            for backend_log in backend_logs:
                for llm_log in llm_logs:
                    if frontend_log.correlation_id == backend_log.correlation_id == llm_log.correlation_id:
                        logs.append({
                            "correlation_id": frontend_log.correlation_id,
                            "frontend_log": frontend_log.to_dict(),
                            "backend_log": backend_log.to_dict(),
                            "llm_log": llm_log.to_dict()
                        })

        return logs