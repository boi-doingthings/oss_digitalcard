from flask import Flask,render_template,request

app = Flask(__name__)

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
    app.run(debug=True,port=5000)
