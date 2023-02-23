from flask import Flask,request, render_template,send_file
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
import openpyxl
import pandas as pd
import time
from datetime import datetime
from main import app


dictionary={'name':'',
        'reg_no':'',
        'date':''}
dataframe=pd.DataFrame(dictionary,index=range(1))


@app.route("/register", methods=["POST","GET"])

def register():
    if request.method=='POST':
        name=request.form.get("name")
        reg=request.form.get("reg")
        now = datetime.now()
        
        
        dataframe.name=name
        dataframe.reg_no=reg
        dataframe.date=now.strftime("%d/%m/%Y %H:%M")
        
        dataframe.to_csv("entry.csv",mode='a')
    
    
    return render_template("register.html")

@app.route("/dashboard", methods=["POST","GET"])
#@login_required
def dashboard():
    time=''
    
    if request.method== 'POST':
        unit=request.form.get('Unit')
        time=request.form.get('time')
    
        

        
    return render_template('dashboard.html', time=time)
@app.route('/download')
def download():
    
    return send_file('entry.csv', as_attachment=True)