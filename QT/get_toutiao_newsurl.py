import requests
import time
import math
import hashlib
import random
from bs4 import BeautifulSoup
import pymysql.cursors
import jieba
from get_newscontent import get_toutiao_newscontent


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}
page = ["", "2", "3", "4", "5"]

def get_ip_list():
    print("正在获取代理列表...")
    # N=1
    ip_list = []
    ipnumber = 1
    for num in page:
        # 通过此方式多获取点ip建立ip池
        url = 'http://www.xicidaili.com/nn/' + num
        html = requests.get(url=url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        ips = soup.find(id='ip_list').find_all('tr')
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            print(tds)
            # 进行代理ip的测试，返回状态码为200的表示该ip能正常使用加入ip列表
            s = requests.get('https://www.baidu.com', 'http:\\' + tds[1].text + ':' + tds[2].text)
            print('第{}个ip：{} 状态{}'.format(ipnumber, 'http:\\' + tds[1].text + ':' + tds[2].text, s.status_code))
            if ipnumber > 99:
                break
            if s.status_code == 200:
                ip_list.append('http:\\' + tds[1].text + ':' + tds[2].text)
                ipnumber += 1
        if ipnumber > 99:
            break
    print("100条代理列表抓取成功.内容如下：")
    print(ip_list)
    return ip_list

# 设置随机代理，可直接在主函数中填写，不写入主函数，只是给我自己参考
def get_random_ip(ip_list):
    print("正在设置随机代理...")
    proxy_ip = random.choice(ip_list)
    proxies = {'http': proxy_ip}
    print("代理设置成功.")
    return proxies



def getASCP():
    t = int(math.floor(time.time()))
    e = hex(t).upper()[2:]
    m = hashlib.md5()
    m.update(str(t).encode(encoding='utf-8'))
    i = m.hexdigest().upper()

    if len(e) != 8:
        AS = '479BB4B7254C150'
        CP = '7E0AC8874BB0985'
        return AS,CP

    n = i[0:5]
    a = i[-5:]
    s = ''
    r = ''
    for o in range(5):
        s += n[o] + e[o]
        r += e[o + 3] + a[o]

    AS = 'A1' + s + e[-3:]
    CP = e[0:3] + r + 'E1'
    print("AS:"+AS,"CP:"+CP)
    return AS,CP



def get_url(label,max_behot_time,AS,CP):
    url = 'https://www.toutiao.com/api/pc/feed/?category={0}&utm_source=toutiao&widen=1' \
           '&max_behot_time={1}' \
           '&max_behot_time_tmp={1}' \
           '&tadrequire=true' \
           '&as={3}' \
           '&cp={3}'.format(label,max_behot_time,AS,CP)
    print(url)
    return url

def get_item(url,proxies):
    cookies = {"tt_webid":"6642907607587702279"}
    wbdata = requests.get(url,cookies = cookies,headers=headers,proxies=proxies).json()
    print(wbdata)
    data = wbdata['data']
    for news in data:
        title = news['title']
        tag_url = news['tag_url']
        news_url = news['source_url']
        news_url = "https://www.toutiao.com"+news_url

        print(title,tag_url,news_url)

    next_data = wbdata['next']
    next_max_behot_time = next_data['max_behot_time']
    print("next_max_behot_time:{0}".format(next_max_behot_time))
    return next_max_behot_time

if __name__ == '__main__':
    dir_labels={
                'news_tech':'科技',
                'news_sports': '体育',
                'news_regimen':'健康',
                'news_military': '军事',
                'news_society': '社会',
                'news_baby': '育儿',
                'news_history': '历史',
                'news_travel': '旅游',
                'news_car': '汽车',
                'news_finance': '财经',
                }
    # 测试5次
    refresh = 5
    # 将获取的代理ip列表放入ip_list中
    ip_list=get_ip_list()
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 db='news',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    for label in dir_labels:
        print(label)
        for x in range(0,refresh+1):
            print("第{0}次：".format(x))
            if x == 0:
                max_behot_time = 0
            else:
                max_behot_time = next_max_behot_time
                print (max_behot_time)
            # 这里将随机设置ip代理
            proxy_ip = random.choice(ip_list)
            proxies = {'proxy': proxy_ip}
            AS,CP = getASCP()
            url = get_url(label,max_behot_time,AS,CP)
            content=get_toutiao_newscontent(url)
            result = (str(content)).replace("\r\n", "").strip()  # 删除多余空行与空格
            cutResult = jieba.cut(result)  # 默认方式分词，分词结果用空格隔开
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO "+label+"(Url,Content,Jie_content)VALUES(%s,%s,%s)"
                print(sql)
                cursor.execute(sql, (url,content, " ".join(cutResult)))
                connection.commit()
            next_max_behot_time = get_item(url,proxies)
            time.sleep(2)
    connection.close()