from bs4 import BeautifulSoup
html = """<html> \
            <body> \
                <h1 id='title'>[1]크롤링이란?</h1> \
                <p class='csstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> \
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
            </body>
        </html>"""

soup = BeautifulSoup(html, 'html.parser')
# 태그로 검색 방법
data_h1 = soup.find('h1')
print(data_h1)
print(data_h1.string)
print(data_h1.get_text())

data_p = soup.find('p') 
print(data_p) # 근데 왜 하나만 나와?

# 동일한 태그의 항목을 원할 때
# ' find ' 라는 함수는 조건에 해당하는 첫번째 항목만 가져오고 끝이난다. 
# ' find ' 함수는 이후의 항목은 탐색하지 아니한다.
print("find Func Example ----")
find_detailed1 = soup.find('p', class_='csstyle')
print(find_detailed1.string)
find_detailed2 = soup.find('p', 'csstyle')
print(find_detailed2.string)
find_detailed3 = soup.find('p', attrs={'align' : 'center'})
print(find_detailed3)
find_detailed4 = soup.find(id='body')
print(find_detailed4)

# 여기서 우리는 모든 것을 들고 오기를 원한다! 진실을 요구한다!!!
print("find_all Func Example ----")
data_all = soup.find_all('p')
for item in data_all:
    print( item.string )