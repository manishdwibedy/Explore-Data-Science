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

print 'Number of rows : ' + str(rows[0][0])

cur.execute("""SELECT SUM(funded_amnt) from lending_club_2007_2011""")

rows = cur.fetchall()

print 'Total loan amount : ' + str(rows[0][0])


print 'Done'