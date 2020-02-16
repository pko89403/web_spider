import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.daum.net")
soup = BeautifulSoup(res.content, 'html.parser')

# mydata = soup.find_all('a', 'link_issue')
mydata = soup.find_all('a', attrs={'class' : 'link_issue', 'tabindex' : '-1'})
for item in mydata:
    print(item.get_text())