import urllib

oUrl = "https://www.douyu.com/"
html = urllib.urlopen(oUrl)
content = html.read()
print content

statusCode = html.getcode()
print statusCode

url = html.geturl()
print 'url:', url

print html.info()

# 下载到本地
urllib.urlretrieve('https://rpic.douyucdn.cn/roomCover/2017/10/11/ac3979e806309af03ba712a88317829d.jpg',
                   'D:/meizhi.jpg')
