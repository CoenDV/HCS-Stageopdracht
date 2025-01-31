from src.logrepository import Repository
from models import Frontend_log, Backend_log, Llm_with_rag_log, Llm_without_rag_log

class LogService:
    def get_all_logs():
        return LogService.format_logs(
            Repository.get_all_frontend_logs(), 
            Repository.get_all_backend_logs(), 
            Repository.get_all_llm_with_rag_logs(), 
            Repository.get_all_llm_without_rag_logs()
        )
    
    def get_all_frontend_logs():
        return Repository.get_all()
    
    def save_frontend_log(frontend_log):
        frontend_log = Frontend_log(
            correlation_id=frontend_log["correlation_id"],
            prompt=frontend_log["prompt"],
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
    
    def get_all_llm_without_rag_logs():
        return Repository.get_all()
    
    def save_llm_without_rag_log(llm_log):
        llm_log = Llm_without_rag_log(
            correlation_id=llm_log["correlation_id"],
            without_rag_answer=llm_log["without_rag_answer"],
            without_rag_duration=llm_log["without_rag_duration"],
            url=llm_log["url"],
            model=llm_log["model"]
        )
        return Repository.save_llm_without_rag_log(llm_log)
    
    def get_all_llm_with_rag_logs():
        return Repository.get_all()
    
    def save_llm_with_rag_log(llm_log):
        llm_log = Llm_with_rag_log(
            correlation_id=llm_log["correlation_id"],
            with_rag_answer=llm_log["with_rag_answer"],
            with_rag_duration=llm_log["with_rag_duration"],
            url=llm_log["url"],
            model=llm_log["model"]
        )
        return Repository.save_llm_with_rag_log(llm_log)
    
    def format_logs(frontend_logs, backend_logs, llm_with_rag_logs, llm_without_rag_logs):
        logs = []
        for i in range(len(frontend_logs)):
            logs.append({
                "correlation_id": frontend_logs[i].correlation_id,
                "frontend_log": frontend_logs[i].to_dict() if i < len(frontend_logs) else {},
                "backend_log": backend_logs[i].to_dict() if i < len(backend_logs) else {},
                "llm_with_rag_log": llm_with_rag_logs[i].to_dict() if i < len(llm_with_rag_logs) else {},
                "llm_without_rag_log": llm_without_rag_logs[i].to_dict() if i < len(llm_without_rag_logs) else {}
            })

        return logs