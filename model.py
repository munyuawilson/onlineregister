from flask_sqlalchemy import SQLAlchemy

from main import app

db=SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///register.db"
db.init_app(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    email=db.Column(db.String,unique=True)
    password=db.Column(db.String(30))





