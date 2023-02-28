from flask import Flask,request, render_template,send_file,session,url_for,abort,redirect
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
import openpyxl
import pandas as pd
import time
from datetime import datetime
from main import *
from model import *
from auth import *
import csv
import pyshorteners
import datetime





@app.route("/register/<token>", methods=["POST","GET"])
def register(token):
    time=session.get('time') 
    print(int(time))
    unit=session.get('unit')
    current_time=session.get('current_time')
    print(current_time)
    current_time=datetime.datetime.strptime(current_time, '%H:%M:%S').time()
    print(current_time)
    print(datetime.datetime.now().time())
    
    time_end = (datetime.datetime.combine(datetime.date.today(), current_time) +
              datetime.timedelta(minutes=int(time))).time()
    
    
    if token != session.get('token'):
        return abort(404)
    
        
    
    print(time_end)
    CSV_FILE = f'{unit}.csv'

    
    CSV_FIELDNAMES = ['Name', 'Registration Number']
    
    if request.method=='POST':
        if datetime.datetime.now().time() > time_end:
            return "Time expired"
        
        else:
            name = request.form['name']
            reg_number = request.form['reg_number']
            
            # Append the new registration to the CSV file
            with open(CSV_FILE, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
                writer.writerow({'Name': name, 'Registration Number': reg_number})
            
            

        
        
    return render_template("register.html")

@app.route("/dashboard", methods=["POST","GET"])
@login_required
def dashboard():
    time=''
    short_url=''
    
    name=session.get('name')
    
    
    
    if request.method== 'POST':
        unit=request.form.get('unit')
        time=request.form.get('time')
        session['time']=time  
        s = pyshorteners.Shortener()
        token=session.get('token')
        short_url = s.tinyurl.short(f'http://127.0.0.1:5000/register/{token}')
        session['unit']=unit
        
        session['current_time']=datetime.datetime.now().time().strftime('%H:%M:%S')

        
        
        
    
    
        
    return render_template('dashboard.html', time=time, name=name, short_url=short_url)
@app.route('/download')
def download():
    
    return send_file(f"{session.get('unit')}.csv", as_attachment=True)
@app.route('/logout', methods=['POST','GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))