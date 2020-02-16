import requests
from bs4 import BeautifulSoup
# 크롤링 -> 웹사이트에서 내가 원하는 것을 추출해내는 기능
if __name__ == "__main__":
    # 웹페이지 주소를 복사해서 requests.get()을 이용해서 가져온다.
    res = requests.get('http://v.media.daum.net/v/20170615203441266')
    # 페이지 소스 보기 - 뭔가 이상한 구조의 코드 들이 나온다. -> HTML5
    # print(res.content, '\n')
    # BeautifulSoup 가 HTML을 파싱함
    # html.parser 여러가지 파서가 있는데 가장 기본적인 파서
    soup = BeautifulSoup(res.content, 'html.parser')
    # 필요한 데이터 추출하기
    # soup.find() 함수로 원하는 부분을 지정
    # 함수 get_text로 원하는 결과를 추출한다.
    mydata = soup.find('title')
    print( mydata.get_text() )
