from app.exensions import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cash_register_id = db.Column(db.Integer, db.ForeignKey('cashregister.id'))
    total = db.Column(db.Numeric(10,2), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)