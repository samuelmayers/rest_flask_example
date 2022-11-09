from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from db import db, ma
from model import Form , FormSchema
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://postgres:Y7rIFjrCMOYdrM4QRxkR@containers-us-west-104.railway.app:5526/railway"
#f"postgresql://${{ PGUSER }}:${{ PGPASSWORD }}@${{ PGHOST }}:5526/${{ PGDATABASE }}"
#'postgresql://postgres:Y7rIFjrCMOYdrM4QRxkR@containers-us-west-104.railway.app:5526/railway'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
SQLAlchemy(app)
Marshmallow(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    forms= Form.query.all()
    return render_template("index.html",forms=forms)

@app.route('/add', methods=['POST'])
def add():
    fullname=request.form['fullname']
    phone=request.form['phone']
    email=request.form['email']
    form=Form(fullname,phone,email)
    db.session.add(form)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<string:id>',methods=['POST','GET','PUT'])
def edit(id):
    form=Form.query.get(id)
    if request.method == "POST" or request.method == "PUT":
        form.fullname = request.form['fullname']
        form.email = request.form['email']
        form.phone = request.form['phone']
        db.session.commit()
        return redirect('/')
    return render_template("update.html", form=form)

@app.route('/delete/<id>', methods=['DELETE','GET'])
def delete(id):
    form=Form.query.get(id)
    db.session.delete(form)
    db.session.commit()
    return redirect('/')

@app.route('/api')
def apis():
    forms = Form.query.all()
    form_schema = FormSchema(many=True)
    op = form_schema.dump(forms)
    return jsonify({"Form":op})

@app.route('/api/<id>')
def api(id):
    form = Form.query.get(id)
    form_schema = FormSchema()
    op = form_schema.dump(form)
    return jsonify({"Form":op})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
