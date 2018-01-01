#Python 3.5

import requests
from bs4 import BeautifulSoup

def save_result(host):

    filename = 'proxy_list.txt'
    result = str(host)

    try:
        file = open(filename,'at')
    except IOError as e:
        print('error opening file')
    else:
        with file:
            file.write(result + '\n')
            file.close()
    print(str(result) + ' was saved to result.txt')


site_url = 'https://www.ip-adress.com/proxy-list'
html_doc = requests.get(site_url)

soup = BeautifulSoup(html_doc.text, 'html.parser')

table = soup.find("table")
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 4:
        save_result(cells[0].text)