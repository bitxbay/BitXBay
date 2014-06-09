# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Bitco\bitmessageqt\sellalert.ui'
#
# Created: Sat Jun 07 19:06:13 2014
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

class Ui_SellAlert(object):
    def setupUi(self, SellAlert):
        SellAlert.setObjectName(_fromUtf8("SellAlert"))
        SellAlert.resize(822, 484)
        SellAlert.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.central2Widget = QtGui.QWidget(SellAlert)
        self.central2Widget.setGeometry(QtCore.QRect(80, 30, 781, 381))
        self.central2Widget.setLocale(QtCore.QLocale(QtCore.QLocale.Cherokee, QtCore.QLocale.UnitedStates))
        self.central2Widget.setObjectName(_fromUtf8("central2Widget"))
        self.smthwrong = QtGui.QLabel(self.central2Widget)
        self.smthwrong.setGeometry(QtCore.QRect(270, 395, 331, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.smthwrong.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.smthwrong.setFont(font)
        self.smthwrong.setText(_fromUtf8(""))
        self.smthwrong.setObjectName(_fromUtf8("smthwrong"))
        self.label = QtGui.QLabel(self.central2Widget)
        self.label.setGeometry(QtCore.QRect(60, 90, 711, 231))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.menuBar = QtGui.QMenuBar(SellAlert)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 853, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.mainToolBar = QtGui.QToolBar(SellAlert)
        self.mainToolBar.setGeometry(QtCore.QRect(0, 0, 4, 12))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.statusBar = QtGui.QStatusBar(SellAlert)
        self.statusBar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))

        self.retranslateUi(SellAlert)
        QtCore.QMetaObject.connectSlotsByName(SellAlert)

    def retranslateUi(self, SellAlert):
        SellAlert.setWindowTitle(_translate("SellAlert", "Sell", None))
        self.label.setText(_translate("SellAlert", "Now your message in the process of sending to the network, \n"
"please wait until it is sent, if necessary, click resend.\n"
" The message is usually sent for 20-40 minutes.", None))

