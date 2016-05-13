import db_connection

def get_db_connection():
    DB = db_connection.DB_Connection()
    connection = DB.getConnection()

    if connection:
        return connection


if __name__ == '__main__':
    get_db_connection()