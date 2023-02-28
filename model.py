from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from main import app

db=SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///register.db"
db.init_app(app)
class User(db.Model,UserMixin):
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    email=db.Column(db.String,unique=True)
    password=db.Column(db.String(30))
    def __init__(self, name, email, password, is_active=True):
        self.name = name
        self.email = email
        self.password = password
        self.is_active = is_active

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
 
    '''def __init__(self, id, is_active=True):
        self.id = id
        self.is_active = is_active
        
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False'''





