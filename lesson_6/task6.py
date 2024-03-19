import mysql.connector
from config import host, user, password, old_db, main_db 

old_db_connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = old_db   
)

old_cursor = old_db_connection.cursor()

select_data = "SELECT * FROM users"
old_cursor.execute(select_data)

rows = old_cursor.fetchall()

old_cursor.close()
old_db_connection.close()

new_db_connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = main_db
)

new_cursor = new_db_connection.cursor()

new_data = []
for row in rows:

    user = row[0:6]
    finance = row[6:10]
    details = row[10:13]
    cars = row[13:17]
    mobiles = row[17:20]

    insert_user = f"INSERT INTO users (first_name, last_name, email, age, country) VALUES('{user[1]}', '{user[2]}', '{user[3]}', {user[4]}, '{user[5]}');"
    new_cursor.execute(insert_user)
    new_db_connection.commit()
    user_id = new_cursor.lastrowid
    insert_finance = f"INSERT INTO user_finance (user_id, salary, bonus) VALUES({user_id},{finance[2]},{finance[3] or 'NULL'});"
    insert_details = f"INSERT INTO user_details (user_id, height, weight, eye_color) VALUES({user_id or 'NULL'},{details[0] or 'NULL'},{details[1] or 'NULL'},'{details[2] or 'NULL'}');"
    insert_cars = f"INSERT INTO cars (user_id, car, car_number, model, year) VALUES({user_id or 'NULL'},'{cars[0] or 'NULL'}',{cars[1] or 'NULL'},'{cars[2] or 'NULL'}',{cars[3] or 'NULL'});"
    insert_mobiles = f"INSERT INTO user_mobiles (user_id, phone_number, operator, mobile_country) VALUES({user_id or 'NULL'},{mobiles[0] or 'NULL'},'{mobiles[1] or 'NULL'}','{mobiles[2] or 'NULL'}');"
    new_cursor.execute(insert_finance)
    new_cursor.execute(insert_details)
    new_cursor.execute(insert_cars)
    new_cursor.execute(insert_mobiles)
    new_db_connection.commit()

new_db_connection.commit()


new_cursor.close()
new_db_connection.close()