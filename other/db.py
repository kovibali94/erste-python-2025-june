import mysql.connector
# pip install mysql-connector-python


def connect(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def run_query(conn, query):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()


def init(conn):
    create_table = """CREATE TABLE user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"""
    run_query(conn, create_table)

    insert_user = """INSERT INTO user (username, email, password) VALUES ('john', 'john@mail.com', 'hashed_password');"""

    run_query(conn, insert_user)
    
    connection.commit()


if __name__ == "__main__":
    connection = connect(
        host="localhost", user="erste", password="erste", database="erste"
    )
    # init(connection)
    query = "SELECT * FROM user;"
    results = run_query(connection, query)
    if results:
        for row in results:
            print(row)
