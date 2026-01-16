# ROLE-2: SQL + Database
# Connect to MySQL and return connection + cursor

import mysql.connector
from config.db_config import DB_CONFIG

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)  # return rows as dicts
        return conn, cursor
    except mysql.connector.Error as err:
        print("MySQL Connection Error:", err)
        return None, None
