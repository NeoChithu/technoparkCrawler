# Import Connetion.py for DB Instance
from connection import Database


def test_connection():
    
    # Creating a Connection
    new_instance = Database()
    cnx = new_instance.database_connector()
    cursor_variable = cnx.cursor()
    # Using the Connection
    try:
        SQL_Q = 'SELECT COUNT(*)  FROM company_list;'
        cursor_variable.execute(SQL_Q)
        row = cursor_variable.fetchall()
        print row
    except Exception as e:
        print "Exception Occured while Connecting to the Database"
        print "Error code:", e.errno        # error number
        print "SQLSTATE value:", e.sqlstate # SQLSTATE value
        print "Error message:", e.msg       # error message
        print "Error:", e                   # errno, sqlstate, msg values



if __name__ == '__main__':
    test_connection()