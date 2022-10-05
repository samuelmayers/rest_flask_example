from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os

from regex import P
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///"+dir_path+r"\formulario.db"
db = SQLAlchemy(app)

class Form(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(200),nullable=False)
    phone=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False)
    def __init__(self,fullname,phone,email):
        self.fullname=fullname
        self.phone=phone
        self.email=email

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    fullname=request.form['fullname']
    phone=request.form['phone']
    email=request.form['email']
    form=Form(fullname,phone,email)
    db.session.add(form)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit')
def edit():
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=4000,debug=True)