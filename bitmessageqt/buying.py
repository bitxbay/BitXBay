# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\last\PyBitsrc\bitmessageqt\buying.ui'
#
# Created: Thu May 08 13:26:33 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Buying(object):
    def setupUi(self, Buying):
        Buying.setObjectName(_fromUtf8("Buying"))
        Buying.resize(751, 452)
        self.centralWidget = QtGui.QWidget(Buying)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(34, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(140, 70, 131, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(140, 120, 91, 31))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(30, 152, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 190, 691, 161))
        self.plainTextEdit.setOverwriteMode(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(310, 64, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(430, 60, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 362, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 362, 111, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        Buying.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Buying)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        Buying.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Buying)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Buying.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Buying)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Buying.setStatusBar(self.statusBar)

        self.retranslateUi(Buying)
        QtCore.QMetaObject.connectSlotsByName(Buying)

    def retranslateUi(self, Buying):
        Buying.setWindowTitle(_translate("Buying", "Buying", None))
        self.label.setText(_translate("Buying", "Deal confirmation", None))
        self.label_2.setText(_translate("Buying", "Deal amount:", None))
        self.label_3.setText(_translate("Buying", "Merchant text:", None))
        self.label_4.setText(_translate("Buying", "0.0", None))
        self.label_6.setText(_translate("Buying", "Your comment for merchant. Type here the shipping address or other important information.", None))
        self.label_7.setText(_translate("Buying", "Merchant rating:", None))
        self.label_8.setText(_translate("Buying", "0.0", None))
        self.pushButton.setText(_translate("Buying", "Buy", None))
        self.pushButton_2.setText(_translate("Buying", "Cancel", None))

