from flask.ext.wtf import Form

from wtforms.fields import TextField,FileField,SelectField,IntegerField,PasswordField,SubmitField

#otherfieldsincludePasswordField

from wtforms.validators import Required,Email

class profile_form(Form):
  image= FileField('image')
  username=TextField('username',validators=[Required()])
  firstname=TextField('firstname',validators=[Required()])
  lastname = TextField('lastname',validators=[Required()])
  age = TextField('age',validators=[Required()])
  sex = SelectField('sex', choices=[
        ('Male','Male'),('Female','Female')], validators=[Required()])
  
class update_form(Form):
  image= FileField('image')
  username=TextField('username',validators=[Required()])
  firstname=TextField('firstname',validators=[Required()])
  lastname = TextField('lastname',validators=[Required()])
  age = TextField('age',validators=[Required()])
  sex = SelectField('sex', choices=[
        ('Male','Male'),('Female','Female')], validators=[Required()])
  email = TextField('email',validators=[Required()])
  password = PasswordField('password',validators=[Required()])
  
class login_form(Form):
  email = TextField('email',validators=[Required()]) 
  password = PasswordField('password',validators=[Required()])
  submit = SubmitField('SUBMIT')
  
class register_form(Form):
  email = TextField('email',validators=[Required()]) 
  password = PasswordField('password',validators=[Required()])
  submit = SubmitField('SUBMIT')
  

