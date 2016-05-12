import psycopg2

dbname = "intern"
host = "payoff-showtime.ctranyfsb6o1.us-east-1.rds.amazonaws.com"
port = 5432
user = "payoff_intern"
password = 'reallysecure'

conn = psycopg2.connect(database=dbname, user=user, password=password, host=host, port=port, sslmode='require')

print 'Done'