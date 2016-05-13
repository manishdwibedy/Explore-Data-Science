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

    total_rows = []
    for table in config.tables:
        query = "SELECT SUM(funded_amnt),issue_d from " + table + " GROUP BY issue_d ORDER BY issue_d DESC"
        rows = db.DB().query(db_connection, query)
        total_rows.extend(rows)

    loan_info = {}
    for loan in total_rows:
        total_amount = loan[0]
        date = loan[1]

        date_info = date.split('-')
        if len(date_info) == 2:
            month = date_info[0]
            year = date_info[1]

            if year in loan_info:
                data = loan_info[year]
                data.append({
                    'month': month,
                    'amount': total_amount
                })
            else:
                data = []
                data.append({
                    'month': month,
                    'amount': total_amount
                })
                loan_info[year] = data
        else:
            print 'Invalid date'
    return loan_info

if __name__ == '__main__':
    db_connection = get_db_connection()

    question_1(db_connection)