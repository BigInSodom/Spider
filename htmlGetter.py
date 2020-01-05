from bs4 import BeautifulSoup
from urllib import request,parse;
import lxml
import json
import class1

url = "http://jwglxt.qau.edu.cn/jsxsd1/kbcx/kbxx_classroom_ifr"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
         "Cookie": "JSESSIONID=8C822C5266AFC44C5DC70F337EE1045A"}

formdata = {
    "xnxqh": "2019-2020-2",
    "skyx": "",
    "xqid": "1",
    "jzwid": "",
    "zc1": "",
    "zc2": "",
    "jc1": "", 
    "jc2": ""
}

data = parse.urlencode(formdata).encode('utf-8')
req = request.Request(url=url, data = data, headers = headers)
response = request.urlopen(req)

print (response.read().decode("utf-8"))
fo = open("D://newdemo.txt", "w+")
fo.write( response.read().decode("utf-8"));
fo.close()
