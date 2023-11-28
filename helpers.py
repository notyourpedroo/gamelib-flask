import os
from gamelib import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class GameForm(FlaskForm):
  name = StringField('Game name', [validators.DataRequired(), validators.Length(min=1, max=50)])
  category = StringField('Game category', [validators.DataRequired(), validators.Length(min=1, max=40)])
  platform = StringField('Game platform', [validators.DataRequired(), validators.Length(min=1, max=20)])
  save = SubmitField('Save')

class UserForm(FlaskForm):
  nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=50)])
  password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=1, max=100)])
  signin = SubmitField('Sign-In')

def recover_image(id):
  for file_name in os.listdir(app.config['UPLOAD_PATH']):
    if f'cover_{id}' in file_name:
      return file_name
    else:
      return 'default_cover.jpg'
  
def delete_file(id):
  file = recover_image(id)
  if file != 'default_cover.jpg':
    os.remove(os.path.join(app.config['UPLOAD_PATH'], file))