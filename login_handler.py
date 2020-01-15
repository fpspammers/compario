from comparioApp import db, login
from comparioApp.models import User
from flask import request
from flask_login import current_user, login_user
from validate_email import validate_email

def checkSignup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirmPassword = request.form['passwordConfirm']

    existingUsers = User.query.filter_by(username=username).first()
    isEmailValid = validate_email(email, check_mx=True, check_regex=True)
    print(isEmailValid)

    if existingUsers is None:
        if isEmailValid:
            if password == confirmPassword:
                newUser = User(username=username, email=email)
                newUser.setPassword(password)
                db.session.add(newUser)
                db.session.commit()
                print("Details Saved")

            else:
                print("Passwords do not match.")
        else:
            print("Enter a valid email.")
    else:
        print("Username already exists")

def checkLogin():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if user is None:
        print("Username is invalid")
    else:
        if(user.checkPassword(password) is False):
            print("Incorrect Password Entered")
        else:
            login_user(user)
            print("Logged in successfully")
