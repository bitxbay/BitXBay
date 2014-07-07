# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sell.ui'
#
# Created: Mon Jul 07 14:45:15 2014
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

class Ui_Sell(object):
    def setupUi(self, Sell):
        Sell.setObjectName(_fromUtf8("Sell"))
        Sell.resize(860, 571)
        Sell.setMinimumSize(QtCore.QSize(0, 0))
        Sell.setStyleSheet(_fromUtf8("QDoubleSpinBox{\n"
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
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(76, 88, 102, 255), stop:1 rgba(65, 73, 86, 255));\n"
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
        Sell.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.verticalLayout = QtGui.QVBoxLayout(Sell)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainToolBar = QtGui.QToolBar(Sell)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.verticalLayout.addWidget(self.mainToolBar)
        self.centralWidget = QtGui.QWidget(Sell)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.productdetails = QtGui.QTextEdit(self.centralWidget)
        self.productdetails.setGeometry(QtCore.QRect(10, 250, 831, 191))
        self.productdetails.setObjectName(_fromUtf8("productdetails"))
        self.payandpost = QtGui.QPushButton(self.centralWidget)
        self.payandpost.setGeometry(QtCore.QRect(664, 450, 131, 31))
        self.payandpost.setObjectName(_fromUtf8("payandpost"))
        self.labelsc = QtGui.QLabel(self.centralWidget)
        self.labelsc.setGeometry(QtCore.QRect(20, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelsc.setFont(font)
        self.labelsc.setObjectName(_fromUtf8("labelsc"))
        self.lblscore = QtGui.QLabel(self.centralWidget)
        self.lblscore.setGeometry(QtCore.QRect(120, 15, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblscore.setFont(font)
        self.lblscore.setObjectName(_fromUtf8("lblscore"))
        self.listaddresssell = QtGui.QComboBox(self.centralWidget)
        self.listaddresssell.setGeometry(QtCore.QRect(10, 50, 331, 22))
        self.listaddresssell.setObjectName(_fromUtf8("listaddresssell"))
        self.categorytext = QtGui.QTextEdit(self.centralWidget)
        self.categorytext.setGeometry(QtCore.QRect(10, 180, 831, 31))
        self.categorytext.setObjectName(_fromUtf8("categorytext"))
        self.lab3el_3 = QtGui.QLabel(self.centralWidget)
        self.lab3el_3.setGeometry(QtCore.QRect(10, 160, 831, 21))
        self.lab3el_3.setObjectName(_fromUtf8("lab3el_3"))
        self.la3bel_4 = QtGui.QLabel(self.centralWidget)
        self.la3bel_4.setGeometry(QtCore.QRect(10, 220, 831, 21))
        self.la3bel_4.setObjectName(_fromUtf8("la3bel_4"))
        self.labelprice = QtGui.QLabel(self.centralWidget)
        self.labelprice.setGeometry(QtCore.QRect(20, 442, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelprice.setFont(font)
        self.labelprice.setObjectName(_fromUtf8("labelprice"))
        self.sellprice = QtGui.QDoubleSpinBox(self.centralWidget)
        self.sellprice.setGeometry(QtCore.QRect(80, 459, 71, 21))
        self.sellprice.setDecimals(4)
        self.sellprice.setMinimum(0.0001)
        self.sellprice.setMaximum(9999999.0)
        self.sellprice.setSingleStep(0.01)
        self.sellprice.setObjectName(_fromUtf8("sellprice"))
        self.onlyreted = QtGui.QCheckBox(self.centralWidget)
        self.onlyreted.setGeometry(QtCore.QRect(360, 49, 181, 23))
        self.onlyreted.setObjectName(_fromUtf8("onlyreted"))
        self.xcategory = QtGui.QComboBox(self.centralWidget)
        self.xcategory.setGeometry(QtCore.QRect(500, 100, 281, 22))
        self.xcategory.setObjectName(_fromUtf8("xcategory"))
        self.xcategory.addItem(_fromUtf8(""))
        self.xcategory.addItem(_fromUtf8(""))
        self.xcategory.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(570, 70, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.smthwrong = QtGui.QLabel(self.centralWidget)
        self.smthwrong.setGeometry(QtCore.QRect(280, 480, 411, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.smthwrong.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.smthwrong.setFont(font)
        self.smthwrong.setText(_fromUtf8(""))
        self.smthwrong.setWordWrap(True)
        self.smthwrong.setObjectName(_fromUtf8("smthwrong"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 450, 121, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 480, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ratinlbl = QtGui.QLabel(self.centralWidget)
        self.ratinlbl.setGeometry(QtCore.QRect(170, 442, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ratinlbl.setFont(font)
        self.ratinlbl.setObjectName(_fromUtf8("ratinlbl"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(300, 459, 62, 21))
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMinimum(0.0001)
        self.doubleSpinBox.setMaximum(99999999.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.01)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.contactsell = QtGui.QComboBox(self.centralWidget)
        self.contactsell.setGeometry(QtCore.QRect(10, 100, 331, 22))
        self.contactsell.setObjectName(_fromUtf8("contactsell"))
        self.contactsell.addItem(_fromUtf8(""))
        self.label213 = QtGui.QLabel(self.centralWidget)
        self.label213.setGeometry(QtCore.QRect(10, 125, 331, 31))
        self.label213.setObjectName(_fromUtf8("label213"))
        self.newsellcont = QtGui.QPushButton(self.centralWidget)
        self.newsellcont.setGeometry(QtCore.QRect(350, 100, 91, 22))
        self.newsellcont.setObjectName(_fromUtf8("newsellcont"))
        self.label_4231 = QtGui.QLabel(self.centralWidget)
        self.label_4231.setGeometry(QtCore.QRect(10, 75, 421, 21))
        self.label_4231.setObjectName(_fromUtf8("label_4231"))
        self.resend = QtGui.QPushButton(self.centralWidget)
        self.resend.setGeometry(QtCore.QRect(610, 0, 171, 41))
        self.resend.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain))
        self.resend.setObjectName(_fromUtf8("resend"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(570, 123, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.location = QtGui.QComboBox(self.centralWidget)
        self.location.setGeometry(QtCore.QRect(500, 150, 281, 22))
        self.location.setObjectName(_fromUtf8("location"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(30, -5, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.centralWidget)

        self.retranslateUi(Sell)
        QtCore.QMetaObject.connectSlotsByName(Sell)

    def retranslateUi(self, Sell):
        Sell.setWindowTitle(_translate("Sell", "Dialog", None))
        self.payandpost.setText(_translate("Sell", "Pay and post", None))
        self.labelsc.setText(_translate("Sell", "Address score:", None))
        self.lblscore.setText(_translate("Sell", "0", None))
        self.lab3el_3.setText(_translate("Sell", "Category. Everyone can create a category. But it is better to use an existing one.", None))
        self.la3bel_4.setText(_translate("Sell", "Product or service details", None))
        self.labelprice.setText(_translate("Sell", "Price:", None))
        self.onlyreted.setText(_translate("Sell", "Show only rated addresses", None))
        self.xcategory.setItemText(0, _translate("Sell", "Goods", None))
        self.xcategory.setItemText(1, _translate("Sell", "Services", None))
        self.xcategory.setItemText(2, _translate("Sell", "Currencies", None))
        self.label.setText(_translate("Sell", "Type of offer", None))
        self.pushButton.setText(_translate("Sell", "Cancel", None))
        self.label_2.setText(_translate("Sell", "For better position make  more rating payment.", None))
        self.ratinlbl.setText(_translate("Sell", "Rating payment:", None))
        self.contactsell.setItemText(0, _translate("Sell", "Contact address", None))
        self.label213.setText(_translate("Sell", "Contact address", None))
        self.newsellcont.setText(_translate("Sell", "New contact", None))
        self.label_4231.setText(_translate("Sell", "Bitcoin address for sign message and rating payment.", None))
        self.resend.setText(_translate("Sell", "Resend last offers", None))
        self.label_3.setText(_translate("Sell", "Location", None))
        self.label_4.setText(_translate("Sell", "Sign different offers by different addresses. For update, use the same address.", None))

