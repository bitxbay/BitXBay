# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_helpDialog(object):
    def setupUi(self, helpDialog):
        helpDialog.setObjectName(_fromUtf8("helpDialog"))
        helpDialog.resize(601, 246)
        self.label = QtGui.QLabel(helpDialog)
        self.label.setGeometry(QtCore.QRect(9, 9, 556, 162))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.formLayout = QtGui.QFormLayout(helpDialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelHelpURI = QtGui.QLabel(helpDialog)
        self.labelHelpURI.setOpenExternalLinks(True)
        self.labelHelpURI.setObjectName(_fromUtf8("labelHelpURI"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelHelpURI)
        self.label = QtGui.QLabel(helpDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(helpDialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(510, 210, 75, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.retranslateUi(helpDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), helpDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), helpDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(helpDialog)

    def retranslateUi(self, helpDialog):
        helpDialog.setWindowTitle(QtGui.QApplication.translate("helpDialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHelpURI.setText(QtGui.QApplication.translate("helpDialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("helpDialog", "BitXBay user manual:\n"
"For sell something go to decentralization trade tab and click on sell button. Then type details choose price and choose how much you want to pay for rating in trade board. And click \"pay and post\". Do not close program about 20 minutes(for sure dont close more then hour)\n"
"To purchase just click on the tab decentalized trade and select goods, services or currency then click refresh. Find interesting proposal. To clarify the necessary details contact to seller by reference after \"contact\" or directly click the \"buy\" and specify everything you need in the comments (no more than 550 characters)", None, QtGui.QApplication.UnicodeUTF8))

