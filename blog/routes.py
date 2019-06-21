from flask import render_template,url_for,redirect,flash
from blog import app,db,bcrypt
from blog.forms import RegistrationForm,LoginForm
from blog.models import User,Post
from flask_login import login_user,current_user,logout_user



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
    if current_user.is_authenticated:
        return redirect(url_for('callHome'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}','succcess')
        #redirecting after validating form 
        return redirect(url_for('callLogin'))


    return render_template('register.html',title='Register',form=form)

#a route for login
@app.route("/login",methods=['GET','POST'])
def callLogin():
    #creating instance of LoginForm class .. object is form
    if current_user.is_authenticated:
        return redirect(url_for('callHome'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('callHome'))
        else:
            flash('Login unsuccessfull','danger')



        
       
    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('callHome'))

    