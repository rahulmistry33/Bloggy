from flask import Flask,render_template,url_for
#this import for login and register from forms.py
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
#for security and preventing cross site request forgery
#generated using secrets module :D
app.config['SECRET_KEY']='0501d344495cc373a2a73670ca42ae80'

posts=[
    {
        'Author':'Rahul Mistry',
        'Title':'Blog Post 1',
        'Content':'Some shitty quotes',
        'Date':'April 21'
    },
    {
        'Author':'Gayatri Srinivasan',
        'Title':'Blog Post 2',
        'Content':'Some shitty quotes',
        'Date':'Feb 1'
    }
]
#@app.route("/")
@app.route("/")
def callHome():
    return render_template("home.html", posts=posts)

@app.route("/About")
def callAbout():
    return render_template("about.html",title="about")

#a route for register
@app.route("/register")
def callRegister():
    #creating instance of RegistrationForm class .. object is form
    form=RegistrationForm()
    return render_template('register.html',title='Register',form=form)

#a route for login
@app.route("/login")
def callLogin():
    #creating instance of LoginForm class .. object is form
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)
    

if __name__=="__main__":
    app.run(debug=True)