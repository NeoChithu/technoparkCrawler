import mysql.connector, sys

class Database():
    def database_connector(self):
        try:
            cnx = mysql.connector.connect(host='localhost', user='root', password='', database='jobcrawler')
            # cursor_variable = cnx.cursor()
            return cnx
        except Exception as e:
            print "Exception Occured while Connecting to the Database"
            print "Error code:", e.errno        # error number
            print "SQLSTATE value:", e.sqlstate # SQLSTATE value
            print "Error message:", e.msg       # error message
            print "Error:", e                   # errno, sqlstate, msg values
            sys.exit()   
        