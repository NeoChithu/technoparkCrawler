from bs4 import BeautifulSoup
import urllib2, sys
import mysql.connector
from datetime import datetime

url = "http://www.technopark.org/job-detail?cmpid=10364&vacancy_id=14347"
# url = "http://www.technopark.org/job-detail?cmpid=228&vacancy_id=14343"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(url,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

total_data = soup.find_all("div", {"class":"det-text group-effect1 arrived"})[0]

data = total_data.find_all("a", href= True)

mail_id = ''

for d in data:

    # print d['href']
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

    newblock = block.text.encode(encoding='UTF-8',errors='strict')
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

# # Company Infos
# company_data = soup.find_all("div", {"class":"col-sm-4 shade"})[0]

# add_data = company_data.find_all("div", {'class':'tit'})

# print add_data