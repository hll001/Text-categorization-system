'''
    通过我们输入的文本进行在data_exercise.py中相同处理方法后得到的测试词向量阵空间testSpace
    利用testspace词频向量空间在，最后通过多项式贝叶斯算法，进行测试集和训练集向量空间进行模型化
    计算处理计算得出对我们的测试集预测的分类结果。

    使用matplotlib库将分类结果处理成柱形图，可直观表示分类结果
    使用wordcloud库生成基于输入文本的词云图，方便体现输入文本的特征
'''
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

# 获取训练集
def readBunch(path):
    with open(path, 'rb') as file:
        bunch = pickle.load(file)
    return bunch

def Classfy_test(textcontent):
    # name_list = []
    # label = ['IT', 'Motion', 'Healthy', 'Military', 'Recruit', 'Education', 'Culture', 'Tourism', 'Automobile',
    #     #          'Finance']
    result=textcontent.replace("\r\n", "").strip()
    cutResult=jieba.cut(result)
    bunch=Bunch(contents=[])
    bunch.contents.append("".join(cutResult))
    # 获取停用词表
    stopWordList = getStopWord("D:/python/bishe/Train_Data/stopwords/哈工大停用词表.txt")
    # 构建测试集TF-IDF向量空间
    testSpace = Bunch(tdm=[],vocabulary={})
    # 导入训练集的词袋
    trainbunch = readBunch("D:/python/bishe/Train_Data/tfidfspace.dat")
    # 使用TfidfVectorizer初始化向量空间模型  使用训练集词袋向量
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5,
                                 vocabulary=trainbunch.vocabulary)
    testSpace.tdm = vectorizer.fit_transform(bunch.contents)
    testSpace.vocabulary = trainbunch.vocabulary
    trainSet = readBunch("D:/python/bishe/Train_Data/tfidfspace.dat")
    clf = MultinomialNB(alpha=0.00001).fit(trainSet.tdm, trainSet.label)# alpha:0.001 alpha 越小，迭代次数越多，精度越高
    predicted = clf.predict(testSpace.tdm)
####################################
    # 此部分是生成分类结果柱形图
    label=['IT','Sport','Healthy','Military','Recruit','Education','Culture','Tourism','Car','Finance']
    print(clf.predict_proba(testSpace.tdm)[0])
    # for item in clf.predict_proba(testSpace.tdm)[0]:
    #     name_list.append(item)
    # print(name_list)
    plt.barh(range(len(clf.predict_proba(testSpace.tdm)[0])), clf.predict_proba(testSpace.tdm)[0], tick_label=label)
    plt.savefig("result.png",dpi=80) # 保存分类结果的柱形图
    plt.close()
##################################
    # print(type(str(predicted[0])))
    # print("预测类别：",predicted[0])

    # 返回预测结果，内容是numpy列表
    return str(predicted[0])

# 写个主函数是为了进行测试

# if __name__ == '__main__':
#     textcontent=input("输入测试的内容：")
#     Classfy_test(textcontent)