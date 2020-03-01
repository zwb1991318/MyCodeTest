'''爬虫实例联系'''
import os
import requests

if __name__ == "__main__":
    URL = "https://item.jd.com/100011333796.html"
    USER_AGENT = {'user-agent':'Mozilla/5.0'}
    try:
        RESPONSE = requests.get(URL, headers=USER_AGENT)
        RESPONSE.raise_for_status()
        # print(RESPONSE.request.headers)
        # print(RESPONSE.status_code)
        # print(RESPONSE.encoding)
        # print(RESPONSE.text[:1000])
    except ValueError:
        print("error")

    URL2 = "http://www.baidu.com"
    URL2SEARCH = "/s?wd="
    KEYWORD = "周文彬"
    try:
        RESPONSE = requests.get(URL2+URL2SEARCH+KEYWORD, headers=USER_AGENT)
        print(RESPONSE.request.url)
        print(RESPONSE.status_code)
        RESPONSE.raise_for_status()
        # print(RESPONSE.text[:1000])
        # print(len(RESPONSE.text))
    except ValueError:
        print("baidu failed")

    URL_MAP = "http://www.gamersky.com/showimage/id_gamersky.shtml?http://img1.gamersky.com/image2020/02/20200227_ls_141_4/gamersky_026origin_051_20202271827A91.jpg"
    DIR = "C://Users//zwb//Desktop//"
    FILE = DIR + URL_MAP.split('/')[-1]
    print(FILE)
    try:
        if not os.path.exists(DIR):
            os.mkdir(DIR)
        if not os.path.exists(FILE):
            RESPONSE = requests.get(URL_MAP)
            print(RESPONSE.content)
            with open(FILE, 'wb') as f:
                f.write(RESPONSE.content)
                f.close()
        else:
            print("file exists")
    except ValueError:
        print("failed")

    
