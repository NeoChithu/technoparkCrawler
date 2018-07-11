from bs4 import BeautifulSoup
import urllib2, sys, ssl
import mysql.connector
from datetime import datetime

cnx = mysql.connector.connect(host='localhost', user='root', password='', database='jobcrawler')
cursor_variable = cnx.cursor()

for i in range(245, 250):
    url = 'http://www.technopark.org/company-details?id='+str(i)
    # url = 'http://www.technopark.org/company-details?id=10364'
    header = {'User-Agent': 'Mozilla/5.0'} 
    req = urllib2.Request(url,headers=header)
    # page = urllib2.urlopen(req)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    info = urllib2.urlopen(req, context=gcontext).read()    
    soup = BeautifulSoup(info, 'html.parser')

    try:
        total_data = soup.find_all("div", {"class":"col-sm-4"})[0]
    except:
        total_data = False
        print str(i) + ' No Data'
    if total_data != False:

        print str(i) + ' Crawling Data'
        company_id = i
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
            except:
                description = ''
            
            try:
                if len(description) == 0:
                    description = additional_data.find_all("p", {"style":"text-align: justify;"})[0].text
                    description = description.encode(encoding='UTF-8',errors='strict')                
            except:
                description = ''            
    
            try:
                domain = additional_data.find_all("h7")[0].text
                domain = domain.encode(encoding='UTF-8',errors='strict')
            except:
                domain = ''

        SQL_QUERY = 'insert ignore into company_list(office_location, company_name, address, phone, email, website, description, domain, company_id, company_url)' \
                    'values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % \
                    (office_location, company_name, address, phone, email, website, description, domain, company_id, url)
        print SQL_QUERY
        cursor_variable.execute(SQL_QUERY)
        cnx.commit()
        # print description, domain
        total_data = False