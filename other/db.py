import mysql.connector


def connect(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def query(conn, query):
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
    query(conn, create_table)

    insert_user = """INSERT INTO user (username, email, password) VALUES ('john', 'john@mail.com', 'hashed_password');"""

    query(conn, insert_user)


if __name__ == "__main__":
    connection = connect(host="erste", user="erste", password="erste", database="erste")
