# -*- coding: utf-8 -*-


import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# r = requests.get('http://127.0.0.1:5000/index/user', headers=headers)
# r = requests.get('http://127.0.0.1:5000/login', auth=('name','123456'))
token = 'bmFtZTowLjAyNDEwNzk0NTAyMjc6MTUxMDEzOTYzNy40Mg=='
r = requests.get('http://127.0.0.1:5000/test', params={'token': token})
print r.text
