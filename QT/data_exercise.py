'''
    此部分是进行对爬取的新闻数据进行训练的过程
    通过对文本分类语料中新闻内容训练得的到分词segResult
    再通过分词的segResult中每一个文件的标题，内容，路径名称进行bunch二进制化处理，得到train_set.dat文件
    读取train_set.dat文件中的二进制文件进行TF-IDF向量化的得到词频矩阵空间，并且以二进制文件tfidfspace.dat文件保存
    最终得到词频矩阵空间
'''
import jieba
import os
import pickle  # 持久化
from numpy import *
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer  # TF_IDF向量生成类
from sklearn.datasets.base import Bunch


def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # 文档中编码有些问题，所有用errors过滤错误
        # 返回读取文件的内容
        content = file.read()
        return content


# result是需要写入文件的内容
def saveFile(path, result):
    with open(path, 'w', errors='ignore') as file:
        file.write(result)


def segText(inputPath, resultPath):
    fatherLists = os.listdir(inputPath)  # 主目录
    for eachDir in fatherLists:  # 遍历主目录中各个文件夹
        eachPath = inputPath + eachDir + "/"  # 保存主目录中每个文件夹目录，便于遍历二级文件
        each_resultPath = resultPath + eachDir + "/"  # 分词结果文件存入的目录
        if not os.path.exists(each_resultPath):
            os.makedirs(each_resultPath)
        childLists = os.listdir(eachPath)  # 获取每个文件夹中的各个文件
        for eachFile in childLists:  # 遍历每个文件夹中的子文件
            eachPathFile = eachPath + eachFile  # 获得每个文件路径
            print(eachFile)
            content = readFile(eachPathFile)  # 调用上面函数读取内容
            # content = str(content)
            result = (str(content)).replace("\r\n", "").strip()  # 删除多余空行与空格
            # result = content.replace("\r\n","").strip()
            cutResult = jieba.cut(result)  # 默认方式分词，分词结果用空格隔开
            saveFile(each_resultPath + eachFile, " ".join(cutResult))  # 调用上面函数保存文件


def bunchSave(inputFile, outputFile):
    catelist = os.listdir(inputFile)
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)  # 将类别保存到Bunch对象中
    for eachDir in catelist:
        eachPath = inputFile + eachDir + "/"
        fileList = os.listdir(eachPath)
        for eachFile in fileList:  # 二级目录中的每个子文件
            fullName = eachPath + eachFile  # 二级目录子文件全路径
            bunch.label.append(eachDir)  # 当前分类标签
            bunch.filenames.append(fullName)  # 保存当前文件的路径
            bunch.contents.append(readFile(fullName).strip())  # 保存文件词向量
    with open(outputFile, 'wb') as file_obj:  # 持久化必须用二进制访问模式打开
        pickle.dump(bunch, file_obj)


def readBunch(path):
    with open(path, 'rb') as file:
        bunch = pickle.load(file)
    return bunch


def writeBunch(path, bunchFile):
    with open(path, 'wb') as file:
        pickle.dump(bunchFile, file)


# 获取停用词列表
def getStopWord(inputFile):
    stopWordList = readFile(inputFile).splitlines()
    return stopWordList


# 求得TF-IDF向量
def getTFIDFMat(inputPath, stopWordList, outputPath):
    bunch = readBunch(inputPath)
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                       vocabulary={})
    # 初始化向量空间
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
    # 文本转化为词频矩阵，单独保存字典文件
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
    tfidfspace.vocabulary = vectorizer.vocabulary_
    writeBunch(outputPath, tfidfspace)


# 建立测试空间，炼化测试数据
# def getTestSpace(testSetPath, trainSpacePath, stopWordList, testSpacePath):
#     bunch = readBunch(testSetPath)
#     # 构建测试集TF-IDF向量空间
#     testSpace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
#                       vocabulary={})
#     # 导入训练集的词袋
#     trainbunch = readBunch(trainSpacePath)
#     # 使用TfidfVectorizer初始化向量空间模型  使用训练集词袋向量
#     vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5,
#                                  vocabulary=trainbunch.vocabulary)
#     transformer = TfidfTransformer()
#     testSpace.tdm = vectorizer.fit_transform(bunch.contents)
#     testSpace.vocabulary = trainbunch.vocabulary
#     # 持久化
#     writeBunch(testSpacePath, testSpace)


if __name__ == '__main__':
    # 获取停用词
    stopWordList = getStopWord("Train_Data/stopwords/哈工大停用词表.txt")
    # 对数据进行训练得到训练集
    segText("Train_Data/文本分类语料库/", "Train_Data/segResult/")  #分词，第一个是分词输入，第二个参数是结果保存的路径,segResult是经过分词之后的结果
    bunchSave("Train_Data/segResult/", "Train_Data/train_set.dat")  # 输入分词，输出分词向量
    getTFIDFMat("Train_Data/train_set.dat", stopWordList, "Train_Data/tfidfspace.dat")  # 输入词向量，输出特征空间
