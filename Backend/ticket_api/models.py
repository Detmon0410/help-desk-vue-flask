from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    __tablename__ = 'tickets'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    user_info = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f"<Ticket {self.title}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_info': self.user_info,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
