import requests
from bs4 import BeautifulSoup
url = 'https://free-proxy-list.net/'
r = requests.get(url=url)
soup = BeautifulSoup(r.content,'lxml')
table = soup.find('div',attrs={'class':'table-responsive'}).find('table').find('tbody')

ip = list()
prt = list()
for tab in table:
    ipaddrss = tab.select('td:nth-of-type(1)')[0].text
    ip.append(ipaddrss)
    portnmbr = tab.select('td:nth-of-type(2)')[0].text
    prt.append(portnmbr)

    code = tab.select('td:nth-of-type(4)')[0].text
    ipdetail = tab.select('td:nth-of-type(5)')[0].text
    google = tab.select('td:nth-of-type(6)')[0].text
    https = tab.select('td:nth-of-type(7)')[0].text
    last_checked = tab.select('td:nth-of-type(8)')[0].text

proxyList = list()
for i in zip(ip,prt):
    proxyList.append(i)

datas = str()
for v, k in proxyList:
    datas += v+':'+k+'\n'

with open('proxy_list.txt','w') as f:
    f.write(datas)
