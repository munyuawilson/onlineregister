from flask import Flask,request, render_template
from flask_login import LoginManager





app = Flask(__name__,static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
from auth import *
from views import *
from model import User
login=LoginManager()
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))



if __name__=="__main__":
    app.run(debug=True)
