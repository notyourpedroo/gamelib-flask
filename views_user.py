from gamelib import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Users
from helpers import UserForm
from flask_bcrypt import check_password_hash

@app.route('/signin')
def signin():
  next_page = request.args.get('next_page')
  form = UserForm()
  if next_page != None:
    return render_template('signin.html', next_page=next_page, form=form)
  else:
    return render_template('signin.html', next_page='/', form=form)

@app.route('/logout')
def logout():
  session['logged_user'] = None
  flash('Logged out successfully!')
  return redirect(url_for('index'))

@app.route('/authenticate', methods=['POST',])
def authenticate():
  form = UserForm(request.form)
  user = Users.query.filter_by(nickname = form.nickname.data).first()
  password = check_password_hash(user.password, form.password.data)
  if user and password:
    session['logged_user'] = user.nickname
    flash(user.name + ' authenticated successfully!')
    next_page = request.form['next_page']
    return redirect(next_page)
  else:
    flash('Not authenticated')
    return redirect(url_for('signin'))
  