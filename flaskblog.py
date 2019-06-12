from flask import Flask
app = Flask(__name__)

#@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello World!</h1>"
@app.route("/About")
def callAbout():
    return "<h1>About page</h1>"

if __name__=="__main__":
    app.run(debug=True)