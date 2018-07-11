
# Imports Related For Beautiful Soup
from bs4 import BeautifulSoup
import urllib2, sys
from datetime import datetime
import mysql.connector

# Import Related to Get Company Details
from comapny_details import add_data

# Imports Related to Get Job Description
from second import job_details

# Database Connection Related Imports
import sys
sys.path.insert(0, sys.path[0]+'\\database')
from connection import Database

import ssl

# Creating a Connection
new_instance = Database()
cnx = new_instance.database_connector()
cursor_variable = cnx.cursor()

def insert_date():

    # add_data("http://www.technopark.org/company-details?id=9548")
    # sys.exit()
    domain_name = "http://www.technopark.org"
    url = "http://technopark.org/job-search"
    header = {'User-Agent': 'Mozilla/5.0'} 
    req = urllib2.Request(url,headers=header)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    info = urllib2.urlopen(req, context=gcontext).read()
    soup = BeautifulSoup(info, 'html.parser')
    # print soup
    table_data = soup.find_all("tr", {"class":"companyList"})    
    
    count = company_count = 0

    for table in table_data:
    
        apply_link = table.find("a", {'class' : 'jobTitleLink'})
        position = apply_link.text
        apply_link = str(domain_name)+'/'+apply_link['href']
        company_url = table.find_all("a", href= True)
        company_name = company_url[1].text
        company_url = str(domain_name)+company_url[1]['href']
        
        try:

            company_id = company_url.split('id=')
            company_id = company_id[1]
            
        except:

            company_id = ''

        try:

            closing_date = table.find_all("td")
            closing_date = closing_date[-1].text

            closing_date = datetime.strptime(closing_date, "%d/%m/%Y").strftime("%Y/%m/%d")

        except:

            closing_date = ''

        try:

            SQL_QUERY = 'insert ignore into technopark(company_name, position, apply_link, company_url, company_id, closing_date)' \
                        'values("%s","%s","%s","%s","%s","%s")' % \
                        (company_name, position, apply_link, company_url, company_id, closing_date)
            cursor_variable.execute(SQL_QUERY)
            cnx.commit()
            affected_rowcount = cursor_variable.rowcount
            count = count + 1
        except Exception as e:

            # print e
            print "Exception Occured while Inserting data to DB File main.py"
            print "Error code:", e.errno        # error number
            print "SQLSTATE value:", e.sqlstate # SQLSTATE value
            print "Error message:", e.msg       # error message
            print "Error:", e                   # errno, sqlstate, msg values
            affected_rowcount = 0

        if affected_rowcount == 1:

            print "Data Storing count " + str(count)

            job_details(apply_link)

            try:

                SQL = "SELECT * from company_list where company_id = " + str(company_id)
                cursor_variable.execute(SQL)
                row = cursor_variable.fetchone()

            except Exception as e:

                print "Exception Occured while Selecting data to DB File main.py"
                print "Error code:", e.errno        # error number
                print "SQLSTATE value:", e.sqlstate # SQLSTATE value
                print "Error message:", e.msg       # error message
                print "Error:", e                   # errno, sqlstate, msg values                
                row = 0

            if row is None:
                company_count = company_count + 1
                print "Company Storing count " + str(company_count)
                add_data(company_url)
            

if __name__ =="__main__":
    insert_date()
    # add_data("http://www.technopark.org/company-details?id=9548")