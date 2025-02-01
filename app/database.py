# Database setup and connection 
from app import db

def init_db():
    db.create_all()