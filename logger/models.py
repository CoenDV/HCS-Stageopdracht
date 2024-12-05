from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Frontend_log(db.Model):
    __tablename__ = 'frontend_logs'
    correlation_id = db.Column(db.String(36), primary_key=True)
    time = db.Column(db.Time, nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Frontend_log {self.correlation_id}>'
    
    def to_dict(self):
        return {
            "time": datetime.time.strftime(self.time, "%H:%M:%S"),
            "url": self.url
        }

class Backend_log(db.Model):
    __tablename__ = 'backend_logs'
    correlation_id = db.Column(db.String(36), primary_key=True)
    prompt = db.Column(db.String(255), nullable=False)
    retrieved_documents = db.Column(db.Text, nullable=True)
    similarity_score = db.Column(db.Float, nullable=True)
    time = db.Column(db.Time, nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Backend_log {self.correlation_id}>'
    
    def to_dict(self):
        return {
            "prompt": self.prompt,
            "retrieved_documents": self.retrieved_documents,
            "similarity_score": self.similarity_score,
            "time": datetime.time.strftime(self.time, "%H:%M:%S"),
            "url": self.url
        }
    
class Llm_without_rag_log(db.Model):
    __tablename__ = 'llm_without_rag_logs'
    correlation_id = db.Column(db.String(36), primary_key=True)
    without_rag_answer = db.Column(db.String(255), nullable=False)
    without_rag_duration = db.Column(db.Time, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Llm_logs {self.correlation_id}>'
    
    def to_dict(self):
        return {
            "without_rag_answer": self.without_rag_answer,
            "without_rag_duration": datetime.time.strftime(self.without_rag_duration, "%H:%M:%S"),
            "url": self.url,
            "model": self.model
        }
    
class Llm_with_rag_log(db.Model):
    __tablename__ = 'llm_with_rag_logs'
    correlation_id = db.Column(db.String(36), primary_key=True)
    with_rag_answer = db.Column(db.String(255), nullable=False)
    with_rag_duration = db.Column(db.Time, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Llm_logs {self.correlation_id}>'
    
    def to_dict(self):
        return {
            "with_rag_answer": self.with_rag_answer,
            "with_rag_duration": datetime.time.strftime(self.with_rag_duration, "%H:%M:%S"),
            "url": self.url,
            "model": self.model
        }