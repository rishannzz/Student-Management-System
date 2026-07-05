# db_config.py
import mysql.connector
from mysql.connector import Error

def get_connection():
    """Establishes and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',          # Default MySQL username
            password='password', # Replace with your password
            database='student_management'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None