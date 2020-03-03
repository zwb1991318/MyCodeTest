"""获取淘宝搜索信息爬虫联系"""
import re
import requests

URL_PRE = "https://s.taobao.com/search?q="
URL_SUF = "&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200303&ie=utf8"
URL_DELT = "&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s="
DELT_NUM = 44

def get_html(url_tb):
    """get html of mackbook pro 16 from taobao.com"""
    print(url_tb)
    mac_list = []
    try:
        response = requests.get(url_tb, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except ValueError:
        return ""

def parse_html(html_tb):
    """put html_tb to macbook pro 16 lsit"""
    print(html)
    mac_list = []
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html_tb)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html_tb)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            mac_list.append([price,title])
    except ValueError:
        print("valuie error")

    return mac_list

def print_macbook(maclist):
    """print macbook pro 16 list from taobao"""
    print(maclist)

if __name__ == "__main__":
    MACBOOK = "macbookpro16"
    SEARCH_URL = URL_PRE + MACBOOK + URL_SUF
    for i in range(3):
        try:
            if i == 0:
                url = SEARCH_URL
            else:
                url = SEARCH_URL + URL_DELT + str(DELT_NUM * i)

            html = get_html(url)
            info_list = parse_html(html)
        except ValueError:
            print("url failed")
            continue
    
    print_macbook(info_list)