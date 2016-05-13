import db
import sys
import config

def get_db_connection():
    '''
    Getting the database connection.
    :return: the database connection object, if connection was successful.
    '''
    DB = db.DB()
    connection = DB.getConnection()

    if connection:
        return connection
    else:
        sys.exit(1)

def question_1(db_connection):

    for table in config.tables:
        query = "SELECT SUM(funded_amnt),issue_d from " + table + " GROUP BY issue_d ORDER BY issue_d DESC"
        rows = db.DB().query(db_connection, query)
        pass

if __name__ == '__main__':
    db_connection = get_db_connection()

    question_1(db_connection)