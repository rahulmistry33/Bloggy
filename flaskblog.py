from flask_sqlalchemy import SQLAlchemy 
from flask import Flask,render_template,url_for,flash,redirect
#this import for login and register from forms.py
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
#for security and preventing cross site request forgery
#generated using secrets module :D
app.config['SECRET_KEY']='0501d344495cc373a2a73670ca42ae80'
#this is for sqlite
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db=SQLAlchemy(app)

class User(db.Model):

    id=db.column(db.Integer,primary_key=True)
    username=db.column(db.String(20),unique=True,nullable=False)
    email=db.column(db.String(20),unique=True,nullable=False)
    image_file=db.column(db.String(20),nullable=False,default="default.png")
    password=db.column(db.string(60),nullable=False)

    def __repr__(self):
        return f"{self.username},{self.email}.{self.image_file}"

class Post(db.Model):
    








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
@app.route("/register",methods=['GET','POST'])
def callRegister():
    #creating instance of RegistrationForm class .. object is form
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','succcess')
        #redirecting after validating form 
        return redirect(url_for('callHome'))


    return render_template('register.html',title='Register',form=form)

#a route for login
@app.route("/login",methods=['GET','POST'])
def callLogin():
    #creating instance of LoginForm class .. object is form
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="rahul.mistry@somaiya.edu" and form.password.data=="123":
            flash('you have logged in successfully!','succcess')
            return redirect(url_for('callHome'))
        else:
            flash('you have entered wrong email or password','danger')

        
       
    return render_template('login.html',title='Login',form=form)
    

if __name__=="__main__":
    app.run(debug=True)