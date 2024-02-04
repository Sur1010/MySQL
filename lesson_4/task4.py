import camelcase
import mysql.connector

# ---- 4.4 ----
c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# ---- 4.11 ----
mydb = mysql.connector.connect(
  host="localhost",
  user="",
  password=""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE new_db")