import os
import psycopg2
import config

class DB(object):
    def __init__(self):
        # By default the username and password have not been found
        self.error = False

    def getInput(self):
        # Checking if the username is present in the environment variable
        if 'username' in os.environ:
            self.user = os.environ.data['username']
            userNameFound = True

        # Checking if the password is present in the environment variable
        if 'password' in os.environ:
            self.password = os.environ['password']
            passwordFound = True

        # If either username or password was not found, then raise exception
        if not userNameFound or not passwordFound:
            self.error = True
            raise EnvironmentError('Please enter the username and password of the database in the environment variables.')

    def getConnection(self):
        self.getInput()
        if not self.error:
            try:
                conn = psycopg2.connect(database=config.dbname, user=self.user, password=self.password, host=config.host, port=config.port, sslmode='require')
                return conn
            except psycopg2.OperationalError, error:
                print 'Error occurred!!'
                print error
                return None
        else:
            return None

if __name__ == '__main__':
    print DB().getConnection()