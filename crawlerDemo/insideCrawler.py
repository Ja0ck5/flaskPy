# coding=utf-8

import urllib2
import re


class SimpleSpider:
    # def lodPage(self, page):
    #     url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"
    #
    #     user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    #
    #     headers = {"User-Agent": user_agent}
    #
    #     req = urllib2.Request(url, headers=headers)
    #
    #     response = urllib2.urlopen(req)
    #
    #     html = response.read()
    #
    #     new_html = html.decode("GBK").encode("utf-8")
    #     return new_html


    def lodPage(self, page):
        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"

        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

        headers = {"User-Agent": user_agent}

        req = urllib2.Request(url, headers=headers)

        response = urllib2.urlopen(req)

        html = response.read()

        new_html = html.decode("GBK").encode("utf-8")

        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        item_list = pattern.findall(new_html)
        return item_list


# main
if __name__ == '__main__':
    # create spider
    mySpider = SimpleSpider()
    # the_page = mySpider.lodPage(1)
    # print the_page
    item_list = mySpider.lodPage(1)
    for item in item_list:
        print item.replace('<p>','').replace('</p>','').replace('<br />','')