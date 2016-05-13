import db_connection
import sys

def get_db_connection():
    '''
    Getting the database connection.
    :return: the database connection object, if connection was successful.
    '''
    DB = db_connection.DB_Connection()
    connection = DB.getConnection()

    if connection:
        return connection
    else:
        sys.exit(1)


if __name__ == '__main__':
    get_db_connection()