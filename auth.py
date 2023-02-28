from flask import Flask,request, render_template,redirect,flash,url_for,session
from flask_login import login_user, logout_user, login_required
import time
from main import *
from model import *
import secrets
from werkzeug.security import generate_password_hash,check_password_hash



@app.route("/",methods=["POST","GET"])
def login():
    if request.method== 'POST':

        email=request.form.get('email')
        password=request.form.get('password')


        
        query_=User.query.filter_by(email=email).first()
        

        if not query_:
            flash('You do not have an account!')
        
        #query_ = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        
        if email == query_.email:
            if check_password_hash(query_.password, password):
                login_user(query_,remember=True)
                session['name'] = query_.name
                TOKEN = secrets.token_hex(16)
                session['token']=TOKEN
                flash('You were successfully logged in')
                
                return redirect('/dashboard')
            else:
                flash('Check your details!')

        

    return render_template('login.html')
@app.route("/create",methods=["POST","GET"])
def create_acc():
    if request.method=='POST':
        with app.app_context():
            db.create_all()
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        if len(password)<5:
            flash('Name and Password should have more than 5 characters!')

        elif len(name)<5:
            flash('Name and Password should have more than 5 characters!')
        else:
            
            query_=User.query.filter_by(email=email).first()
            
            if query_:
                    flash('User already there!!')
                    
            
            else:
                hashed_password = generate_password_hash(password)
                new_user=User(name=name, email=email,password=hashed_password)
                
                
                db.session.add(new_user)
                db.session.commit()
                login_user(query_,remember=True)
                session['name'] = query_.name
                flash('Account created Succefully!!')
                return redirect('/dashboard')

    
    return render_template("Create_acc.html")
    
    

