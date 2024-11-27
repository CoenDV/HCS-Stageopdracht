from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Frontend_log(db.Model):
    __tablename__ = 'frontend_logs'
    correlation_id = db.Column(db.Integer, primary_key=True)
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
    correlation_id = db.Column(db.Integer, primary_key=True)
    retrieved_document_id = db.Column(db.Integer, nullable=True)
    similarity_score = db.Column(db.Float, nullable=True)
    time = db.Column(db.Time, nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Backend_log {self.correlation_id}>'
    
    def to_dict(self):
        return {
            "retrieved_document_id": self.retrieved_document_id,
            "similarity_score": self.similarity_score,
            "time": datetime.time.strftime(self.time, "%H:%M:%S"),
            "url": self.url
        }
    
class Llm_log(db.Model):
    __tablename__ = 'llm_logs'
    correlation_id = db.Column(db.Integer, primary_key=True)
    without_rag_answer = db.Column(db.String(255), nullable=True)
    without_rag_duration = db.Column(db.Time, nullable=True)
    with_rag_answer = db.Column(db.String(255), nullable=True)
    with_rag_duration = db.Column(db.Time, nullable=True)
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Llm_logs {self.correlation_id}>'
    
    def to_dict(self):
        return {
            "without_rag_answer": self.without_rag_answer,
            "without_rag_duration": datetime.time.strftime(self.without_rag_duration, "%H:%M:%S"),
            "with_rag_answer": self.with_rag_answer,
            "with_rag_duration": datetime.time.strftime(self.with_rag_duration, "%H:%M:%S"),
            "url": self.url
        }