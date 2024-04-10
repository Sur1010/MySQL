import mysql.connector
from config import host, user, password, database

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()

    connection.start_transaction()

    from_user = input("Who is the sender: ")
    to_user = input("Who is the recipient: ")
    money = int(input("The amount of money: "))  
    card = input("Which card: ")

    cursor.execute(f"SELECT account_balance FROM card WHERE user_id='{from_user}' AND id='{card}'")
    sender_balance = cursor.fetchone()[0]

    if sender_balance < money:
        raise ValueError("Insufficient balance")

    cursor.execute(f"UPDATE card SET account_balance = account_balance - {money} WHERE user_id='{from_user}' AND id='{card}'")

    cursor.execute(f"UPDATE card SET account_balance = account_balance + {money} WHERE user_id='{to_user}'")

    cursor.execute(f"INSERT INTO transactions (user_id, date, money, from_user_id, to_user_id, is_success) VALUES ({from_user}, NOW(), {money}, {from_user}, {to_user}, True)")

    connection.commit()

    print("Transaction successful")

except mysql.connector.Error as e:
    connection.rollback()
    print("Transaction rolled back due to error:", e)

    
    cursor.execute(f"INSERT INTO transactions (user_id, date, money, from_user_id, to_user_id, is_success) VALUES ({from_user}, NOW(), {money}, {from_user}, {to_user}, False)")

finally:
    cursor.close()
    connection.close()