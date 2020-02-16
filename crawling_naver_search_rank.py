import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(res, 'html.parser')
hotKeys = soup.select("ah_roll_area")
print(hotKeys)

index = 0
for key in hotKeys:
    index += 1
    print(str(index) + ", " + key.text)
    if index >= 20:
        break


# find()의 결과에서
# 다시 한번 더 find()를 한다."김원준") )
#mydata = soup.find_all("div", class_="ah_list")
#print(mydata)
#items = mydata.find_all('span', 'ah_k')
#for item in items:
#    print(item)