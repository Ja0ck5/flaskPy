# coding=utf-8

import urllib2


class SimpleSpider:
    def lodPage(self, page):
        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"

        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

        headers = {"User-Agent": user_agent}

        req = urllib2.Request(url, headers=headers)

        response = urllib2.urlopen(req)

        html = response.read()

        new_html = html.decode("GBK")

        return new_html

# main
if __name__ == '__main__':
    # create spider
    mySpider = SimpleSpider()
    the_page = mySpider.lodPage(1)
    print the_page