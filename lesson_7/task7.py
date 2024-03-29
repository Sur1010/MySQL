import mysql.connector
from config import host, user, password, database

connection = mysql.connector.connect(
host = host,
user = user,
password = password,
database = database
)

cursor = connection.cursor()

# query = '''
#     SELECT 
#         users.id,
#         users.first_name,
#         users.last_name,
#         users.email,
#         users.age,
#         users.country,
#         user_details.height,
#         user_details.weight,
#         user_details.eye_color,
#         user_finance.salary,
#         user_finance.bonus,
#         user_mobiles.phone_number,
#         user_mobiles.operator,
#         user_mobiles.mobile_country,
#         cars.car,
#         cars.car_number,
#         cars.model,
#         cars.year
#     FROM users
#     LEFT JOIN user_details ON users.id = user_details.user_id
#     LEFT JOIN user_finance ON users.id = user_finance.user_id
#     LEFT JOIN cars ON users.id = cars.user_id
#     LEFT JOIN user_mobiles ON users.id = user_mobiles.user_id
# '''

# cursor.execute(query)

table_name = input("Enter the name of the table you want to see: ")

choice = input("select the action 'create', 'update', 'delete', 'list': ")

if choice == "create":
    new_column_name = input('Enter the new column name: ')
    column_type = input('Enter the column type(INT, VARCHAR(255), etc.): ')
    create_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {column_type}"
    cursor.execute(create_query)
    connection.commit()
elif choice == "update":
    column_name = input('Enter the column name to update: ')
    new_value = input('Enter the new value: ')
    update_query = f"UPDATE {table_name} SET {column_name} = '{new_value}'"
    cursor.execute(update_query)
    connection.commit()
elif choice == "delete":
    id_to_delete = input('Enter the id to delete: ')
    delete_query = f"DELETE FROM {table_name} WHERE id = {id_to_delete}"
    cursor.execute(delete_query)
    connection.commit()
elif choice == "list":    
    limit_size = input('Select how many values yow want to see: ')
    offset = 0

    list_query = f"SELECT * FROM {table_name} LIMIT {limit_size} OFFSET {offset}"
    cursor.execute(list_query)
    results = cursor.fetchall()

    for row in results:
        print(row)

# table_name_query = f'SELECT * FROM {table_name}'

# cursor.execute(table_name_query)

# rows = cursor.fetchall()


# for row in rows:
#     print(row)

cursor.close()
connection.close()