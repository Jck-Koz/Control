import mysql.connector
from mysql.connector import Error

# Global variable for the connection
connection = None


def create_connection():
    global connection
    if connection is None or not connection.is_connected():
        try:
            connection = mysql.connector.connect(
               
            )
            if connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: '{e}'")
    return connection


def close_connection():
    global connection
    if connection and connection.is_connected():
        connection.close()
        connection = None
        print("MySQL connection is closed")


def check_connection(conn):
    if conn is None or not conn.is_connected():
        conn = create_connection()
    return conn

        