import psycopg2

dbname = "intern"
host = "payoff-showtime.ctranyfsb6o1.us-east-1.rds.amazonaws.com"
port = 5432
user = "payoff_intern"
password = 'reallysecure'

conn = psycopg2.connect(database=dbname, user=user, password=password, host=host, port=port, sslmode='require')

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

print 'Done'

