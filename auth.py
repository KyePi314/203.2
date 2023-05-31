## For log in/sign up actions ##
from flask import render_template, request, Blueprint

auth = ('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # Defining the login page path
def login(): # Log in page function
    if request.method=='GET':
        return render_template('landingpage.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        ### Finish when doing python stuff next meeting ###