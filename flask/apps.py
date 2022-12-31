from flask import Flask,render_template,request,jsonify,flash,redirect,url_for
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os,sys
import uuid
app = Flask(__name__)
app.secret_key = os.urandom(16)

db = MongoClient(
    host='mongodb',
    port=27017
)

for x in os.environ:
        print((x, os.getenv(x)))

from supporters import *
@app.route('/')
def main_page():
    return render_template("profile.html")

@app.route('/login/',methods=["GET","POST"])
def login_page():
    if request.method =="POST":
        if (
            (request.form['username'] == os.environ['admin_user']) & \
            (request.form['password']== os.environ['admin_pass'])
        ):
            return redirect(url_for('create_profile'))
        else:
            flash("Incorrect Password!! Please try again!!")
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route('/manage/',methods=['GET','POST'])
def create_profile():
    if request.method == "GET":
            return render_template(
                'create_profile.html',
                len=len(profile_fields),
                fields=profile_fields
                )
    else:
        file = request.files['img_file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        # filename =str( uuid.uuid1() )+ '_'+secure_filename(file.filename)
        filename =secure_filename(file.filename)
        file.save(os.path.join(image_save_path, filename))
        #print('upload_image filename: ' + filename)
        flash('Profile successfully updated.')
        return redirect(url_for('login_page'))

if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')
