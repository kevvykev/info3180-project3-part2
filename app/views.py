"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import smtplib
import random
import os
from app import app
from flask import render_template, request, redirect, url_for, jsonify, g, flash
from app.models import UserSchema
from app.models import User, Logindb
from app import db
import time
from datetime import datetime
from . forms import profile_form,login_form,register_form,update_form
import random
import json
from werkzeug import secure_filename
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from token import generate_confirmation_token, confirm_token
from decorators import check_confirmed
#from app.models import UserSchema

'''Function declaration'''
def sendmail(email,subject,msg):
  # Credentials (if needed)
  fromname = 'kevyg123@gmail.com'
  fromaddr = 'kevyg123@gmail.com'
  
  username = 'kevyg123@gmail.com'

  password = 'hbodojywustkxeou'

  # The actual mail send

  server = smtplib.SMTP('smtp.gmail.com:587')

  server.starttls()
  server.login(username,password)
  toaddrs = email
  message = """From: {} <{}>

  To: {} <{}>

  Subject: {}

  {}

  """
  toname = 'User'

  messagetosend = message.format(
   fromname,
   fromaddr,
   toname,
   toaddrs,
   subject,
   msg)
  server.sendmail(fromaddr, toaddrs, messagetosend)

  server.quit()
  return True

def time():
  time = datetime.now()
  return time
###
# Routing for your application.
###
@app.route('/game/')
def games():
  return render_template('games.html')

@app.route('/profile/update')
def update():
  form = update_form()
  user = User.query.filter_by(userid = current_user.userid).first()
  user = User.query.filter_by(username = form.username).first()
  email = Logindb.query.filter_by(email = form.username).first()
  if request.method == "POST":
    if form.firstname.data:
      user.firstname = form.firstname.data
      db.session.add(user)
      db.session.commit()
    if form.lastname.data:
      user.lastname = form.lastname.data
      db.session.add(user)
      db.session.commit()
    if form.age.data:
      user.age = form.age.data
      db.session.add(user)
      db.session.commit()
    if form.sex.data:
      user.sex = form.sex.data
      db.session.add(user)
      db.session.commit()
    if form.age.data:
      user.age = form.age.data
      db.session.add(user)
      db.session.commit()
    if not username:
      if form.username.data:
        user.username = form.username.data
        db.session.add(user)
    if not email:
      if form.email.data:
        users.email = form.email.data
        db.session.add(user)
      return redirect(url_for('profile'))
    return render_template("update.html", form=form)
      
      
      

@app.route('/signup/confirm/<confirmcode>')
@login_required
def confirm_email(confirmcode):
    try:
        email = confirm_token(confirmcode)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = Logindb.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('profile'))
  
  
@app.route("/login", methods=["GET", "POST"])
def login():
    form = login_form()
    if request.method == 'POST':
      user =  Logindb.query.filter_by(email = form.email.data).first()
      if user:
        if user.password == form.password.data:
          user = load_user(user.userid)
          login_user(user)
          return redirect(request.args.get("next") or url_for("home"))
    return render_template("login.html", form=form)

@app.route('/resend')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('confirm_email', confirmcode=token, _external=True)
    html = render_template('activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('unconfirmed'))
  
@app.before_request
def before_request():
  g.user=current_user.get_id()
  
@lm.user_loader
def load_user(userid):
  return Logindb.query.get(int(userid))

@app.route("/logout")
def logout():
  logout_user()
  return redirect(request.args.get("next") or url_for("login"))

@app.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect('home')
    flash('Please confirm your account!', 'warning')
    return render_template('unconfirmed.html') 
  
@app.route("/register", methods=["GET","POST"])
def register():
  form = register_form()
  user = Logindb.query.filter_by(email=form.email.data).first()
  if request.method == "POST":
    if user:
      error = 'User already registered'
      return render_template('register.html',form=form, error=error)
    else:
      userid = random.randint(10000000, 99999999)
      u_id = Logindb.query.filter_by(userid=userid).first()
    if u_id:
      userid = random.randint(10000000, 99999999)
    else:
      user = Logindb(userid, form.email.data, form.password.data)    
      db.session.add(user)
      db.session.commit()
      token = generate_confirmation_token(user.email)
      confirm_url = url_for('confirm_email', confirmcode=token, _external=True)
      html = render_template('activate.html', confirm_url=confirm_url)
      subject = "Please confirm your email"
      sendmail(user.email, subject, html)

      login_user(user)
     
      return redirect(url_for('profile'))
  return render_template('register.html',form=form)

@app.route('/game/<int:id>')
def game(id):
  if id == 1:
    return render_template('platformer.html')
  if id == 2:
    return render_template('spaceinvader.html')
    
@app.route('/')
@login_required
@check_confirmed
def home():
  """Render website's home page."""
  return render_template('home.html')


@app.route('/_get_current_user')
def get_current_user():
  username = "bob"
  email = "bob@example.com"
  id = "3424324"
  return jsonify(username=username,
                   email=email,
                   id=id)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
  
@app.route('/profile/',methods=["GET","POST"])
@login_required
@check_confirmed
def profile():
  form = profile_form()
  if request.method == 'POST':
    if form.validate_on_submit():
      image = request.files['image']
      filename = secure_filename(image.filename)
      image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  
      firstname = request.form['firstname']
      lastname = request.form['lastname']
      age = request.form['age']
      sex = request.form['sex']
      userid = current_user.userid
      new_user = User(userid,filename,firstname,lastname,age,sex)
      db.session.add(new_user)
      db.session.commit()
      return render_template('profileform.html', form=form)
  return render_template('profileform.html', form=form)

@app.route("/profiles/",methods=["POST", "GET"])

def profiles():
  '''render webpage profiles'''
  users = db.session.query(User).all()
  if request.method =="POST":
    serializer = UserSchema(many=True)
    result = serializer.dump(users)
    return jsonify({'Users':result.data})
  return render_template('profile.html',users=users)


@app.route("/profile/<userid>/", methods=["GET"])
def user(userid):
  users = User.query.filter_by(userid=userid).first()
  if request.method=="POST":
    return jsonify(Age=user.age,Sex = user.sex, date= user.date, Tdollars=user.TDollars, Image= user.image, High_Score = user.high_score)
    users = User.query.filter_by(userid=userid).first()
  return render_template('singleprofile.html', user = users)



   
   


if __name__ == '__main__':
  app.run(debug=True, host=os.getenv("IP", '0.0.0.0'),port=int(os.getenv("PORT", 8080) ))