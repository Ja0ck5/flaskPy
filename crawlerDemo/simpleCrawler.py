# coding=utf-8
import urllib
import urllib2
import re

oUrl = "https://www.douyu.com/"


# html = urllib.urlopen(oUrl)
# content = html.read()
# # print 'src',content.find('src')
# # print content[2511:2612]
# print content
#
# statusCode = html.getcode()
# print statusCode
#
# url = html.geturl()
# print 'url:', url
#
# print html.info()
#
# # 下载到本地
# urllib.urlretrieve('https://rpic.douyucdn.cn/roomCover/2017/10/11/ac3979e806309af03ba712a88317829d.jpg',
#                    'D:/meizhi.jpg')


def getImg(htmlContent):
    imgList = re.findall(r'data-original="(.*?\.(jpg|png))"', htmlContent)
    x = 0
    for imgUrl in imgList:
        imgUrlReal = imgUrl[0]
        if imgUrlReal.endswith('jpg'):
            urllib.urlretrieve(imgUrlReal, 'D:/temp/%d.jpg' % x)
            print '完成下载 %s,本地地址: D:/temp/%d.jpg' % (imgUrlReal, x)
        else:
            urllib.urlretrieve(imgUrlReal, 'D:/temp/%d.png' % x)
            print '完成下载 %s,本地地址: D:/temp/%d.png' % (imgUrlReal, x)

        x += 1


def getHtmlContent(url):
    page = urllib.urlopen(url)
    return page.read()


# htmlContent = getHtmlContent(oUrl)
# getImg(htmlContent)
#
#
# urllib.urlretrieve('https://staticlive.douyucdn.cn/upload/signs/201710231811548748.jpg','D:/temp/broken.jpg')


# urllib2
# request = urllib2.Request(oUrl)
# response = urllib2.urlopen(request)
#
# with open("picture.jpg", "wb") as f:
#     f.write(response.read())
# print response.geturl()
# print response.info()  # 返回报文头信息
# print urllib2.urlopen(oUrl).read()


from bs4 import BeautifulSoup

html = urllib.urlopen(oUrl)
htmlContent = html.read()
soup = BeautifulSoup(htmlContent)

print soup.prettify()
# print soup.title
# print soup.p
# print soup.div
# print soup.img
# print soup.p.string

# print soup.img.attr
# print soup.select('.btn-2code')

