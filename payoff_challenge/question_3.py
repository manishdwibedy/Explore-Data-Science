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

def question_3_maximum(db_connection):
    '''
    Computing the average interest rate on the basis of sub-grade
    :param db_connection:
    :return:
    '''

    average_grade = {}

    # Loop over all the tables
    for table in config.tables:
        # The data in tables other than 2015 has interest rate as string with a % symbol
        if '2015' not in table:
            query = "SELECT sub_grade, MAX(CAST(TRIM(SUBSTRING(int_rate, 1, 6)) AS FLOAT)), MIN(CAST(TRIM(SUBSTRING(int_rate, 1, 6)) AS FLOAT)) from " + table \
                + " WHERE int_rate IS NOT NULL AND octet_length(int_rate) > 1 group by sub_grade"
            rows = db.DB().query(db_connection, query)
        # The data in 2015 table has interest rate as float without the % symbol
        else:
            query = "SELECT sub_grade, MAX(int_rate), MIN(int_rate) from " + table \
                + " group by sub_grade"
            rows = db.DB().query(db_connection, query)



        # Loop over every grade
        for row in rows:
            subgrade = row[0]
            max = row[1]
            min = row[2]

            # If the grade has already been seen, compute the maximum
            if subgrade in average_grade:
                old_grade_data = average_grade[subgrade]

                # computing the new maximum and minimum
                new_max = average_grade[subgrade]['max']
                new_min = average_grade[subgrade]['min']
                max_year = average_grade[subgrade]['max_year']
                min_year = average_grade[subgrade]['min_year']

                if average_grade[subgrade]['max'] < max:
                    new_max = max
                    max_year = table[13:]
                if average_grade[subgrade]['min'] > min:
                    new_min = min
                    min_year = table[13:]

                average_grade[subgrade] = {
                    'max': new_max,
                    'max_year': max_year,
                    'min': new_min,
                    'min_year': min_year
                }
            # If seeing the grade for the first time, then assign it as it is
            else:
                average_grade[subgrade] = {
                    'max': max,
                    'max_year': table[13:],
                    'min': min,
                    'min_year': table[13:]
                }

    final_grade_info = {}
    for grade, grade_info in average_grade.iteritems():
        subgrade = grade[1:]
        grade = grade[:1]

        if grade in final_grade_info:
            final_grade_info[grade][subgrade] = grade_info
        else:
            final_grade_info[grade] = {subgrade: grade_info}

    return final_grade_info

def print_subgrade_info(sub_grade_info):
    '''
    Printing the average interest rate on the basis of sub-grade
    :param sub_grade_info: the computation of average interest rate on the basis of sub-grade
    :return: None
    '''
    grade_list = sub_grade_info.keys()

    for grade in sorted(grade_list):
        print 'Grade ' + grade

        sub_grade_list = sub_grade_info[grade].keys()
        for sub_grade in sorted(sub_grade_list):
            print 'Subgrade : ' + sub_grade
            print "\tMinimum Loan Rate : {0:.3f}%".format(sub_grade_info[grade][sub_grade]['min'])
            print "\tMinimum Loan Year : " + sub_grade_info[grade][sub_grade]['min_year'].replace('_', '-')
            print "\tMaximum Loan Rate : {0:.3f}%".format(sub_grade_info[grade][sub_grade]['max'])
            print "\tMaximum Loan Year : " + sub_grade_info[grade][sub_grade]['max_year']

        print '\n\n'

if __name__ == '__main__':
    db_connection = get_db_connection()

    print '\n\nSegregating on the basis of sub_grades'
    info = question_3_maximum(db_connection)

    print_subgrade_info(info)