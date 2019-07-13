# 进入文本分类系统界面的入口文件。在该py文件中导入我们设计好的界面文件，直接在此处调用执行
# 几乎所有的文本分类系统的后台逻辑功能都是在此文件中实现的。

import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from main import Ui_mainWindow  # 导入文本分类系统主界面 Ui_mainWindow
from data_test_win import Classfy_test  # 导入文本分类处理函数 Classfy_test进行分类
from ciyun_pic import getciyuntu  # 导入生成词云图函数 getciyuntu生成词云图
from get_newscontent import get_newcontent  # 导入获取特定url文本内容函数
from data_exercise import readFile,saveFile  # 导入读取文件和写入文件的函数
import os


class mainwindow(QtWidgets.QWidget, Ui_mainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        # 将文本分类功能绑定在pushButtoncl按钮的点击事件
        self.pushButtoncl.clicked.connect(self.classfy)
        # 将打开文件的功能绑定在pushButtonop按钮的点击事件上
        self.pushButtonop.clicked.connect(self.openfile)
        # 将生成词云图功能绑定在pushbuttonciyun按钮的点击事件上
        self.pushButtonciyun.clicked.connect(self.ciyuntu)
        # 将通过爬去url文本功能绑定在pushbutton_url按钮的点击事件上
        self.pushButton_url.clicked.connect(self.getnewscontent)
        self.pushButton.clicked.connect(self.getfolder)

    # 文本分类，获取输入文本直接调用Classfy_test函数即可
    def classfy(self):
        str = self.textEdit.toPlainText()
        self.label3.setText(Classfy_test(str))
        pixre = QPixmap('result.png')
        self.picturelabel.setPixmap(pixre)  # 将生成的分类结果柱形图放在控件picturelabel上

    # 打开特定文件，将内容显示在文本框内textEdit
    def openfile(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'open file', '')  # 默认打开的起始路径是当前路径
            with open(filename[0], 'r') as f:
                my_txt = f.read()
                self.textEdit.setPlainText(my_txt)
        except:
            pass


    # 打开特定文件夹，对文件夹内容进行分类
    def getfolder(self):
        try:
            directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 默认起始路径
            print(directory + '/')
            fatherLists = os.listdir(directory + '/')
            print(fatherLists)
            resultPath = 'D:/python/bishe/QTtest/QTtest/result/'
            for eachFile in fatherLists:  # 遍历主目录中各个文件
                eachPathfile = directory + '/' + eachFile
                print(eachPathfile)
                content = readFile(eachPathfile)  # 调用上面函数读取内容
                result_eachDir = Classfy_test(content)
                each_resultPath = resultPath + result_eachDir + "/"  # 分词结果文件存入的目录
                print(each_resultPath)
                if not os.path.exists(each_resultPath):
                    os.makedirs(each_resultPath)
                print(each_resultPath + eachFile)
                saveFile(each_resultPath + eachFile, content)
            self.textEdit.setPlainText('分类完成！！！')
        except:
            pass

    # 生成词云图
    def ciyuntu(self):
        str = self.textEdit.toPlainText()
        getciyuntu(str)
        pixre = QPixmap('ciyuntu.png')
        self.picturelabel.setPixmap(pixre)  # 将生成的词云图放在控件picturelabel上

    def getnewscontent(self):
        url = self.textEdit_url.toPlainText()
        content = get_newcontent(url)
        if content != False:
            self.textEdit.setPlainText(content)
        else:
            QMessageBox.about(self, "提示", "链接输入有误，重新输入！！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mainwindow()
    myshow.show()
    sys.exit(app.exec_())
