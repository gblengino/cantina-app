from app.exensions import db
from datetime import datetime

class CashRegister(db.Model):
    __tablename__ = 'cashregister'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_open = db.Column(db.Boolean, nullable=False)
    opened_at = db.Column(db.DateTime, nullable=True)
    closed_at = db.Column(db.DateTime, nullable=True)