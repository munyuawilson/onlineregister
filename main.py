from flask import Flask,request, render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
from auth import *
from views import *



if __name__=="__main__":
    app.run(debug=True)
