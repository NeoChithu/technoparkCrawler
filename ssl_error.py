# url ="http://www.google.com"


# url = "http://technopark.org/job-search"
# header = {'User-Agent': 'Mozilla/5.0'} 
# req = urllib2.Request(url,headers=header)
# page = urllib2.urlopen(req)


# soup = BS(info, 'html.parser')

# input = input.replace("!web ", "")      
# url = "https://domainsearch.p.mashape.com/index.php?name=" + input
# req = urllib2.Request(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
# gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
# info = urllib2.urlopen(req, context=gcontext).read()
# Message.Chat.SendMessage ("" + info)

# domain_name = "http://www.technopark.org"
# url = str(domain_name)+"/job-search"
# header = {'User-Agent': 'Mozilla/5.0'} 
# req = urllib2.Request(url,headers=header)
# gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# info = urllib2.urlopen(req, context=gcontext).read()

# # page = urllib2.urlopen(req)
# soup = BeautifulSoup(info, 'html.parser')

# table_data = soup.find_all("tr", {"class":"companyList"})

import ssl, urllib2
from bs4 import BeautifulSoup

def get_data():
    url = "http://technopark.org/job-search"
    header = {'User-Agent': 'Mozilla/5.0'} 
    req = urllib2.Request(url,headers=header)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    info = urllib2.urlopen(req, context=gcontext).read()
    soup = BeautifulSoup(info, 'html.parser')
    # print soup
    
    table_data = soup.find_all("tr", {"class":"companyList"})    
    print table_data[0]

if __name__ == "__main__":
    get_data()

