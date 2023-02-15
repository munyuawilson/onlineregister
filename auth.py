from flask import Flask,request, render_template,redirect,flash
from flask_login import login_user, logout_user, current_user, login_required
import time
from main import app
from model import User,db
with app.app_context():
            db.create_all()


@app.route("/",methods=["POST","GET"])

def login():
    if request.method== 'POST':

        email=request.form.get('email')
        password=request.form.get('password')



        query_= db.session.execute(db.select(User).filter_by(email=email)).all()

        if not query_:
            flash('You do not have an account!')
        query_ = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        if email == query_.email:
            if password==query_.password:
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
        query_= db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        
        if email == query_.email:
                flash('User already there!!')
    
        new_user=User(name=name, email=email,password=password)
        
        
        db.session.add(new_user)
        db.session.commit()
        flash('Account created Succefully!!')
        return redirect('/dashboard')

    
    return render_template("Create_acc.html")
    
    

