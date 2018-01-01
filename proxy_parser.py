import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from urllib.request import urlopen


site_url = 'https://www.ip-adress.com/proxy-list'
html_doc = requests.get(site_url)

soup = BeautifulSoup(html_doc.text, 'html.parser')
#print(soup.prettify())

for el in soup.find_all('a'):
    #print (el)
    continue

table = soup.table
#print(table.contents[0])


table = soup.find("table")
for row in table.findAll("tr"):
    cells = row.findAll("td")
    for cell in cells:
        print(cell.text)
