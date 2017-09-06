# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\G\Desktop\Python\yun\yun.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(501, 434)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 280, 341, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Bt_yun_x = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_yun_x.setEnabled(True)
        self.Bt_yun_x.setObjectName("Bt_yun_x")
        self.gridLayout.addWidget(self.Bt_yun_x, 0, 0, 1, 1)
        self.Bt_bo_x = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_bo_x.setEnabled(False)
        self.Bt_bo_x.setObjectName("Bt_bo_x")
        self.gridLayout.addWidget(self.Bt_bo_x, 0, 1, 1, 1)
        self.Bt_xxdf = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_xxdf.setEnabled(False)
        self.Bt_xxdf.setObjectName("Bt_xxdf")
        self.gridLayout.addWidget(self.Bt_xxdf, 0, 3, 1, 1)
        self.Bt_dang_x = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_dang_x.setEnabled(False)
        self.Bt_dang_x.setObjectName("Bt_dang_x")
        self.gridLayout.addWidget(self.Bt_dang_x, 0, 2, 1, 1)
        self.Bt_yun_z = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_yun_z.setEnabled(False)
        self.Bt_yun_z.setObjectName("Bt_yun_z")
        self.gridLayout.addWidget(self.Bt_yun_z, 1, 0, 1, 1)
        self.Bt_bo_z = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_bo_z.setEnabled(False)
        self.Bt_bo_z.setObjectName("Bt_bo_z")
        self.gridLayout.addWidget(self.Bt_bo_z, 1, 1, 1, 1)
        self.Bt_dang_z = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_dang_z.setEnabled(False)
        self.Bt_dang_z.setObjectName("Bt_dang_z")
        self.gridLayout.addWidget(self.Bt_dang_z, 1, 2, 1, 1)
        self.Bt_xlfd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Bt_xlfd.setEnabled(False)
        self.Bt_xlfd.setObjectName("Bt_xlfd")
        self.gridLayout.addWidget(self.Bt_xlfd, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 391, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 0, 161, 411))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setMaximumSize(QtCore.QSize(199, 126))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setDocumentTitle("")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_3.setMinimumSize(QtCore.QSize(0, 175))
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.textEdit_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 132))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.image_u = QtWidgets.QLabel(self.centralWidget)
        self.image_u.setGeometry(QtCore.QRect(0, 80, 170, 170))
        self.image_u.setAutoFillBackground(True)
        self.image_u.setFrameShape(QtWidgets.QFrame.Box)
        self.image_u.setObjectName("image_u")
        self.image_opp = QtWidgets.QLabel(self.centralWidget)
        self.image_opp.setGeometry(QtCore.QRect(170, 80, 170, 170))
        self.image_opp.setAutoFillBackground(True)
        self.image_opp.setFrameShape(QtWidgets.QFrame.Box)
        self.image_opp.setObjectName("image_opp")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 501, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionguanyu = QtWidgets.QAction(MainWindow)
        self.actionguanyu.setObjectName("actionguanyu")
        self.menu.addAction(self.actionguanyu)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "运"))
        self.Bt_yun_x.setText(_translate("MainWindow", "运"))
        self.Bt_bo_x.setText(_translate("MainWindow", "小波"))
        self.Bt_xxdf.setText(_translate("MainWindow", "吸星大法"))
        self.Bt_dang_x.setText(_translate("MainWindow", "小挡"))
        self.Bt_yun_z.setText(_translate("MainWindow", "中运"))
        self.Bt_bo_z.setText(_translate("MainWindow", "中波"))
        self.Bt_dang_z.setText(_translate("MainWindow", "中挡"))
        self.Bt_xlfd.setText(_translate("MainWindow", "小李飞刀"))
        self.label_3.setText(_translate("MainWindow", "对手"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">对手</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">你</p></body></html>"))
        self.image_u.setText(_translate("MainWindow", "你"))
        self.image_opp.setText(_translate("MainWindow", "对手"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.actionguanyu.setText(_translate("MainWindow", "guanyu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

