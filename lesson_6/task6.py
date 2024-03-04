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

new_data = []
for row in rows:
    new_row = (
        # row[0:6],
        # row[6:10],
        # row[10:13],
        # row[13:17],
        # row[17:]       
    )
    # user = row[0:6],
    # user_finance = row[6:10]
    # user_details = row[10:13]
    # insert_user = f"INSERT INTO users(first_name, last_name, email, age, country) VALUES({str(user)},)"
    # insert_user_finance = f"INSERT INTO users(user_id, salary, bonus) VALUES({str(user_finance)},)"
    # insert_user_details = f"INSERT INTO users(user_id, height, weight, eye_color) VALUES({str(user_details)},)"

    new_data.append(new_row)
print(new_data)



new_db_connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = main_db
)

new_cursor = new_db_connection.cursor()



# new_cursor.close()
# new_db_connection.close()



