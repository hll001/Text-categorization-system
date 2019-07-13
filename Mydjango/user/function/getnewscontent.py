# 目前只是支持腾讯新闻，网易新闻，今日头条三个新闻网站平台，搜狐部分可以
from bs4 import BeautifulSoup
import lxml
import re
import html
import requests


def get_other_newcontent(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }
    html = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('h1').text
    new_content = title + '\n'
    for item in soup.find_all('p'):
        new_content = new_content + item.text + '\n'
    print("############################")
    # print(new_content)
    return new_content


def get_toutiao_newscontent(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }
    data = requests.get(url=url, headers=headers).text
    content = re.findall(r"content:(.+)", data)[0]
    html_content = html.unescape(content)
    soup = BeautifulSoup(html_content, 'lxml')
    new_content = ''
    for item in soup.find_all('p'):
        new_content = new_content + item.text + '\n'
    print("****************************")
    # print(new_content)
    return new_content


def get_newcontent(url):
    try:
        return {'news':get_other_newcontent(url)}
    except:
        try:
            return {'news':get_toutiao_newscontent(url)}
        except:
            print("出错了")
            return {'news':'False'}


