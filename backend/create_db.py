from app import create_app
from app.exensions import db
from app.models import *

app = create_app()

with app.app_context():
    db.create_all()
    print('✅ Base de datos y tablas creadas')