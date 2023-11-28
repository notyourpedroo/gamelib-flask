from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from gamelib import app, db
from models import Games
from helpers import recover_image, delete_file, GameForm, UserForm
import time

@app.route('/')
def index():
  game_list = Games.query.order_by(Games.id)
  return render_template('list.html', title='Games', games=game_list)

@app.route('/new')
def new():
  if 'logged_user' not in session or session['logged_user'] == None:
    return redirect(url_for('signin', next_page=url_for('new')))
  form = GameForm()
  return render_template('new.html', title='New Game', form=form)

@app.route('/create', methods=['POST',])
def create():
  form = GameForm(request.form)
  if not form.validate_on_submit():
    return redirect(url_for('new'))
  name = form.name.data
  category = form.category.data
  platform = form.platform.data
  game = Games.query.filter_by(name=name).first()
  if game:
    flash('This game already exists')
    return redirect(url_for('index'))
  new_game = Games(name=name, category=category, platform=platform)
  db.session.add(new_game)
  db.session.commit()
  file = request.files['file']
  upload_path = app.config['UPLOAD_PATH']
  timestamp = time.time()
  file_name = f'cover_{new_game.id}-{timestamp}.jpg'
  save_path = f'{upload_path}/{file_name}'
  file.save(save_path)

  return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
  if 'logged_user' not in session or session['logged_user'] == None:
    return redirect(url_for('signin', next_page=url_for('edit')))
  game = Games.query.filter_by(id=id).first()
  form = GameForm()
  form.name.data = game.name
  form.category.data = game.category
  form.platform.data = game.platform
  game_cover = recover_image(id)
  return render_template('edit.html', title='Editing Game', id=id, game_cover=game_cover, form=form)

@app.route('/update', methods=['POST',])
def update():
  form = GameForm(request.form)

  if form.validate_on_submit():
    game = Games.query.filter_by(id=request.form['id']).first()
    game.name = form.name.data
    game.category = form.category.data
    game.platform = form.platform.data
    db.session.add(game)
    db.session.commit()
    file = request.files['file']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    delete_file(game.id)
    file_name = f'cover_{game.id}-{timestamp}.jpg'
    save_path = f'{upload_path}/{file_name}'
    file.save(save_path)

  return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
  if 'logged_user' not in session or session['logged_user'] == None:
    return redirect(url_for('signin'))
  Games.query.filter_by(id=id).delete()
  db.session.commit()
  flash('Game deleted successfully!')
  return redirect(url_for('index'))

@app.route('/uploads/<file_name>')
def image(file_name):
  return send_from_directory('uploads', file_name)
