from flask import Flask,request, render_template
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
import openpyxl
import pandas as pd
import time
from datetime import datetime
from main import app



@app.route("/register", methods=["POST","GET"])

def register():
    if request.method=='POST':
        name=request.form.get("name")
        reg=request.form.get("reg")
        now = datetime.now()
        dictionary={'name':'',
        'reg_no':'',
        'date':''}
        
        dataframe=pd.DataFrame(dictionary,index=range(1))
        dataframe['name']=name
        dataframe['reg_no']=reg
        dataframe['date']=now.strftime("%d/%m/%Y %H:%M")
        
        print(dataframe)
        
        dataframe.to_csv("entry.csv",mode='a')
    
    
    return render_template("register.html")

@app.route("/dashboard", methods=["POST","GET"])

def dashboard():
    time=''
    
    if request.method== 'POST':
        unit=request.form.get('Unit')
        time=request.form.get('time')

        
    return render_template('dashboard.html', time=time)
