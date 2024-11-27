from models import Frontend_log, Backend_log, Llm_log, db

class Repository:
    def get_all_frontend_logs():
        return Frontend_log.query.all()

    def save(frontend_log):
        db.session.add(frontend_log)
        db.session.commit()
        return frontend_log
    
    def get_all_backend_logs():
        return Backend_log.query.all()
    
    def save(backend_log):
        db.session.add(backend_log)
        db.session.commit()
        return backend_log
    
    def get_all_llm_logs():
        return Llm_log.query.all()
    
    def save(llm_log):
        db.session.add(llm_log)
        db.session.commit()
        return llm_log