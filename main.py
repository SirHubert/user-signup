from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/")
def index():
    return render_template("user-signup.html")

@app.route("/", methods=['POST'])

def valid_name():

    name = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''

    if " " in(name):
        username_error = 'No spaces allowed'
        
    else:
        if len(name)>20 or len(name)< 3:
            username_error = 'Entry must be between 3-20 characters'
            
    
    if " " in(password):
        password_error = 'No spaces allowed'   
        
    else:
        if len(password)>20 or len(password)< 3:
            password_error = 'Entry must be between 3-20 characters'
    
    if password != verify:
            password_error = 'Passwords do not match'

    if len(email)>0:
        if len(email)>20 or len(email)< 3:
            email_error = 'Entry must be between 3-20 characters'
        else:
            if email.count('@') !=1 or email.count('.') !=1:
             email_error = 'Improper email format'

    if not username_error and not password_error and not email_error:
        return redirect('/welcome?name={0}'.format(name))
    else:
        return render_template('user-signup.html', username_error = username_error, 
        password_error = password_error, email_error=email_error, username=name, password=password)

    


        


@app.route("/welcome")
def valid_info():
    name = request.args.get('name')
    return '<h1>Welcome {0}</h1>'.format(name)




    
app.run()