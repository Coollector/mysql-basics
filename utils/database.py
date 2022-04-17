import mysql.connector
from mysql.connector import Error




#"""
#All MYSQL - actions you could think of
#"""

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print(f"\n\nConnection to '{host_name}' was succeful with user '{user_name}'\n\n")
    except Error as err:
        print(f"\n\nError in create_server_connection:\n'{err}'\n\n")

    return connection



def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(f"\n\nConnected to '{db_name}' at '{host_name}' with user: '{user_name}'\n\n")
    except Error as rr:
        print(f"\n\nError in create_db_connection:\n'{err}'\n\n")

    return connection



def create_database(connection, name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {name};")
        cursor.close()
        cursor = connection.cursor()
        print(f"\n\nDatabase '{name}' created successfully\n\n")
    except Error as err:
        print(f"\n\nError in create_database:\n'{err}'\n\n")



def create_table(connection, db_name, table_name, parameters):
    cursor = connection.cursor()
    current_db = read_query(connection, f"SELECT DATABASE();")
    if current_db != db_name:
        try:
            cursor.execute(f"USE {db_name};")
            cursor.close()
            cursor = connection.cursor()
        except Error as err:
            print(f"\n\nError in create_table (use other database):\n'{err}'\n\n")
            return None
    try:
        cursor.execute(f"CREATE TABLE {table_name} ({parameters});")
        cursor.close()
        cursor = connection.cursor()
    except Error as err:
        print(f"\n\nError in create_table:\n'{err}'\n\n")



def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.fetchall()
        cursor.close()
        cursor = connection.cursor()
        print(f"\n\nExecuted\n'{query}'\nsuccessfully\n\n")
    except Error as err:
        print(f"\n\nError in execute_query:\n'{err}'\n\n")



def execute_list_query(connection, query, values):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, values)
        connection.commit()
        cursor.close()
        cursor = connection.cursor()
        print("\n\nexecute_list_query successfully finished\n\n")
    except Error as err:
        print(f"\n\nError in execute_list_query:\n'{err}'\n\n")




def read_query(connection, query, print_succes=True):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        if print_succes:
            print(f"\n\nread_query successfully finished:\n{query}\n\n")
            print_succes = True
        result = cursor.fetchall()
        cursor.close()
        cursor = connection.cursor()
        return result
    except Error as err:
        print(f"\n\nError in read_query:\n'{err}'\n\n")
