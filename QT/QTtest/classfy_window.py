# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# 进入文本分类系统界面的入口文件。在该py文件中导入我们设计好的界面文件，直接在此处调用执行（老版本，建议使用该同级目录QTtest下的Function_entry入口）
# 几乎所有的文本分类系统的后台逻辑功能都是在此文件中实现的。



import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from data_test_win import Classfy_test # 导入文本分类处理函数 Classfy_test进行分类
from ciyun_pic import getciyuntu # 导入生成词云图函数 getciyuntu生成词云图

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 471)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(809, 471))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("classfy_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(224, 255, 254);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(809, 471))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vertical_ttitle = QtWidgets.QVBoxLayout()
        self.vertical_ttitle.setObjectName("vertical_ttitle")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setObjectName("label1")
        self.vertical_ttitle.addWidget(self.label1, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.vertical_ttitle, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.picturelabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picturelabel.sizePolicy().hasHeightForWidth())
        self.picturelabel.setSizePolicy(sizePolicy)
        self.picturelabel.setStyleSheet("")
        self.picturelabel.setText("")
        self.picturelabel.setObjectName("picturelabel")
        self.horizontalLayout_2.addWidget(self.picturelabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.horizontalLayout_3.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.horizontalLayout_3.addWidget(self.label3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonop.setObjectName("pushButtonop")
        self.horizontalLayout.addWidget(self.pushButtonop)
        self.pushButtonciyun = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonciyun.setObjectName("pushButtonciyun")
        self.horizontalLayout.addWidget(self.pushButtonciyun)
        self.pushButtoncl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtoncl.setObjectName("pushButtoncl")
        self.horizontalLayout.addWidget(self.pushButtoncl)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    ###############################
        # 动态事件绑定部分

        # 将文本分类功能绑定在pushButtoncl按钮的点击事件
        self.pushButtoncl.clicked.connect(self.classfy)
        # 将打开文件的功能绑定在pushButtonop按钮的点击事件上
        self.pushButtonop.clicked.connect(self.openfile)
        # 将生成词云图功能绑定在pushbuttonciyun按钮的点击事件上
        self.pushButtonciyun.clicked.connect(self.ciyuntu)

    # 文本分类，获取输入文本直接调用Classfy_test函数即可
    def classfy(self):
        str = self.textEdit.toPlainText()
        self.label3.setText(Classfy_test(str))
        pixre = QPixmap('result.png')
        self.picturelabel.setPixmap(pixre)  # 将生成的分类结果柱形图放在控件picturelabel上

    # 打开特定文件，将内容显示在文本框内textEdit
    def openfile(self):
        filename = QFileDialog.getOpenFileName(QtWidgets.QMainWindow(), '打开文件', '')  # 默认打开的起始路径是当前路径
        with open(filename[0], 'r') as f:
            my_txt = f.read()
            self.textEdit.setPlainText(my_txt)

    # 生成词云图
    def ciyuntu(self):
        str = self.textEdit.toPlainText()
        getciyuntu(str)
        pixre = QPixmap('ciyuntu.png')
        self.picturelabel.setPixmap(pixre)  # 将生成的词云图放在控件picturelabel上
    #################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文本分类系统"))
        self.label1.setText(_translate("MainWindow", "文本分类系统"))
        self.label2.setText(_translate("MainWindow", "               推荐分类结果："))
        self.pushButtonop.setText(_translate("MainWindow", "打开文件"))
        self.pushButtonciyun.setText(_translate("MainWindow", "生成词云图"))
        self.pushButtoncl.setText(_translate("MainWindow", "分类"))

# 文本分类桌面端入口
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow=Ui_MainWindow()
    w=QtWidgets.QMainWindow()
    mywindow.setupUi(w)
    w.show()
    sys.exit(app.exec_())