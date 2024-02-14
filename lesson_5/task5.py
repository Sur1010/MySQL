import mysql.connector
from config import host, user, password, database

connection = mysql.connector.connect(
host = host,
user = user,
password = password,
database = database
)

table_list = ["users.txt", "user_cars.txt", "user_details.txt", "user_finance.txt", "user_mobiles.txt"]

for txt_file in table_list:
  with open(txt_file, 'r') as file:
    sql_txt = file.read().split(';')

    for i in sql_txt:
      if i.strip():
        cursor = connection.cursor()
        cursor.execute(i)
        cursor.close()