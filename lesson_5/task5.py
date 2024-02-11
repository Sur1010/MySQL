import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

with open('users.txt', 'r') as file:
  sql_txt = file.read().split(';')

  for i in sql_txt:
    if i.strip():
      cursor = connection.cursor()
      cursor.execute(i)
      cursor.close()