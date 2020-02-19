import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    inni_url = "https://item.jd.com/100005119668.html"
    res = requests.get(url=inni_url)
    soup = BeautifulSoup(res.content, "html.parser")

    #data = soup.find("div", class_="detail")

    """
    <div class='detail'>
        <div class='m m-content comment' id='comment'>
            <div class='mc'>
                <div class='J-comments-list comments-list ETab'>
                    <div class='tab-con'>
                        <div id='comment-0'>
                            <div comment-column J-comment-column>
                                <p class='comment-con'>

    """
    #hidcomment > div:nth-child(2) > div.i-item > div.comment-content

    comment_date = soup.select("div.detail div.date-buy")
    comments = soup.select("div.detail div.comment-content")
    
    for date, comment in zip(comment_date, comments):
        print(date.get_text(), "\t", comment.get_text(), '\n')

    "?callback=fetchJSON_comment98vv33&productId=100005119668&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1"
    params = {
        "callback": "fetchJSON_comment98vv33",
        "productId": "100005119668",
        "score": "0",
        "sortType": "5",
        "page": "1",
        "pageSize": "10",
        "isShadowSku": "0",
        "rid": "0",
        "fold": "1"}
    headers = {
        "Host": "club.jd.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "no-cors",
        "Referer": "https://item.jd.com/100005119668.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "__jda=122270672.15821141688521044410946.1582114169.1582114169.1582114169.1; __jdc=122270672; __jdv=122270672|direct|-|none|-|1582114168855; __jdu=15821141688521044410946; areaId=53283; 3AB9D23F7A4B3C9B=OY5C7P5G47GD2P7PWQPB3FDYRXGXLQFGRD46ZJX7MOMGZ32IQ2E2JRFMNBV2V6MY7OS6Q7U6GW6GXCQ4Z7RWOVA3IM; shshshfpa=891f1a01-1e30-679d-b15f-dcbeeace02a2-1582114291; shshshfpb=sgIejwIvmLutqo5lEfRFnPg%3D%3D; shshshfp=ac2c211586b1c6aed3d96fc0758c3ef1; ipLoc-djd=53283-53422-58662-0; jwotest_product=99; JSESSIONID=9314D985EF399C95627313B1114AFFD7.s1"

    }
    
    callback = requests.get(url="https://club.jd.com/comment/productPageComments.action",
                            headers=headers,
                            params=params)
    print('*' * 100)
    
    soup_page1 = BeautifulSoup(callback.content, "html.parser")
    data = soup_page1.find('content')
    
    print(soup_page1)
