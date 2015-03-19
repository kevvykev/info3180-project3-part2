from flask.ext.wtf import Form

from wtforms.fields import TextField,FileField,SelectField,IntegerField

#otherfieldsincludePasswordField

from wtforms.validators import Required,Email

class profile_form(Form):
  image= FileField('image')
  firstname=TextField('firstname',validators=[Required()])
  lastname = TextField('lastname',validators=[Required()])
  age = TextField('age',validators=[Required()])
  sex = SelectField('sex', choices=[
        ('M','Male'),('F','Female')], validators=[Required()])
  email = TextField('email',validators=[Required()]) 

