import mysql.connector
from mysql.connector import Error


#connection function
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print("Connection Established Successfully.")
    except Error as e:
        print(f"The error '{e} has occured.")
    return connection
conn = create_connection("cis3368.cnul0adngz4b.us-east-2.rds.amazonaws.com", "admin", "Password!", "cis3368") #Info to connect to DB
cursor = conn.cursor(dictionary=True)
