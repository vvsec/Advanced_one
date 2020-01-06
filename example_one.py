# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup


#公用变量
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
loginurl = 'http://basetest.m9kj-team.com:9999/login.php'
levelurl = 'http://basetest.m9kj-team.com:9999/security.php'

#请求区域
def gen():
    pass
    # req = requests.get(url=loginurl,headers=header)
    # res = req.text
    # print(res)
    # data = {
    #     'username':'admin',
    #     'password':'password',
    #     'Login' : 'Login',
    #     'user_token':'a671219a354dffb0259288d55a238aa8'
    # }
    # req_post = requests.post(url=loginurl,headers=header,data=data)
    # res_post = req_post.text
    # print(res_post)
def sp(user,pwd):
    session = requests.Session()
    req = session.get(url=loginurl,headers=header)
    res = req.text
    # print(res)
    soup = BeautifulSoup(res,'html.parser')
    token = soup.find('input',{'name':'user_token'})['value']
    # print(target)
    data = {
        'username':user,
        'password':pwd,
        'Login': 'Login',
        'user_token': token
    }
    session.post(url=loginurl,data=data,headers=header)
    secreq = session.get(url=levelurl,headers=header)
    # print(secreq.text)
    #获取impossible
    soup_level = BeautifulSoup(secreq.text,'html.parser')
    result = soup_level.find('form',{'method':'POST'}).p.em.string
    print('用户名是：%s,密码是：%s,难易程度：%s'%(user,pwd,result))
if __name__ == '__main__':
    dic = {'admin':'password','gordonb':'abc123','smithy':'password'}
    for m,v in dic.items():
        sp(m,v)