# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
#
# Created: Fri Aug 22 00:34:52 2014
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

class Ui_password(object):
    def setupUi(self, password):
        password.setObjectName(_fromUtf8("password"))
        password.resize(466, 227)
        password.setMinimumSize(QtCore.QSize(0, 0))
        password.setAutoFillBackground(False)
        password.setStyleSheet(_fromUtf8("QDoubleSpinBox{\n"
"color:#fff;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"\n"
"border-radius: 3px;\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"\n"
"}\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(55, 64, 73), stop:0.917522 rgb(73, 82, 97), stop:0.978056 rgb(90, 100, 112));\n"
"}\n"
"\n"
" QMenuBar::item {\n"
"     spacing: 3px; /* spacing between menu bar items */\n"
"     padding: 1px 4px;\n"
"     background: transparent;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"     background: #a8a8a8;\n"
" }\n"
"\n"
" QMenuBar::item:pressed {\n"
"     background: #888888;\n"
" }\n"
"\n"
" QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"     background: #a8a8a8;\n"
" }\n"
"\n"
" QMenuBar::item:pressed {\n"
"     background: #888888;\n"
" }\n"
"\n"
"\n"
"QTabBar::tab {width: 130px; }\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"QWidget {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(166, 178, 192, 185), stop:1 rgba(65, 73, 86, 255));\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:pressed {\n"
"color:#acb3bd;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"/* ----- QSpinBox ---- */\n"
"\n"
"QSpinBox{\n"
"color:#fff;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"\n"
"border-radius: 3px;\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"\n"
"}\n"
"QSpinBox::up-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"QSpinBox::down-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"QSpinBox::up-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QSpinBox::down-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QSpinBox::down-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(55, 64, 73), stop:0.917522 rgb(73, 82, 97), stop:0.978056 rgb(90, 100, 112));\n"
"}\n"
"QTextEdit {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}\n"
"/* ----- QProgressBar ---- */\n"
"\n"
"QProgressBar {\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    text-align: center;\n"
"    border-radius: 3px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* ----- QLineEdit ---- */\n"
"\n"
"QLineEdit {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* ----- QTextBrowser ---- */\n"
"\n"
"QTextBrowser {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* -----  QTextBrowser - QScrollBar:vertical  ---- */\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QTextBrowser - QScrollBar:horizontal  ---- */\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QPlainTextEdit ---- */\n"
"\n"
"QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* ----- QCheckBox ---- */\n"
"\n"
"QCheckBox {\n"
"    spacing: 10px;\n"
"     color:#fff;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    border-radius: 3px;\n"
"width:16px;\n"
"height:16px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/newPrefix/images/check.png);\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    border-radius: 3px;\n"
"    width:16px;\n"
"    height:16px;\n"
"}\n"
"\n"
"/* ----- QTabWidget ---- */\n"
"\n"
"QTabWidget::pane{\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"}\n"
"QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    min-width:100px;\n"
"    min-height:25px;\n"
"    padding-left:5px;\n"
" }\n"
"\n"
" QTabBar::tab:selected,  QTabBar::tab:!selected:hover {\n"
" background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
" color:#fff;\n"
" }\n"
" QTabBar::tab:!selected:hover\n"
" {\n"
" color:#fff;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"\n"
"    border-left-color: rgba(47, 53, 64, 255);\n"
"    border-left-style: solid;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgba(47, 53, 64, 255);\n"
"    border-top-style: solid;\n"
"    border-top-width:1px;\n"
"    border-right-color: rgba(47, 53, 64, 255);\n"
"    border-right-style: solid;\n"
"    border-right-width:1px;\n"
"\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 2px;\n"
"     color:#acb3bd;\n"
"     background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"\n"
" }\n"
"\n"
"/* ----- QComboBox editable and !editable ---- */\n"
"\n"
"\n"
" QComboBox:editable {\n"
"\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"   border-radius: 3px;\n"
"     padding: 1px 18px 1px 13px;\n"
"     min-width: 6em;\n"
"     min-height:28px;\n"
"\n"
"    color:#fff;\n"
"    margin-bottom:3px;\n"
" }\n"
"\n"
" QComboBox:!editable {\n"
"  border-radius: 10px;\n"
"  padding: 1px 18px 1px 3px;\n"
"  min-width: 6em;\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow-combo.png);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down:!editable {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
"\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:1, stop:0 rgb(0, 40, 65), stop:0.319716 rgba(127, 204, 255, 255), stop:0.803987 rgba(0, 0, 0, 255), stop:0.994318 rgba(0, 0, 0, 255));\n"
"\n"
"    border-left-style: solid;\n"
"    border-left-width:2px;\n"
"\n"
"    padding:9px 5px 7px 5px;\n"
"    width:17px;\n"
"}\n"
"\n"
"QComboBox::drop-down:editable {\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
" padding:6px;\n"
" width:16px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down:hover:editable {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
" QComboBox::drop-down:editable:on {\n"
" color:#acb3bd;\n"
" background-color:  rgba(47, 53, 64, 255);\n"
"border:0 solid transparent;\n"
" }\n"
"\n"
"\n"
"QComboBox QListView\n"
"{\n"
"margin:5px;\n"
"background-color:  rgb(47, 53, 64);\n"
"}\n"
"\n"
"\n"
"QComboBox QListView:on::item {\n"
"    border-left: 1px solid transparent;\n"
"    color:#acb3bd;\n"
"padding-left:5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    selection-background-color: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
"    selection-color:#fff;\n"
"}\n"
"\n"
"/* ----- QScrollBar:vertical ---- */\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QScrollBar:horizontal ---- */\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QRadioButton ---- */\n"
"\n"
"QRadioButton\n"
"{\n"
"color:#fff;\n"
"\n"
"}\n"
" QRadioButton::indicator::unchecked {\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"\n"
"    border-radius:8px;\n"
"    width:16px;\n"
"    height:16px;\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
" QRadioButton::indicator::checked {\n"
" background-color:  rgba(47, 53, 64, 255);\n"
" border-radius: 8px;\n"
" width:16px;\n"
" height:16px;\n"
"     image: url(:/newPrefix/images/radio.png);\n"
" }\n"
"\n"
"\n"
" QRadioButton::indicator:checked:pressed {\n"
"    image: url(:/newPrefix/images/radio.png);\n"
" }\n"
"\n"
"/* ----- QTableView ---- */\n"
"\n"
"QTableView\n"
"{\n"
"color:#fff;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-radius: 3px;\n"
"gridline-color:rgb(90, 100, 112);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
"}\n"
"QHeaderView::section, QTableView QTableCornerButton::section {\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"padding:5px;\n"
" }\n"
"\n"
" QHeaderView::section:checked, QTableView QTableCornerButton::section:checked\n"
" {\n"
" background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
" border-color: rgba(47, 53, 64, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
"  border-radius: 3px;\n"
" }\n"
"\n"
"/* ----- QScrollBar:vertical ---- */\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QScrollBar:horizontal ---- */\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
""))
        password.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(password)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.centralWidget = QtGui.QWidget(password)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label231 = QtGui.QLabel(self.centralWidget)
        self.label231.setGeometry(QtCore.QRect(0, 160, 571, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label231.sizePolicy().hasHeightForWidth())
        self.label231.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label231.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label231.setFont(font)
        self.label231.setStyleSheet(_fromUtf8("QLabel{\n"
"background-color:  rgba(0, 0, 0, 0);\n"
"}"))
        self.label231.setWordWrap(True)
        self.label231.setObjectName(_fromUtf8("label231"))
        self.ok = QtGui.QPushButton(self.centralWidget)
        self.ok.setGeometry(QtCore.QRect(380, 171, 61, 26))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 170, 291, 31))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setPlaceholderText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 22, 441, 141))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"background-color:  rgba(0, 0, 0, 0);\n"
"background-image: url(:/newPrefix/images/logo.png);\n"
"background-position: top center; \n"
"background-repeat: norepeat;\n"
"}"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.centralWidget)

        self.retranslateUi(password)
        QtCore.QMetaObject.connectSlotsByName(password)

    def retranslateUi(self, password):
        password.setWindowTitle(_translate("password", "Dialog", None))
        self.label231.setText(_translate("password", "Password:", None))
        self.ok.setText(_translate("password", "OK", None))
        self.lineEdit.setToolTip(_translate("password", "Electrum password. Only latin.", None))

