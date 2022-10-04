from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add')
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