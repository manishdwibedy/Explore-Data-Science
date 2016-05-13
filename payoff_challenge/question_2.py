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

def question_2(db_connection):

    total_rows = []
    for table in config.tables:
        query = "SELECT grade, int_rate from " + table
        rows = db.DB().query(db_connection, query)
        total_rows.extend(rows)


    grade_data = []
    for row in total_rows:
        grade = str(row[0])
        interest = str(row[1])
        if len(interest) > 0:
            interest = interest.replace('%', '')
            grade_data.append({
                'grade': grade,
                'interest': interest
            })

    grade_distribution = {}
    for grade in grade_data:
        if grade['grade'] in grade_distribution:
            grade_info = grade_distribution[grade['grade']]
            grade_distribution[grade['grade']] = {
                'sum': grade_info['sum'] + float(grade['interest']) ,
                'count': grade_info['count'] + 1
            }
        else:
            grade_distribution[grade['grade']] = {
                'sum': float(grade['interest']),
                'count': 1
            }

    for grade, grade_info in grade_distribution.iteritems():
        print 'Grade ' + grade
        print 'Average Interest : ' + str(grade_info['sum'] / grade_info['count']) + '%'
    print 'Done'

if __name__ == '__main__':
    db_connection = get_db_connection()

    info = question_2(db_connection)

    pass