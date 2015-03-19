from . import db
import views
from marshmallow import Schema, fields
import random

class User(db.Model):
  id= db.Column(db.Integer,primary_key=True)
  image = db.Column(db.String(80))
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  age = db.Column(db.Integer)
  sex = db.Column(db.String(80))
  high_score = db.Column(db.Integer)
  TDollars = db.Column(db.Integer)
  email = db.Column(db.String(80))
  date = db.Column(db.Date())
  userid = db.Column(db.Integer)
  
  
  
  def __init__ (self,image,firstname,lastname,age,sex,email):
    self.image = image
    self.firstname=firstname
    self.lastname=lastname
    self.age = age
    self.sex = sex
    self.TDollars = 0
    self.high_score = 0
    self.email = email
    self.date = views.time()
    self.userid = random.randint(10000000,99999999)
    
  def __repr__ (self):
    return '<User%r>' % self.firstname

class UserSchema(Schema):
  formatted_name = fields.Method("format_name")


  class Meta:
    fields = ('firstname', 'lastname', 'image', 'age', 'sex', 'high_score','email','TDollars','date','userid')
 