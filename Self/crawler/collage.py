"""Test get imfo Univ"""
import requests
from bs4 import BeautifulSoup
import bs4

def get_html_text(url):
    """use requests to get info from website"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except ValueError:
        return ""

def fill_univ_list(html):
    """use requehtmls to get univ info to list"""
    ulist = []
    soup = BeautifulSoup(html, "html.parser")
    for body_tr in soup.find('tbody').children:
        if isinstance(body_tr, bs4.element.Tag):
            tds = body_tr("td")
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

    return ulist

def print_univ_list(univ_list, num):
    """print univ info list"""
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校", "总分", chr(12288)))
    for i in range(num):
        univ = univ_list[i]
        print(tplt.format(univ[0], univ[1], univ[2], chr(12288)))

if __name__ == "__main__":
    URL = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    print_univ_list(fill_univ_list(get_html_text(URL)), 20)
