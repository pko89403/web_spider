import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    
    res = requests.get('https://news.v.daum.net/v/20170615203441266')
    soup = BeautifulSoup(res.content, 'html.parser')

    mydata = soup.find_all('span', 'txt_info') # return list
    for item in mydata:
        print( item.string )

    # 우리는 기사를 스크랩하기 위해서 <p>를 크롤링하기를 원한다.
    # 그런데 이 <p>는 특정 클래스가 없네?
    # 그 위를 덮는 class를 찾는다. 거슬러 거슬러 올라간다.
    paragraph = soup.find('div', 'layer_util layer_summary')
    print( paragraph.get_text() )

    # 크롤링 후처리
    # \n, 불필요한 데이터 삭제, 깔끔하게 문자열 정리
    