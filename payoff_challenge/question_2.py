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

# SELECT grade, AVG(CAST(substring(int_rate from '.*%')) AS INTEGER ) from lending_club_2007_2011

def question_2(db_connection):

    average_grade = {}
    for table in config.tables:
        # overlay(int_rate placing '' for 1 from 5 )
        if '2015' not in table:
            query = "SELECT grade, AVG(CAST(TRIM(SUBSTRING(int_rate, 1, 6)) AS FLOAT)), COUNT(GRADE) from " + table \
                + " WHERE int_rate IS NOT NULL AND octet_length(int_rate) > 1 group by grade"
            rows = db.DB().query(db_connection, query)
        else:
            query = "SELECT grade, AVG(int_rate), COUNT(GRADE) from " + table \
                + " group by grade"
            rows = db.DB().query(db_connection, query)
        for row in rows:
            grade = row[0]
            average = row[1]
            count = row[2]
            if grade in average_grade:
                old_grade_data = average_grade[grade]
                final_average = (old_grade_data['average'] * old_grade_data['count'] + average * count) / (old_grade_data['count'] + count)
                average_grade[grade] = {
                    'average': final_average,
                    'count': old_grade_data['count'] + count
                }
            else:
                average_grade[grade] = {
                    'average': average,
                    'count': count
                }
    pass




if __name__ == '__main__':
    db_connection = get_db_connection()

    info = question_2(db_connection)

    pass