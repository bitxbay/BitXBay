# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Bitco\bitmessageqt\litegrab.ui'
#
# Created: Tue Jul 01 11:58:49 2014
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

class Ui_litegrab(object):
    def setupUi(self, litegrab):
        litegrab.setObjectName(_fromUtf8("litegrab"))
        litegrab.resize(500, 300)
        litegrab.setMinimumSize(QtCore.QSize(0, 0))
        litegrab.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(litegrab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.centralWidget = QtGui.QWidget(litegrab)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.liteonoff = QtGui.QDialogButtonBox(self.centralWidget)
        self.liteonoff.setGeometry(QtCore.QRect(140, 230, 161, 41))
        self.liteonoff.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.liteonoff.setObjectName(_fromUtf8("liteonoff"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 431, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.centralWidget)

        self.retranslateUi(litegrab)
        QtCore.QMetaObject.connectSlotsByName(litegrab)

    def retranslateUi(self, litegrab):
        litegrab.setWindowTitle(_translate("litegrab", "Dialog", None))
        self.label.setText(_translate("litegrab", "You run the program the first time, and the blockchain is not downloaded yet. You can activate the light mode and see all the offers without waiting to download whole blockchain. But this will require queries to the blockchain.info . If you want to activate the light mode, click OK.", None))

