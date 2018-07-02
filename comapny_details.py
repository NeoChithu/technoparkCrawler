from bs4 import BeautifulSoup
import urllib2, sys
import mysql.connector
from datetime import datetime

# Database Connection Related Imports
import sys
sys.path.insert(0, sys.path[0]+'\\database')
from connection import Database
# Creating a Connection
new_instance = Database()
cnx = new_instance.database_connector()
cursor_variable = cnx.cursor()

def add_data(url):
    
    url = url
    company_id = url.split('?id=')[1]
    print url
    
# for i in range(1, 250):
#     url = 'http://www.technopark.org/company-details?id='+str(i)
#     company_id = i
    header = {'User-Agent': 'Mozilla/5.0'} 
    req = urllib2.Request(url,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')

    try:

        total_data = soup.find_all("div", {"class":"col-sm-4"})[0]

    except:

        total_data = False
        # print (' No Data')

    if total_data != False:

        # print (' Crawling Data')
        list_data = total_data.find_all("li", {"class":""})
        office_location = company_name = address = phone = email = website = ''
        
        for data in list_data:
            
            newblock = data.text.encode(encoding='UTF-8',errors='strict')

            if "Office Location" in newblock:

                office_location = newblock
                office_location = office_location.replace('Office Location', '').strip()
            
            elif "company name" in newblock:

                company_name = newblock
                company_name = company_name.replace('company name', '').strip()

            elif "address" in newblock:

                address = newblock
                address = address.replace('address', '').strip()

            elif "pin" in newblock:

                pin = newblock
                pin = pin.replace('pin', '').strip()
            
            elif "phone" in newblock:

                phone = newblock
                phone = phone.replace('phone', '').strip()

            elif "email" in newblock:

                email = newblock
                email = email.replace('email', '').strip()

            elif "website" in newblock:

                website = newblock
                website = website.replace('website', '').strip()
        # print office_location, company_name, address, phone, email, website
        try:

            additional_data = soup.find_all("div", {"class":"col-sm-8"})[0]

        except:

            additional_data = False
            description = domain = ''
            
        if additional_data != False:

            try:

                description = additional_data.find_all("div", {"style":"text-align: justify;"})[0].text
                description = description.encode(encoding='UTF-8',errors='strict')
                description = description.replace('"', '')
                description = description.replace('\xc2','').replace('\xa0', '').replace('\n').replace('\r', '')               
                description = description.decode(encoding='UTF-8',errors='strict')

            except:

                description = ''
            
            try:

                if len(description) == 0:

                    description = additional_data.find_all("p", {"style":"text-align: justify;"})[0].text
                    description = description.encode(encoding='UTF-8',errors='strict') 
                    description = description.replace('\xc2','').replace('\xa0', '').replace('\n').replace('\r', '')               
                    description = description.decode(encoding='UTF-8',errors='strict')

            except:

                description = ''            
    
            try:

                domain = additional_data.find_all("h7")[0].text
                domain = domain.encode(encoding='UTF-8',errors='strict')

            except:

                domain = ''

        try:

            # print (office_location, company_name, address, phone, email, website, description, domain, company_id, url)
            SQL_QUERY = 'insert ignore into company_list(office_location, company_name, address, phone, email, website, description, domain, company_id, company_url)' \
                        'values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % \
                        (office_location, company_name, address, phone, email, website, description, domain, company_id, url)
            # print (SQL_QUERY)
            cursor_variable.execute(SQL_QUERY)
            cnx.commit()

        except Exception as e:

            # print (office_location, company_name, address, phone, email, website, description, domain, company_id, url)
            print "Exception Occured while Inserting data to DB File company_details.py"

        total_data = False


# link = "http://www.technopark.org/company-details?id=10347"
# link = "http://www.technopark.org/company-details?id=10137"
# link = "http://www.technopark.org/company-details?id=9548"
# company_id = 10137
# link = "http://www.technopark.org/company-details?id=9548"
# add_data(link)   