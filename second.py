from bs4 import BeautifulSoup
import urllib2, sys
import mysql.connector
from datetime import datetime

# Database Connection Related Imports
import sys, ssl
sys.path.insert(0, sys.path[0]+'\\database')
from connection import Database
# Creating a Connection
new_instance = Database()
cnx = new_instance.database_connector()
cursor_variable = cnx.cursor()

def job_details(url):
    # print url
    header = {'User-Agent': 'Mozilla/5.0'} 
    req = urllib2.Request(url,headers=header)
    # page = urllib2.urlopen(req)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    info = urllib2.urlopen(req, context=gcontext).read()    
    soup = BeautifulSoup(info, 'html.parser')
    total_data = soup.find_all("div", {"class":"det-text group-effect1 arrived"})[0]
    data = total_data.find_all("a", href= True)

    mail_id = ''

    for d in data:
        
        if 'mailto:' in d['href']:

            mail_id = d['href']
            mail_id = mail_id.replace('mailto:','')

        else:

            pass
    # print mail_id
    block_data = total_data.find_all("div", {'class':'block'})
    # print block_data[5]
    walkin = False
    description = skills = walkin_venu = ''

    for block in block_data:

        newblock = ''
        # newblock = block.text.decode(encoding='UTF-8',errors='strict')

        try:

            newblock = block.text.replace("'", "\\'")
            newblock = newblock.encode(encoding='UTF-8',errors='strict')
            
        except:

            newblock = ''
            # print "Block ERROR"

        # print newblock
        if 'Brief description :' in newblock:

            description = newblock

        elif 'Preferred skills' in newblock:

            skills = newblock     

        elif 'Walk in venue' in newblock:

            walkin_venu = newblock  
            walkin = True

        else:
            pass

    try:

        SQL_Q = 'select id from technopark where apply_link = "'+str(url)+'"'
        cursor_variable.execute(SQL_Q)
        row = cursor_variable.fetchone()
        # print row[0]

    except Exception as e:

        print "Exception Occured while Selecting data to DB File second.py"
        print "Error code:", e.errno        # error number
        print "SQLSTATE value:", e.sqlstate # SQLSTATE value
        print "Error message:", e.msg       # error message
        print "Error:", e                   # errno, sqlstate, msg values

    try:

        SQL = "UPDATE technopark set mail_id = '"+str(mail_id)+"', walkin = '"+str(walkin)+"', description = '"+str(description)+"', walkin_venu = '"+str(walkin_venu)+"', skills = '"+str(skills)+"' where id = "+str(row[0])
        # print (SQL)
        cursor_variable.execute(SQL)
        cnx.commit()

    except Exception as e:

        print "Exception Occured while Writing data to DB File second.py"
        print "Error code:", e.errno        # error number
        print "SQLSTATE value:", e.sqlstate # SQLSTATE value
        print "Error message:", e.msg       # error message
        print "Error:", e                   # errno, sqlstate, msg values

