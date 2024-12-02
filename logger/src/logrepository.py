from models import Frontend_log, Backend_log, Llm_with_rag_log, Llm_without_rag_log, db

class Repository:
    # Frontend logs
    def get_all_frontend_logs():
        return Frontend_log.query.all()

    def save_frontend_log(frontend_log):
        db.session.add(frontend_log)
        db.session.commit()
        return frontend_log
    
    # Backend logs
    def get_all_backend_logs():
        return Backend_log.query.all()
    
    def save_backend_log(backend_log):
        db.session.add(backend_log)
        db.session.commit()
        return backend_log
    
    # LLM logs
    def get_all_llm_without_rag_logs():
        return Llm_without_rag_log.query.all()
    
    def save_llm_without_rag_log(llm_log):
        db.session.add(llm_log)
        db.session.commit()
        return llm_log
    
    def get_all_llm_with_rag_logs():
        return Llm_with_rag_log.query.all()
    
    def save_llm_with_rag_log(llm_log):
        db.session.add(llm_log)
        db.session.commit()
        return llm_log