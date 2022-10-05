from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///"+dir_path+r"\formulario.db"
db = SQLAlchemy(app)

class Form(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(200))
    phone=db.Column(db.String(200))
    email=db.Column(db.String(200), unique=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    return redirect(url_for('home'))

@app.route('/edit')
def edit():
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)