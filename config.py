import os

SECRET_KEY = 'flaskgamelib'

SQLALCHEMY_DATABASE_URI = \
  '{sgbd}://{username}:{password}@{server}/{database}'.format(
    sgbd = 'mysql+mysqlconnector',
    username = 'root',
    password = 'admin',
    server = '127.0.0.1',
    database = 'gamelib'
  )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'