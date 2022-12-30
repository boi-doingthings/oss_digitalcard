from flask import Flask,render_template,request
from pymongo import MongoClient
app = Flask(__name__)

db = MongoClient(
    host='mongodb',
    port=27017
)


@app.route('/')
def main_page():
    return "This is home."

@app.route('/login',methods=["GET","POST"])
def login_page():
    if request.method =="POST":
        return "Your creds are: {} and {}".format(
            request.form.get("username"),
            request.form.get("password")
            )
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')
