import jieba
import pickle  # 持久化
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF向量生成类
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # 多项式贝叶斯算法
import matplotlib.pyplot as plt


def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # 文档中编码有些问题，所有用errors过滤错误
        # 返回读取文件的内容
        content = file.read()
        return content


# 获取停用词列表
def getStopWord(inputFile):
    stopWordList = readFile(inputFile).splitlines()
    return stopWordList


# 获取训练集的
def readBunch(path):
    with open(path, 'rb') as file:
        bunch = pickle.load(file)
    return bunch


def Classfy_test(textcontent):
    # name_list = []
    # label = ['IT', 'Motion', 'Healthy', 'Military', 'Recruit', 'Education', 'Culture', 'Tourism', 'Automobile',
    #     #          'Finance']
    result = textcontent.replace("\r\n", "").strip()
    # print(result)
    cutResult = jieba.cut(result)
    bunch = Bunch(contents=[])
    # print("".join(cutResult))
    bunch.contents.append("".join(cutResult))
    # 获取停用词表
    stopWordList = getStopWord("D:/python/bishe/Train_Data/stopwords/哈工大停用词表.txt")
    # 构建测试集TF-IDF向量空间
    testSpace = Bunch(tdm=[], vocabulary={})
    # 导入训练集的词袋
    trainbunch = readBunch("D:/python/bishe/Train_Data/tfidfspace.dat")
    # 使用TfidfVectorizer初始化向量空间模型  使用训练集词袋向量
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5,
                                 vocabulary=trainbunch.vocabulary)
    testSpace.tdm = vectorizer.fit_transform(bunch.contents)
    testSpace.vocabulary = trainbunch.vocabulary
    trainSet = readBunch("D:/python/bishe/Train_Data/tfidfspace.dat")
    clf = MultinomialNB(alpha=0.001).fit(trainSet.tdm, trainSet.label)  # alpha:0.001 alpha 越小，迭代次数越多，精度越高
    predicted = clf.predict(testSpace.tdm)
    # predicted[0]是预测结果，clf.predict_proba(testSpace.tdm)[0]内容是numpy列表
    #返回字典结构，方便后期json化
    return {'jieguo': str(predicted[0]), 'shuju': [round(x, 4) for x in clf.predict_proba(testSpace.tdm)[0]]}
