import psycopg2
import config
import os
import sys

# By default the username and password have not been found
userNameFound = False
passwordFound = False

# Checking if the username is present in the environment variable
if 'username' in os.environ:
    user = os.environ.data['username']
    userNameFound = True

# Checking if the password is present in the environment variable
if 'password' in os.environ:
    password = os.environ['password']
    passwordFound = True

# If either username or password was not found, then exit displaying the erro
if not userNameFound or not passwordFound:
    print 'Please enter the username and password of the database in the environment variables.'
    sys.exit(1)

conn = psycopg2.connect(database=config.dbname, user=user, password=password, host=config.host, port=config.port, sslmode='require')

cur = conn.cursor()

cur.execute("""SELECT COUNT(id) from lending_club_2007_2011""")

rows = cur.fetchall()

# print 'Number of rows : ' + str(rows[0][0])

cur.execute("""SELECT SUM(funded_amnt) from lending_club_2007_2011""")

rows = cur.fetchall()

# print 'Total loan amount : $ ' + str(rows[0][0])

cur.execute("""SELECT *
FROM lending_club_2007_2011
LIMIT 1""")

rows = cur.fetchall()

# print 'One row data ' + str(rows[0])

print '---Question 1---\n\n'
print '\n\nTotal Monthly Loan Amount :'
cur.execute("""SELECT SUM(funded_amnt),issue_d from lending_club_2007_2011 GROUP BY issue_d ORDER BY issue_d DESC """)

rows = cur.fetchall()

for row in rows:
    month = str(row[1])
    amount = str(row[0])
    if row[0]:
        print 'Month : ' + month
        print 'Amount $: ' + amount

print '\n\nAverage Monthly Loan Amount :'
cur.execute("""SELECT AVG(funded_amnt),issue_d from lending_club_2007_2011 GROUP BY issue_d ORDER BY issue_d DESC """)

rows = cur.fetchall()

for row in rows:
    month = str(row[1])
    amount = str(row[0])
    if row[0]:
        print 'Month : ' + month
        print 'Amount $: ' + amount


print '\n\nAverage Monthly Loan Amount :'
cur.execute("""SELECT AVG(funded_amnt),issue_d from lending_club_2007_2011 GROUP BY issue_d ORDER BY issue_d DESC """)

rows = cur.fetchall()

for row in rows:
    month = str(row[1])
    amount = str(row[0])
    if row[0]:
        print 'Month : ' + month
        print 'Amount $: ' + amount


print '\n\nNumber of grades :'
cur.execute("""SELECT COUNT(*) from lending_club_2007_2011 GROUP BY grade""")

rows = cur.fetchall()

print 'Number of grades : ' + str(len(rows))

print '\n\nAverage Rate as per the grade :'
cur.execute("""SELECT grade, int_rate from lending_club_2007_2011""")

rows = cur.fetchall()

grade_data = []
for row in rows:
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

