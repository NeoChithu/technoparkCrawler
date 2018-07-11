# SSL Context error was appearing to resolve the issue the SSl module of Python was used.
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

