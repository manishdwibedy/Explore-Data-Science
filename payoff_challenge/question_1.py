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
        query = "SELECT SUM(funded_amnt), AVG(funded_amnt), issue_d from " + table + " GROUP BY issue_d ORDER BY issue_d DESC"
        rows = db.DB().query(db_connection, query)
        total_rows.extend(rows)

    total_monthly_loan_info = {}
    average_monthly_loan_info = {}
    for loan in total_rows:
        total_amount = loan[0]
        average_amount = loan[1]
        date = loan[2]

        date_info = date.split('-')
        if len(date_info) == 2:
            month = date_info[0]
            year = date_info[1]

            if year in total_monthly_loan_info:
                data = total_monthly_loan_info[year]
                data.append({
                    'month': month,
                    'amount': total_amount
                })

                data1 = average_monthly_loan_info[year]
                data1.append({
                    'month': month,
                    'amount': average_amount
                })
            else:
                data = []
                data1 = []
                data.append({
                    'month': month,
                    'amount': total_amount
                })
                data1.append({
                    'month': month,
                    'amount': average_amount
                })
                total_monthly_loan_info[year] = data
                average_monthly_loan_info[year] = data1
        else:
            print 'Invalid date'
    return {
        'average': average_monthly_loan_info,
        'total': total_monthly_loan_info
    }

if __name__ == '__main__':
    db_connection = get_db_connection()

    info = question_1(db_connection)

    pass