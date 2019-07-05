from flask import Flask,render_template,url_for,request,session
from flask_sqlalchemy import SQLAlchemy
import json 
from flask_mail import Mail

local_server=True
with open("config.json","r") as c:
    params=json.load(c)["params"]

 
app=Flask(__name__)
app.secret_key = 'rahulrocks:D'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params["user-gmail"],
    MAIL_PASSWORD= params["user-password"]

)

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

    
db = SQLAlchemy(app)
mail=Mail(app)

class Contacts(db.Model):
    # sno,name,email,phone,message
    sno = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20),  nullable=False)
    message = db.Column(db.String(100),  nullable=False)

class Posts(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100),  nullable=False)
    date = db.Column(db.String(20),  nullable=False)
    subtitle = db.Column(db.String(50),  nullable=False)






@app.route("/")
def home():
    posts=Posts.query.filter_by().all()
    return render_template("index.html",params=params,posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",params=params)

@app.route("/dashboard",methods=["GET","POST"])
def login():
    if 'user' in session and session['user']==params["admin-username"]:
        return render_template("dashboard.html",params=params)

    if request.method=="POST":
        uname=request.form.get('uname')
        password=request.form.get('pass')
        if uname==params["admin-username"] and password==params["admin-password"]:
            session["user"]=uname
            return render_template("dashboard.html",params=params)
       
    return render_template("login.html",params=params)

@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name,email=email,phone=phone,message=message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New message from blog"+name,
        sender=email,
        recipients=[params["user-gmail"]],
        body=message + "\n" + phone)



        
    return render_template("contact.html",params=params)

@app.route("/posts_route/<string:post_slug>",methods=['GET'])
def posts_route(post_slug):
    postings=Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html",params=params,postings=postings)









if __name__=="__main__":
    app.run(debug=True)