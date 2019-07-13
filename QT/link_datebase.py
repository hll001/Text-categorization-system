import pymysql.cursors
import os
import jieba
import random

def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # 文档中编码有些问题，所有用errors过滤错误
        # 返回读取文件的内容
        content = file.read()
        return content


def insertnews(inputPath):
    # labels = ['news_tech', 'news_sports', 'news_regimen', 'news_military', 'news_society', 'news_baby',
    #               'news_history', 'news_travel', 'news_car', 'news_finance']
    # num=0
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 db='news',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    fatherLists=os.listdir(inputPath)
    # print(fatherLists)
    for eachDir in fatherLists:  # 遍历主目录中各个文件夹
        eachPath = inputPath + eachDir + "/"  # 保存主目录中每个文件夹目录，便于遍历二级文件
        childLists = os.listdir(eachPath)  # 获取每个文件夹中的各个文件
        for eachFile in childLists:  # 遍历每个文件夹中的子文件
            eachPathFile = eachPath + eachFile  # 获得每个文件路径
            print(eachPath+'/'+eachFile)
            content = readFile(eachPathFile)  # 调用上面函数读取内容
            result = (str(content)).replace("\r\n", "").strip()  # 删除多余空行与空格
            cutResult = jieba.cut(result)  # 默认方式分词，分词结果用空格隔开
            # print(type(" ".join(cutResult)))
            url='https://www.toutiao.com/a6698'+str(random.randint(400000000000000,999999999999999))+'/'
            # print(url)
            # print(content)
            # print('**********************************')
            # print(" ".join(cutResult))
            with connection.cursor() as cursor:
                sql = "INSERT IGNORE INTO "+eachDir+"(Url,Content,Jie_content)VALUES(%s,%s,%s)"
                print(sql)
                cursor.execute(sql, (url,content, " ".join(cutResult)))
                connection.commit()
        # num=num+1
    connection.close()
    # with connection.cursor() as cursor:
    #     sql = "INSERT IGNORE INTO IT(Url,Content,Jie_content)VALUES(%s,%s,%s)"
    #     print(sql)
    #     cursor.execute(sql, ('1','2', '3'))
    #     connection.commit()
    # connection.close()
    # fatherLists = os.listdir(inputPath)
    # for eachDir in fatherLists:  # 遍历主目录中各个文件夹
    #     print(eachDir)
    # labels = ['news_tech','news_sports','news_regimen','news_military','news_society','news_baby','news_history','news_travel','news_car','news_finance']

if __name__ == '__main__':
    insertnews("Train_Data/文本分类语料库/")