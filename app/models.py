from . import db
import views
from marshmallow import Schema, fields


class User(db.Model):
  userid = db.Column(db.Integer,primary_key=True)
  image = db.Column(db.String(80))
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  username = db.Column(db.String(80), unique=True)
  age = db.Column(db.Integer)
  sex = db.Column(db.String(80))
  high_score = db.Column(db.Integer)
  TDollars = db.Column(db.Integer)
  date = db.Column(db.Date())
  
  def __init__ (self,userid,image,firstname,lastname,age,sex):
    self.image = image
    self.firstname=firstname
    self.lastname=lastname
    self.age = age
    self.sex = sex
    self.TDollars = 0
    self.high_score = 0
    self.date = views.time()
    self.userid =userid
    
    
  
    
  def __repr__ (self):
    return '<User%r>' % self.firstname

class UserSchema(Schema):
  formatted_name = fields.Method("format_name")


  class Meta:
    fields = ('firstname', 'lastname', 'image', 'age', 'sex', 'high_score','email','TDollars','date','userid')
 
class Logindb(db.Model):
  email = db.Column(db.String, unique = True)
  password = db.Column(db.String(80))
  userid = db.Column(db.Integer, primary_key = True)
  confirmed = db.Column(db.Boolean, default=False)
  
  def __init__(self,userid,email,password):
    self.email =  email 
    self.password = password 
    self.userid = userid
    self.confirmed = False
    
  def is_authenticated(self):
        return True

  def is_active(self):
        return True

  def is_anonymous(self):
        return False

  def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

  def __repr__(self):
        return '<User %r>' % (self.username)
  