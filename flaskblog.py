from flask import Flask,render_template,url_for
app = Flask(__name__)

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
@app.route("/home")
def callHome():
    return render_template("home.html", posts=posts)
@app.route("/About")
def callAbout():
    return render_template("about.html",title="about")
    

if __name__=="__main__":
    app.run(debug=True)