# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

session = requests.Session()

rreq = session.get(url='http://basetest.m9kj-team.com:9999/login.php')
soup = BeautifulSoup(rreq.text,'html.parser')
user_token = soup.find('input',type='hidden')['value']
print(user_token)
session.post(url='http://basetest.m9kj-team.com:9999/login.php', data={
    "username": "admin",
    "password": "password",
    'Login': 'Login',
    'user_token': user_token
})

ssr = session.get('http://basetest.m9kj-team.com:9999/security.php')
print(ssr.text)

soup = BeautifulSoup(ssr.text,'html.parser')
all = soup.find('form',method='POST').p.em.string
print(all)
