import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Connecting...")
try:
  conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='admin'
  )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print('There is something wrong with the username or password')
  else:
    print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `gamelib`;")

cursor.execute("CREATE DATABASE `gamelib`;")

cursor.execute("USE `gamelib`;")

# criando tabelas
TABLES = {}

TABLES['Games'] = ('''
  CREATE TABLE `games` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `category` varchar(40) NOT NULL,
  `platform` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
  CREATE TABLE `users` (
  `name` varchar(50) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`nickname`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
  table_sql = TABLES[table_name]
  try:
    print('Creating table {}:'.format(table_name), end=' ')
    cursor.execute(table_sql)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
      print('Already exists')
    else:
      print(err.msg)
  else:
    print('OK')

# inserindo usuarios
user_sql = 'INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)'
users = [
  ("Pedro", "notyourpedroo", generate_password_hash("111").decode('utf-8')),
  ("Larissa", "hillaryssaa", generate_password_hash("222").decode('utf-8')),
  ("Matheus", "matheus_leodonel", generate_password_hash("333").decode('utf-8'))
]
cursor.executemany(user_sql, users)

cursor.execute('select * from gamelib.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
  print(user[1])

# inserindo jogos
game_sql = 'INSERT INTO games (name, category, platform) VALUES (%s, %s, %s)'
games = [
  ('Rocket League', 'Sports', 'PC'),
  ('God of War', 'Hack n Slash', 'PS2'),
  ('Mortal Kombat', 'Luta', 'PS2'),
  ('Valorant', 'FPS', 'PC'),
  ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
  ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(game_sql, games)

cursor.execute('select * from gamelib.games')
print(' -------------  Games:  -------------')
for game in cursor.fetchall():
  print(game[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
