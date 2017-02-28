#coding:utf-8

import urllib2
import urllib
import re
import time

def getWords(list,url=""):

    url2 =  "http://www.xiangqu.com/xiangqu/preSearchWords"
    url = url or url2

    for item in list:
        gic = urllib.quote(item)
        data = {
            "keyword": gic,
            "num": 10
        }

        headers = {
            "POST":url,
            "Host":'www.xiangqu.com',
            "Referer":'http://www.xiangqu.com/',
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
        }
        postData = urllib.urlencode(data)
        # print data
        req = urllib2.Request(url,postData)

        for key in headers:
            req.add_header(key,headers[key])

        html = urllib2.urlopen(req).read()

        print str(html)

        ss = re.findall("\"(.*?)\"",html)

        for item in ss:
            print item
        time.sleep(6)

list1 = ['s']
url = "http://www.xiangqu.com/im/getFilterWords"

getWords(list1,url)
