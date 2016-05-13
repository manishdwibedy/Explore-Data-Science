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
    '''
    Computing the average interest rate
    :param db_connection:
    :return:
    '''

    average_grade = {}

    # Loop over all the tables
    for table in config.tables:
        # The data in tables other than 2015 has interest rate as string with a % symbol
        if '2015' not in table:
            query = "SELECT grade, AVG(CAST(TRIM(SUBSTRING(int_rate, 1, 6)) AS FLOAT)), COUNT(GRADE) from " + table \
                + " WHERE int_rate IS NOT NULL AND octet_length(int_rate) > 1 group by grade"
            rows = db.DB().query(db_connection, query)
        # The data in 2015 table has interest rate as float without the % symbol
        else:
            query = "SELECT grade, AVG(int_rate), COUNT(GRADE) from " + table \
                + " group by grade"
            rows = db.DB().query(db_connection, query)

        # Loop over every grade
        for row in rows:
            grade = row[0]
            average = row[1]
            count = row[2]

            # If the grade has already been seen, compute the weighted average
            if grade in average_grade:
                old_grade_data = average_grade[grade]

                # computing the weighted average
                final_average = (old_grade_data['average'] * old_grade_data['count'] + average * count) / (old_grade_data['count'] + count)
                average_grade[grade] = {
                    'average': final_average,
                    'count': old_grade_data['count'] + count
                }
            # If seeing the grade for the first time, then add it as it is
            else:
                average_grade[grade] = {
                    'average': average,
                    'count': count
                }
    return average_grade

if __name__ == '__main__':
    db_connection = get_db_connection()

    info = question_2(db_connection)

    print info