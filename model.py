from flask_sqlalchemy import Model
from db import db, ma

class Form(db.Model):
    __bind_key__ = 'None'
    id=db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(200),nullable=False)
    phone=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False)
    def __init__(self,fullname,phone,email):
        self.fullname=fullname
        self.phone=phone
        self.email=email

class FormSchema(ma.Schema):
    class Meta:
       model=Form
       fields = ("fullname", "phone", "email", "_links")
