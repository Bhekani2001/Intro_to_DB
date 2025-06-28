import mysql.connector
from mysql.connector import Error  # Important: needed for exception type

def create_database():
    connection = None

    try:
        # Connect to MySQL (update password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Philani@_2001'  # Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Use exact database name: alxbookstore
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
            print("Database 'alxbookstore' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
