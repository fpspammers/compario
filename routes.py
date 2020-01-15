from comparioApp import comparioAppInstance, login_handler
from flask_login import current_user, login_user
from flask import request, send_file, render_template, jsonify
import json

#
#PAGE LOADING routes
#

#Loads the homepage

@comparioAppInstance.route('/')
def loadHome():
    return render_template('homepage.html')

#Loads the login page

@comparioAppInstance.route('/loginPage')
def loadLogin():
    return render_template('login.html')

#Loads the sign up page

@comparioAppInstance.route('/signUpPage')
def loadSignUp():
    return render_template('signup.html')

#
#BUSINESS LOGIC ROUTES
#

#Checkes the login details against existing user details

@comparioAppInstance.route('/processLogin', methods=['POST'])
def processLogin():
    if(current_user.is_authenticated):
        return redirect(url_for('loadHome'))
    else:
        login_handler.checkLogin()
        return render_template('login.html')



@comparioAppInstance.route('/processSignUp', methods=['POST'])
def processSignUp():
    login_handler.checkSignup()
    return render_template('login.html')



@comparioAppInstance.route('/searchProcess', methods=['POST'])
def processSearch():
    data = request.form['searchBar']
    print(data)
    items = [{"name": "Galaxy S10", "amazonPrice": 200, "flipkartPrice": 300},
    {"name": "Galaxy S10+", "amazonPrice": 400, "flipkartPrice": 500},
    {"name": "Galaxy S10e", "amazonPrice": 100, "flipkartPrice": 150}]

    return render_template("search-results.html", items = items)
