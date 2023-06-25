from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import data_required
 
app=Flask(__name__)
@app.route('/')

def index():
    first_name="KAVIN"
    names="This is safe usage"
    favourite_things=["Crazy","Stuffs","to","Play",40,42]
    return render_template("index.html",First_name=first_name,safes=names,favourite_things=favourite_things)

@app.route('/user/<name>')  
def user(name):
    return render_template("user.html",user_name=name)

@app.errorhandler(404)
def Page_notFound(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def Internal_Error(e):
    return render_template("500.html"),500

