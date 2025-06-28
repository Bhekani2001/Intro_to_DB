import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (default user: root, no password)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Change if your root user has a password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
