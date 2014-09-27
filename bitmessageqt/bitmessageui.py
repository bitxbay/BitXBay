# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bitmessageui.ui'
#
# Created: Sun Sep 14 21:10:29 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(885, 594)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/can-icon-24px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QTabBar::tab:!selected\n"
" {\n"
"border-color: rgba(47, 53, 64, 255);\n"
" border-style: solid;\n"
" border-top-width:1px;\n"
" border-left-width:2px;\n"
" border-right-width:2px;\n"
" }\n"
"\n"
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
"    padding:0;\n"
"    margin:0;\n"
"\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"padding:0;\n"
"margin-top:-1px;\n"
"image:url(:/newPrefix/images/chunk.png);\n"
"\n"
"}\n"
"QToolBar{\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"}\n"
"QDoubleSpinBox{\n"
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
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(106, 118, 132, 255), stop:1 rgba(65, 73, 86, 5));\n"
"    }\n"
"\n"
"/* ----- QPushButton ---- */\n"
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
"\n"
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
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setStyleSheet(_fromUtf8(""))
        self.tabWidget_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget_4 = QtGui.QTabWidget(self.tab)
        self.tabWidget_4.setEnabled(True)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 891, 511))
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.Main = QtGui.QWidget()
        self.Main.setObjectName(_fromUtf8("Main"))
        self.frame = QtGui.QFrame(self.Main)
        self.frame.setGeometry(QtCore.QRect(0, 0, 881, 481))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_49 = QtGui.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(625, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 98, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 56, 64, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.sync = QtGui.QProgressBar(self.frame)
        self.sync.setGeometry(QtCore.QRect(236, 63, 231, 21))
        self.sync.setProperty("value", 0)
        self.sync.setObjectName(_fromUtf8("sync"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 290, 881, 221))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.bitcoinaddresses = QtGui.QTableWidget(self.frame_2)
        self.bitcoinaddresses.setGeometry(QtCore.QRect(9, 9, 861, 211))
        self.bitcoinaddresses.setAutoFillBackground(False)
        self.bitcoinaddresses.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.EditKeyPressed)
        self.bitcoinaddresses.setAlternatingRowColors(False)
        self.bitcoinaddresses.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.bitcoinaddresses.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.bitcoinaddresses.setObjectName(_fromUtf8("bitcoinaddresses"))
        self.bitcoinaddresses.setColumnCount(3)
        self.bitcoinaddresses.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.bitcoinaddresses.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.bitcoinaddresses.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.bitcoinaddresses.setHorizontalHeaderItem(2, item)
        self.bitcoinaddresses.horizontalHeader().setCascadingSectionResizes(True)
        self.bitcoinaddresses.horizontalHeader().setDefaultSectionSize(360)
        self.bitcoinaddresses.horizontalHeader().setHighlightSections(False)
        self.bitcoinaddresses.horizontalHeader().setMinimumSectionSize(50)
        self.bitcoinaddresses.horizontalHeader().setSortIndicatorShown(False)
        self.bitcoinaddresses.horizontalHeader().setStretchLastSection(True)
        self.bitcoinaddresses.verticalHeader().setVisible(False)
        self.tableWidget = QtGui.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(490, 40, 391, 251))
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(124)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(33)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget.verticalHeader().setMinimumSectionSize(19)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.label_ucbalance = QtGui.QLabel(self.frame)
        self.label_ucbalance.setGeometry(QtCore.QRect(130, 90, 46, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Heiti Std R"))
        font.setPointSize(10)
        self.label_ucbalance.setFont(font)
        self.label_ucbalance.setObjectName(_fromUtf8("label_ucbalance"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 151, 23))
        self.pushButton.setStyleSheet(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.sync_label = QtGui.QLabel(self.frame)
        self.sync_label.setGeometry(QtCore.QRect(170, 30, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 0, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 0, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 1, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.sync_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sync_label.setFont(font)
        self.sync_label.setAutoFillBackground(False)
        self.sync_label.setObjectName(_fromUtf8("sync_label"))
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(20, 245, 241, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(195, 3, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 6, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 4, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 3, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 6, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 4, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 4, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_11.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setAcceptDrops(False)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_balance = QtGui.QLabel(self.frame)
        self.label_balance.setGeometry(QtCore.QRect(130, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Heiti Std R"))
        font.setPointSize(10)
        self.label_balance.setFont(font)
        self.label_balance.setObjectName(_fromUtf8("label_balance"))
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 150, 481, 101))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.lineEdit_10 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 10, 381, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(90, 40, 381, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_48 = QtGui.QLabel(self.frame_3)
        self.label_48.setGeometry(QtCore.QRect(20, 9, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.label_50 = QtGui.QLabel(self.frame_3)
        self.label_50.setGeometry(QtCore.QRect(30, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_51 = QtGui.QLabel(self.frame_3)
        self.label_51.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.overviewamount = QtGui.QDoubleSpinBox(self.frame_3)
        self.overviewamount.setEnabled(True)
        self.overviewamount.setGeometry(QtCore.QRect(90, 70, 141, 22))
        self.overviewamount.setStyleSheet(_fromUtf8("QDoubleSpinBox{\n"
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
"   image: url(C:/QtQss/icons/up-arrow.png);\n"
"}\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/down-arrow.png);\n"
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
"}"))
        self.overviewamount.setDecimals(10)
        self.overviewamount.setMaximum(21000000.0)
        self.overviewamount.setSingleStep(0.01)
        self.overviewamount.setProperty("value", 0.0)
        self.overviewamount.setObjectName(_fromUtf8("overviewamount"))
        self.sendbtc = QtGui.QPushButton(self.frame_3)
        self.sendbtc.setGeometry(QtCore.QRect(335, 70, 141, 22))
        self.sendbtc.setStyleSheet(_fromUtf8(""))
        self.sendbtc.setObjectName(_fromUtf8("sendbtc"))
        self.label_52 = QtGui.QLabel(self.frame)
        self.label_52.setGeometry(QtCore.QRect(260, 260, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_44 = QtGui.QLabel(self.frame)
        self.label_44.setGeometry(QtCore.QRect(110, 119, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.tabWidget_4.addTab(self.Main, _fromUtf8(""))
        self.expert = QtGui.QWidget()
        self.expert.setEnabled(False)
        self.expert.setObjectName(_fromUtf8("expert"))
        self.label_10 = QtGui.QLabel(self.expert)
        self.label_10.setGeometry(QtCore.QRect(5, 3, 871, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.importprivkey = QtGui.QPushButton(self.expert)
        self.importprivkey.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.importprivkey.setObjectName(_fromUtf8("importprivkey"))
        self.privkey = QtGui.QLineEdit(self.expert)
        self.privkey.setGeometry(QtCore.QRect(170, 96, 301, 23))
        self.privkey.setObjectName(_fromUtf8("privkey"))
        self.label_13 = QtGui.QLabel(self.expert)
        self.label_13.setGeometry(QtCore.QRect(490, 93, 371, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_13.setPalette(palette)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.dumpkey = QtGui.QPushButton(self.expert)
        self.dumpkey.setGeometry(QtCore.QRect(10, 150, 141, 31))
        self.dumpkey.setObjectName(_fromUtf8("dumpkey"))
        self.dumpaddress = QtGui.QLineEdit(self.expert)
        self.dumpaddress.setGeometry(QtCore.QRect(170, 156, 301, 23))
        self.dumpaddress.setObjectName(_fromUtf8("dumpaddress"))
        self.privdump = QtGui.QLabel(self.expert)
        self.privdump.setGeometry(QtCore.QRect(490, 153, 321, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.privdump.setPalette(palette)
        self.privdump.setObjectName(_fromUtf8("privdump"))
        self.deltx = QtGui.QPushButton(self.expert)
        self.deltx.setGeometry(QtCore.QRect(10, 222, 141, 31))
        self.deltx.setObjectName(_fromUtf8("deltx"))
        self.line = QtGui.QFrame(self.expert)
        self.line.setGeometry(QtCore.QRect(0, 195, 881, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tx = QtGui.QLineEdit(self.expert)
        self.tx.setGeometry(QtCore.QRect(170, 226, 301, 23))
        self.tx.setObjectName(_fromUtf8("tx"))
        self.label_14 = QtGui.QLabel(self.expert)
        self.label_14.setGeometry(QtCore.QRect(490, 226, 371, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_14.setPalette(palette)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.deltx_2 = QtGui.QPushButton(self.expert)
        self.deltx_2.setGeometry(QtCore.QRect(10, 280, 141, 31))
        self.deltx_2.setObjectName(_fromUtf8("deltx_2"))
        self.tx_2 = QtGui.QLineEdit(self.expert)
        self.tx_2.setGeometry(QtCore.QRect(170, 286, 301, 23))
        self.tx_2.setObjectName(_fromUtf8("tx_2"))
        self.label_15 = QtGui.QLabel(self.expert)
        self.label_15.setGeometry(QtCore.QRect(490, 283, 371, 39))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_15.setPalette(palette)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.line_2 = QtGui.QFrame(self.expert)
        self.line_2.setGeometry(QtCore.QRect(0, 330, 881, 21))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.savebtc = QtGui.QPushButton(self.expert)
        self.savebtc.setGeometry(QtCore.QRect(10, 410, 141, 31))
        self.savebtc.setObjectName(_fromUtf8("savebtc"))
        self.backupaddress = QtGui.QLineEdit(self.expert)
        self.backupaddress.setGeometry(QtCore.QRect(290, 415, 301, 23))
        self.backupaddress.setObjectName(_fromUtf8("backupaddress"))
        self.label_16 = QtGui.QLabel(self.expert)
        self.label_16.setGeometry(QtCore.QRect(10, 345, 851, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_16.setPalette(palette)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.saveamount = QtGui.QDoubleSpinBox(self.expert)
        self.saveamount.setGeometry(QtCore.QRect(170, 414, 93, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.saveamount.setFont(font)
        self.saveamount.setObjectName(_fromUtf8("saveamount"))
        self.autosave = QtGui.QCheckBox(self.expert)
        self.autosave.setGeometry(QtCore.QRect(170, 450, 531, 17))
        self.autosave.setObjectName(_fromUtf8("autosave"))
        self.tabWidget_4.addTab(self.expert, _fromUtf8(""))
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab6 = QtGui.QWidget()
        self.tab6.setObjectName(_fromUtf8("tab6"))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab6)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 120, 861, 391))
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.buyer = QtGui.QWidget()
        self.buyer.setObjectName(_fromUtf8("buyer"))
        self.label_24 = QtGui.QLabel(self.buyer)
        self.label_24.setGeometry(QtCore.QRect(10, 50, 101, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.lineEdit_2 = QtGui.QLineEdit(self.buyer)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 291, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Heiti Std R"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButtonManualEscrowBuyer = QtGui.QPushButton(self.buyer)
        self.pushButtonManualEscrowBuyer.setGeometry(QtCore.QRect(540, 40, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.5, 0.0001, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0709427, QtGui.QColor(60, 68, 79))
        gradient.setColorAt(0.947522, QtGui.QColor(73, 82, 97))
        gradient.setColorAt(0.958056, QtGui.QColor(90, 100, 112))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButtonManualEscrowBuyer.setPalette(palette)
        self.pushButtonManualEscrowBuyer.setStyleSheet(_fromUtf8("QWidget {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(76, 88, 102, 255), stop:1 rgba(65, 73, 86, 255));\n"
"    }\n"
"QPushButton\n"
"{\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-radius: 3px;\n"
"\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
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
"QSpinBox{\n"
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
"QSpinBox::up-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/up-arrow.png);\n"
"}\n"
"QSpinBox::down-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/down-arrow.png);\n"
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
""))
        self.pushButtonManualEscrowBuyer.setObjectName(_fromUtf8("pushButtonManualEscrowBuyer"))
        self.label_28 = QtGui.QLabel(self.buyer)
        self.label_28.setGeometry(QtCore.QRect(240, 108, 251, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.buyer)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 130, 861, 241))
        self.textBrowser_2.setStyleSheet(_fromUtf8("background-color: rgb(235, 235, 235);"))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label_25 = QtGui.QLabel(self.buyer)
        self.label_25.setGeometry(QtCore.QRect(460, 90, 371, 21))
        self.label_25.setStyleSheet(_fromUtf8(""))
        self.label_25.setText(_fromUtf8(""))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.spinBox_2 = QtGui.QDoubleSpinBox(self.buyer)
        self.spinBox_2.setGeometry(QtCore.QRect(419, 50, 101, 22))
        self.spinBox_2.setStyleSheet(_fromUtf8("QDoubleSpinBox{\n"
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
"   image: url(C:/QtQss/icons/up-arrow.png);\n"
"}\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/down-arrow.png);\n"
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
"}"))
        self.spinBox_2.setDecimals(10)
        self.spinBox_2.setMinimum(0.001)
        self.spinBox_2.setMaximum(999999.99)
        self.spinBox_2.setSingleStep(0.001)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.escrowlabelforbuyer = QtGui.QLineEdit(self.buyer)
        self.escrowlabelforbuyer.setGeometry(QtCore.QRect(100, 80, 291, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Heiti Std R"))
        self.escrowlabelforbuyer.setFont(font)
        self.escrowlabelforbuyer.setText(_fromUtf8(""))
        self.escrowlabelforbuyer.setObjectName(_fromUtf8("escrowlabelforbuyer"))
        self.frombox = QtGui.QComboBox(self.buyer)
        self.frombox.setGeometry(QtCore.QRect(100, 20, 291, 22))
        self.frombox.setObjectName(_fromUtf8("frombox"))
        self.frombox.addItem(_fromUtf8(""))
        self.pushButton_2 = QtGui.QPushButton(self.buyer)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 20, 91, 22))
        self.pushButton_2.setStyleSheet(_fromUtf8("QWidget {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(76, 88, 102, 255), stop:1 rgba(65, 73, 86, 255));\n"
"    }\n"
"QPushButton\n"
"{\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-radius: 3px;\n"
"\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
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
"QSpinBox{\n"
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
"QSpinBox::up-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/up-arrow.png);\n"
"}\n"
"QSpinBox::down-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/down-arrow.png);\n"
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
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.comment = QtGui.QPlainTextEdit(self.buyer)
        self.comment.setGeometry(QtCore.QRect(650, 10, 171, 111))
        self.comment.setOverwriteMode(True)
        self.comment.setObjectName(_fromUtf8("comment"))
        self.tabWidget_3.addTab(self.buyer, _fromUtf8(""))
        self.merchant = QtGui.QWidget()
        self.merchant.setObjectName(_fromUtf8("merchant"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.merchant)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 110, 861, 261))
        self.textBrowser_3.setStyleSheet(_fromUtf8("background-color: rgb(235, 235, 235);"))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label_40 = QtGui.QLabel(self.merchant)
        self.label_40.setGeometry(QtCore.QRect(0, 85, 301, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_26 = QtGui.QLabel(self.merchant)
        self.label_26.setGeometry(QtCore.QRect(450, 50, 341, 20))
        self.label_26.setText(_fromUtf8(""))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.newmerchantaddress = QtGui.QPushButton(self.merchant)
        self.newmerchantaddress.setGeometry(QtCore.QRect(74, 40, 211, 22))
        self.newmerchantaddress.setStyleSheet(_fromUtf8(""))
        self.newmerchantaddress.setObjectName(_fromUtf8("newmerchantaddress"))
        self.youids = QtGui.QTableWidget(self.merchant)
        self.youids.setGeometry(QtCore.QRect(330, 2, 481, 101))
        self.youids.setStyleSheet(_fromUtf8(""))
        self.youids.setFrameShadow(QtGui.QFrame.Sunken)
        self.youids.setLineWidth(1)
        self.youids.setAlternatingRowColors(False)
        self.youids.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.youids.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.youids.setColumnCount(1)
        self.youids.setObjectName(_fromUtf8("youids"))
        self.youids.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.youids.setHorizontalHeaderItem(0, item)
        self.youids.horizontalHeader().setCascadingSectionResizes(True)
        self.youids.horizontalHeader().setDefaultSectionSize(0)
        self.youids.horizontalHeader().setMinimumSectionSize(52)
        self.youids.horizontalHeader().setSortIndicatorShown(True)
        self.youids.horizontalHeader().setStretchLastSection(True)
        self.youids.verticalHeader().setVisible(False)
        self.youids.verticalHeader().setDefaultSectionSize(26)
        self.youids.verticalHeader().setSortIndicatorShown(False)
        self.youids.verticalHeader().setStretchLastSection(False)
        self.tabWidget_3.addTab(self.merchant, _fromUtf8(""))
        self.label_20 = QtGui.QLabel(self.tab6)
        self.label_20.setGeometry(QtCore.QRect(20, 20, 841, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setScaledContents(True)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.buyerhelp = QtGui.QLabel(self.tab6)
        self.buyerhelp.setGeometry(QtCore.QRect(420, 91, 441, 30))
        palette = QtGui.QPalette()
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 6, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 6, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.buyerhelp.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buyerhelp.setFont(font)
        self.buyerhelp.setStyleSheet(_fromUtf8(""))
        self.buyerhelp.setText(_fromUtf8(""))
        self.buyerhelp.setObjectName(_fromUtf8("buyerhelp"))
        self.tabWidget_2.addTab(self.tab6, _fromUtf8(""))
        self.tab7 = QtGui.QWidget()
        self.tab7.setObjectName(_fromUtf8("tab7"))
        self.tabWidget_5 = QtGui.QTabWidget(self.tab7)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 881, 511))
        self.tabWidget_5.setObjectName(_fromUtf8("tabWidget_5"))
        self.board = QtGui.QWidget()
        self.board.setObjectName(_fromUtf8("board"))
        self.checkBox = QtGui.QCheckBox(self.board)
        self.checkBox.setGeometry(QtCore.QRect(10, 66, 101, 21))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.offertype = QtGui.QComboBox(self.board)
        self.offertype.setGeometry(QtCore.QRect(10, 109, 201, 25))
        self.offertype.setObjectName(_fromUtf8("offertype"))
        self.offertype.addItem(_fromUtf8(""))
        self.offertype.addItem(_fromUtf8(""))
        self.offertype.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.board)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(3, 390, 221, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 208, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 208, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_12.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8(""))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.news = QtGui.QLabel(self.board)
        self.news.setGeometry(QtCore.QRect(3, 261, 221, 131))
        palette = QtGui.QPalette()
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.news.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.news.setFont(font)
        self.news.setText(_fromUtf8(""))
        self.news.setWordWrap(True)
        self.news.setObjectName(_fromUtf8("news"))
        self.pushButton_5 = QtGui.QPushButton(self.board)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 61, 81, 31))
        self.pushButton_5.setStyleSheet(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.lineEdit = QtGui.QLineEdit(self.board)
        self.lineEdit.setGeometry(QtCore.QRect(10, 232, 151, 20))
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.location = QtGui.QComboBox(self.board)
        self.location.setGeometry(QtCore.QRect(10, 190, 201, 25))
        self.location.setObjectName(_fromUtf8("location"))
        self.location.addItem(_fromUtf8(""))
        self.location.setItemText(0, _fromUtf8(""))
        self.blckchn = QtGui.QCheckBox(self.board)
        self.blckchn.setGeometry(QtCore.QRect(10, 31, 191, 21))
        self.blckchn.setChecked(True)
        self.blckchn.setObjectName(_fromUtf8("blckchn"))
        self.pushButton_4 = QtGui.QPushButton(self.board)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 231, 50, 21))
        self.pushButton_4.setStyleSheet(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.comboBox_2 = QtGui.QComboBox(self.board)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 150, 201, 25))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.textBrowser = QtGui.QTextBrowser(self.board)
        self.textBrowser.setGeometry(QtCore.QRect(230, 10, 651, 471))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgb(235, 235, 235);"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget_5.addTab(self.board, _fromUtf8(""))
        self.sell = QtGui.QWidget()
        self.sell.setObjectName(_fromUtf8("sell"))
        self.label_17 = QtGui.QLabel(self.sell)
        self.label_17.setGeometry(QtCore.QRect(50, 12, 131, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_17.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.offerslist = QtGui.QListWidget(self.sell)
        self.offerslist.setGeometry(QtCore.QRect(5, 40, 241, 401))
        self.offerslist.setObjectName(_fromUtf8("offerslist"))
        self.sellWidget = QtGui.QWidget(self.sell)
        self.sellWidget.setGeometry(QtCore.QRect(251, 2, 661, 571))
        self.sellWidget.setStyleSheet(_fromUtf8("/* ----- QPlainTextEdit ---- */\n"
"\n"
"QTextEdit {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}"))
        self.sellWidget.setObjectName(_fromUtf8("sellWidget"))
        self.productdetails = QtGui.QTextEdit(self.sellWidget)
        self.productdetails.setGeometry(QtCore.QRect(10, 250, 611, 191))
        self.productdetails.setObjectName(_fromUtf8("productdetails"))
        self.payandpost = QtGui.QPushButton(self.sellWidget)
        self.payandpost.setGeometry(QtCore.QRect(480, 446, 121, 31))
        self.payandpost.setObjectName(_fromUtf8("payandpost"))
        self.labelsc = QtGui.QLabel(self.sellWidget)
        self.labelsc.setGeometry(QtCore.QRect(10, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelsc.setFont(font)
        self.labelsc.setObjectName(_fromUtf8("labelsc"))
        self.lblscore = QtGui.QLabel(self.sellWidget)
        self.lblscore.setGeometry(QtCore.QRect(120, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblscore.setFont(font)
        self.lblscore.setObjectName(_fromUtf8("lblscore"))
        self.listaddresssell = QtGui.QComboBox(self.sellWidget)
        self.listaddresssell.setGeometry(QtCore.QRect(10, 40, 291, 22))
        self.listaddresssell.setObjectName(_fromUtf8("listaddresssell"))
        self.categorytext = QtGui.QTextEdit(self.sellWidget)
        self.categorytext.setGeometry(QtCore.QRect(10, 183, 611, 31))
        self.categorytext.setObjectName(_fromUtf8("categorytext"))
        self.lab3el_3 = QtGui.QLabel(self.sellWidget)
        self.lab3el_3.setGeometry(QtCore.QRect(10, 160, 831, 21))
        self.lab3el_3.setObjectName(_fromUtf8("lab3el_3"))
        self.la3bel_4 = QtGui.QLabel(self.sellWidget)
        self.la3bel_4.setGeometry(QtCore.QRect(10, 220, 831, 21))
        self.la3bel_4.setObjectName(_fromUtf8("la3bel_4"))
        self.labelprice = QtGui.QLabel(self.sellWidget)
        self.labelprice.setGeometry(QtCore.QRect(10, 447, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelprice.setFont(font)
        self.labelprice.setObjectName(_fromUtf8("labelprice"))
        self.sellprice = QtGui.QDoubleSpinBox(self.sellWidget)
        self.sellprice.setGeometry(QtCore.QRect(53, 454, 71, 20))
        self.sellprice.setDecimals(4)
        self.sellprice.setMinimum(0.001)
        self.sellprice.setMaximum(9999999.0)
        self.sellprice.setSingleStep(0.01)
        self.sellprice.setObjectName(_fromUtf8("sellprice"))
        self.onlyreted = QtGui.QCheckBox(self.sellWidget)
        self.onlyreted.setGeometry(QtCore.QRect(310, 40, 181, 23))
        self.onlyreted.setObjectName(_fromUtf8("onlyreted"))
        self.xcategory = QtGui.QComboBox(self.sellWidget)
        self.xcategory.setGeometry(QtCore.QRect(340, 87, 241, 22))
        self.xcategory.setObjectName(_fromUtf8("xcategory"))
        self.xcategory.addItem(_fromUtf8(""))
        self.xcategory.addItem(_fromUtf8(""))
        self.xcategory.addItem(_fromUtf8(""))
        self.label_18 = QtGui.QLabel(self.sellWidget)
        self.label_18.setGeometry(QtCore.QRect(340, 66, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.smthwrong = QtGui.QLabel(self.sellWidget)
        self.smthwrong.setGeometry(QtCore.QRect(180, 220, 431, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(106, 118, 132))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86, 5))
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
        self.label_19 = QtGui.QLabel(self.sellWidget)
        self.label_19.setGeometry(QtCore.QRect(20, 480, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.ratinlbl = QtGui.QLabel(self.sellWidget)
        self.ratinlbl.setGeometry(QtCore.QRect(130, 446, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ratinlbl.setFont(font)
        self.ratinlbl.setObjectName(_fromUtf8("ratinlbl"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.sellWidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(250, 453, 62, 20))
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMinimum(0.0)
        self.doubleSpinBox.setMaximum(99999999.0)
        self.doubleSpinBox.setSingleStep(0.0001)
        self.doubleSpinBox.setProperty("value", 0.001)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.contactsell = QtGui.QComboBox(self.sellWidget)
        self.contactsell.setGeometry(QtCore.QRect(10, 100, 291, 22))
        self.contactsell.setObjectName(_fromUtf8("contactsell"))
        self.contactsell.addItem(_fromUtf8(""))
        self.label213 = QtGui.QLabel(self.sellWidget)
        self.label213.setGeometry(QtCore.QRect(10, 127, 141, 21))
        self.label213.setObjectName(_fromUtf8("label213"))
        self.newsellcont = QtGui.QPushButton(self.sellWidget)
        self.newsellcont.setGeometry(QtCore.QRect(180, 130, 91, 22))
        self.newsellcont.setObjectName(_fromUtf8("newsellcont"))
        self.label_4231 = QtGui.QLabel(self.sellWidget)
        self.label_4231.setGeometry(QtCore.QRect(10, 60, 291, 21))
        self.label_4231.setObjectName(_fromUtf8("label_4231"))
        self.label_21 = QtGui.QLabel(self.sellWidget)
        self.label_21.setGeometry(QtCore.QRect(340, 118, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.location_2 = QtGui.QComboBox(self.sellWidget)
        self.location_2.setGeometry(QtCore.QRect(340, 138, 241, 22))
        self.location_2.setObjectName(_fromUtf8("location_2"))
        self.label_22 = QtGui.QLabel(self.sellWidget)
        self.label_22.setGeometry(QtCore.QRect(170, 0, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.prolong = QtGui.QPushButton(self.sellWidget)
        self.prolong.setGeometry(QtCore.QRect(360, 446, 75, 31))
        self.prolong.setObjectName(_fromUtf8("prolong"))
        self.resend = QtGui.QPushButton(self.sell)
        self.resend.setGeometry(QtCore.QRect(30, 446, 171, 31))
        self.resend.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain))
        self.resend.setObjectName(_fromUtf8("resend"))
        self.tabWidget_5.addTab(self.sell, _fromUtf8(""))
        self.tabWidget_2.addTab(self.tab7, _fromUtf8(""))
        self.Advenced_messaging = QtGui.QWidget()
        self.Advenced_messaging.setObjectName(_fromUtf8("Advenced_messaging"))
        self.gridLayoutWidget = QtGui.QWidget(self.Advenced_messaging)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 881, 521))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.Advenced_messaging)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 881, 520))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet(_fromUtf8("QTabBar::tab {width: 98px; }"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.inbox = QtGui.QWidget()
        self.inbox.setObjectName(_fromUtf8("inbox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.inbox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayoutSearch = QtGui.QHBoxLayout()
        self.horizontalLayoutSearch.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayoutSearch.setObjectName(_fromUtf8("horizontalLayoutSearch"))
        self.inboxSearchLineEdit = QtGui.QLineEdit(self.inbox)
        self.inboxSearchLineEdit.setObjectName(_fromUtf8("inboxSearchLineEdit"))
        self.horizontalLayoutSearch.addWidget(self.inboxSearchLineEdit)
        self.inboxSearchOptionCB = QtGui.QComboBox(self.inbox)
        self.inboxSearchOptionCB.setObjectName(_fromUtf8("inboxSearchOptionCB"))
        self.inboxSearchOptionCB.addItem(_fromUtf8(""))
        self.inboxSearchOptionCB.addItem(_fromUtf8(""))
        self.inboxSearchOptionCB.addItem(_fromUtf8(""))
        self.inboxSearchOptionCB.addItem(_fromUtf8(""))
        self.inboxSearchOptionCB.addItem(_fromUtf8(""))
        self.horizontalLayoutSearch.addWidget(self.inboxSearchOptionCB)
        self.verticalLayout_2.addLayout(self.horizontalLayoutSearch)
        self.splitter = QtGui.QSplitter(self.inbox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tableWidgetInbox = QtGui.QTableWidget(self.splitter)
        self.tableWidgetInbox.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetInbox.setAlternatingRowColors(False)
        self.tableWidgetInbox.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidgetInbox.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetInbox.setWordWrap(False)
        self.tableWidgetInbox.setObjectName(_fromUtf8("tableWidgetInbox"))
        self.tableWidgetInbox.setColumnCount(4)
        self.tableWidgetInbox.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetInbox.setHorizontalHeaderItem(3, item)
        self.tableWidgetInbox.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetInbox.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidgetInbox.horizontalHeader().setHighlightSections(False)
        self.tableWidgetInbox.horizontalHeader().setMinimumSectionSize(27)
        self.tableWidgetInbox.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetInbox.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetInbox.verticalHeader().setVisible(False)
        self.tableWidgetInbox.verticalHeader().setDefaultSectionSize(26)
        self.textEditInboxMessage = QtGui.QTextEdit(self.splitter)
        self.textEditInboxMessage.setBaseSize(QtCore.QSize(0, 500))
        self.textEditInboxMessage.setReadOnly(True)
        self.textEditInboxMessage.setObjectName(_fromUtf8("textEditInboxMessage"))
        self.verticalLayout_2.addWidget(self.splitter)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/inbox.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.inbox, icon1, _fromUtf8(""))
        self.send = QtGui.QWidget()
        self.send.setObjectName(_fromUtf8("send"))
        self.pushButtonLoadFromAddressBook = QtGui.QPushButton(self.send)
        self.pushButtonLoadFromAddressBook.setGeometry(QtCore.QRect(335, 78, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButtonLoadFromAddressBook.setFont(font)
        self.pushButtonLoadFromAddressBook.setObjectName(_fromUtf8("pushButtonLoadFromAddressBook"))
        self.pushButtonFetchNamecoinID = QtGui.QPushButton(self.send)
        self.pushButtonFetchNamecoinID.setGeometry(QtCore.QRect(462, 78, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButtonFetchNamecoinID.setFont(font)
        self.pushButtonFetchNamecoinID.setObjectName(_fromUtf8("pushButtonFetchNamecoinID"))
        self.label_4 = QtGui.QLabel(self.send)
        self.label_4.setGeometry(QtCore.QRect(9, 126, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBoxSendFrom = QtGui.QComboBox(self.send)
        self.comboBoxSendFrom.setGeometry(QtCore.QRect(61, 53, 261, 20))
        self.comboBoxSendFrom.setMinimumSize(QtCore.QSize(99, 0))
        self.comboBoxSendFrom.setObjectName(_fromUtf8("comboBoxSendFrom"))
        self.label_3 = QtGui.QLabel(self.send)
        self.label_3.setGeometry(QtCore.QRect(9, 101, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.labelFrom = QtGui.QLabel(self.send)
        self.labelFrom.setGeometry(QtCore.QRect(354, 53, 16, 16))
        self.labelFrom.setText(_fromUtf8(""))
        self.labelFrom.setObjectName(_fromUtf8("labelFrom"))
        self.radioButtonSpecific = QtGui.QRadioButton(self.send)
        self.radioButtonSpecific.setGeometry(QtCore.QRect(61, 9, 193, 16))
        self.radioButtonSpecific.setChecked(True)
        self.radioButtonSpecific.setObjectName(_fromUtf8("radioButtonSpecific"))
        self.lineEditTo = QtGui.QLineEdit(self.send)
        self.lineEditTo.setGeometry(QtCore.QRect(61, 78, 261, 20))
        self.lineEditTo.setObjectName(_fromUtf8("lineEditTo"))
        self.textEditMessage = QtGui.QTextEdit(self.send)
        self.textEditMessage.setGeometry(QtCore.QRect(61, 126, 801, 331))
        self.textEditMessage.setObjectName(_fromUtf8("textEditMessage"))
        self.label = QtGui.QLabel(self.send)
        self.label.setGeometry(QtCore.QRect(9, 76, 28, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.send)
        self.label_2.setGeometry(QtCore.QRect(9, 52, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButtonBroadcast = QtGui.QRadioButton(self.send)
        self.radioButtonBroadcast.setGeometry(QtCore.QRect(61, 31, 298, 16))
        self.radioButtonBroadcast.setObjectName(_fromUtf8("radioButtonBroadcast"))
        self.lineEditSubject = QtGui.QLineEdit(self.send)
        self.lineEditSubject.setGeometry(QtCore.QRect(61, 103, 261, 20))
        self.lineEditSubject.setText(_fromUtf8(""))
        self.lineEditSubject.setObjectName(_fromUtf8("lineEditSubject"))
        self.pushButtonSend = QtGui.QPushButton(self.send)
        self.pushButtonSend.setGeometry(QtCore.QRect(769, 463, 101, 20))
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.labelSendBroadcastWarning = QtGui.QLabel(self.send)
        self.labelSendBroadcastWarning.setEnabled(True)
        self.labelSendBroadcastWarning.setGeometry(QtCore.QRect(11, 462, 751, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSendBroadcastWarning.sizePolicy().hasHeightForWidth())
        self.labelSendBroadcastWarning.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSendBroadcastWarning.setFont(font)
        self.labelSendBroadcastWarning.setIndent(-1)
        self.labelSendBroadcastWarning.setObjectName(_fromUtf8("labelSendBroadcastWarning"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/send.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.send, icon2, _fromUtf8(""))
        self.sent = QtGui.QWidget()
        self.sent.setObjectName(_fromUtf8("sent"))
        self.verticalLayout = QtGui.QVBoxLayout(self.sent)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sentSearchLineEdit = QtGui.QLineEdit(self.sent)
        self.sentSearchLineEdit.setObjectName(_fromUtf8("sentSearchLineEdit"))
        self.horizontalLayout.addWidget(self.sentSearchLineEdit)
        self.sentSearchOptionCB = QtGui.QComboBox(self.sent)
        self.sentSearchOptionCB.setObjectName(_fromUtf8("sentSearchOptionCB"))
        self.sentSearchOptionCB.addItem(_fromUtf8(""))
        self.sentSearchOptionCB.addItem(_fromUtf8(""))
        self.sentSearchOptionCB.addItem(_fromUtf8(""))
        self.sentSearchOptionCB.addItem(_fromUtf8(""))
        self.sentSearchOptionCB.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.sentSearchOptionCB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter_2 = QtGui.QSplitter(self.sent)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.tableWidgetSent = QtGui.QTableWidget(self.splitter_2)
        self.tableWidgetSent.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetSent.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tableWidgetSent.setAlternatingRowColors(False)
        self.tableWidgetSent.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidgetSent.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetSent.setWordWrap(False)
        self.tableWidgetSent.setObjectName(_fromUtf8("tableWidgetSent"))
        self.tableWidgetSent.setColumnCount(4)
        self.tableWidgetSent.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSent.setHorizontalHeaderItem(3, item)
        self.tableWidgetSent.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetSent.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidgetSent.horizontalHeader().setHighlightSections(False)
        self.tableWidgetSent.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetSent.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSent.verticalHeader().setVisible(False)
        self.tableWidgetSent.verticalHeader().setStretchLastSection(False)
        self.textEditSentMessage = QtGui.QTextEdit(self.splitter_2)
        self.textEditSentMessage.setReadOnly(True)
        self.textEditSentMessage.setObjectName(_fromUtf8("textEditSentMessage"))
        self.verticalLayout.addWidget(self.splitter_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/sent.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.sent, icon3, _fromUtf8(""))
        self.youridentities = QtGui.QWidget()
        self.youridentities.setObjectName(_fromUtf8("youridentities"))
        self.pushButtonNewAddress = QtGui.QPushButton(self.youridentities)
        self.pushButtonNewAddress.setGeometry(QtCore.QRect(9, 9, 75, 23))
        self.pushButtonNewAddress.setStyleSheet(_fromUtf8("QWidget {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(76, 88, 102, 255), stop:1 rgba(65, 73, 86, 255));\n"
"    }\n"
"QPushButton\n"
"{\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-radius: 3px;\n"
"\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
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
"QSpinBox{\n"
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
"QSpinBox::up-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/up-arrow.png);\n"
"}\n"
"QSpinBox::down-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/down-arrow.png);\n"
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
""))
        self.pushButtonNewAddress.setObjectName(_fromUtf8("pushButtonNewAddress"))
        self.tableWidgetYourIdentities = QtGui.QTableWidget(self.youridentities)
        self.tableWidgetYourIdentities.setGeometry(QtCore.QRect(9, 38, 847, 441))
        self.tableWidgetYourIdentities.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidgetYourIdentities.setLineWidth(1)
        self.tableWidgetYourIdentities.setAlternatingRowColors(False)
        self.tableWidgetYourIdentities.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetYourIdentities.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetYourIdentities.setObjectName(_fromUtf8("tableWidgetYourIdentities"))
        self.tableWidgetYourIdentities.setColumnCount(3)
        self.tableWidgetYourIdentities.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tableWidgetYourIdentities.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetYourIdentities.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetYourIdentities.setHorizontalHeaderItem(2, item)
        self.tableWidgetYourIdentities.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetYourIdentities.horizontalHeader().setDefaultSectionSize(346)
        self.tableWidgetYourIdentities.horizontalHeader().setMinimumSectionSize(52)
        self.tableWidgetYourIdentities.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetYourIdentities.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetYourIdentities.verticalHeader().setVisible(False)
        self.tableWidgetYourIdentities.verticalHeader().setDefaultSectionSize(26)
        self.tableWidgetYourIdentities.verticalHeader().setSortIndicatorShown(False)
        self.tableWidgetYourIdentities.verticalHeader().setStretchLastSection(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/identities.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.youridentities, icon4, _fromUtf8(""))
        self.subscriptions = QtGui.QWidget()
        self.subscriptions.setObjectName(_fromUtf8("subscriptions"))
        self.label_5 = QtGui.QLabel(self.subscriptions)
        self.label_5.setGeometry(QtCore.QRect(9, 9, 800, 16))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButtonAddSubscription = QtGui.QPushButton(self.subscriptions)
        self.pushButtonAddSubscription.setGeometry(QtCore.QRect(9, 28, 111, 23))
        self.pushButtonAddSubscription.setStyleSheet(_fromUtf8("QWidget {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(76, 88, 102, 255), stop:1 rgba(65, 73, 86, 255));\n"
"    }\n"
"QPushButton\n"
"{\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-radius: 3px;\n"
"\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
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
"QSpinBox{\n"
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
"QSpinBox::up-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/up-arrow.png);\n"
"}\n"
"QSpinBox::down-arrow\n"
"{\n"
"   image: url(C:/QtQss/icons/down-arrow.png);\n"
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
""))
        self.pushButtonAddSubscription.setObjectName(_fromUtf8("pushButtonAddSubscription"))
        self.tableWidgetSubscriptions = QtGui.QTableWidget(self.subscriptions)
        self.tableWidgetSubscriptions.setGeometry(QtCore.QRect(9, 57, 851, 421))
        self.tableWidgetSubscriptions.setAlternatingRowColors(False)
        self.tableWidgetSubscriptions.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetSubscriptions.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetSubscriptions.setObjectName(_fromUtf8("tableWidgetSubscriptions"))
        self.tableWidgetSubscriptions.setColumnCount(2)
        self.tableWidgetSubscriptions.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSubscriptions.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSubscriptions.setHorizontalHeaderItem(1, item)
        self.tableWidgetSubscriptions.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetSubscriptions.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidgetSubscriptions.horizontalHeader().setHighlightSections(False)
        self.tableWidgetSubscriptions.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetSubscriptions.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSubscriptions.verticalHeader().setVisible(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/subscriptions.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.subscriptions, icon5, _fromUtf8(""))
        self.addressbook = QtGui.QWidget()
        self.addressbook.setObjectName(_fromUtf8("addressbook"))
        self.label_6 = QtGui.QLabel(self.addressbook)
        self.label_6.setGeometry(QtCore.QRect(9, 9, 861, 26))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButtonAddAddressBook = QtGui.QPushButton(self.addressbook)
        self.pushButtonAddAddressBook.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.pushButtonAddAddressBook.setObjectName(_fromUtf8("pushButtonAddAddressBook"))
        self.tableWidgetAddressBook = QtGui.QTableWidget(self.addressbook)
        self.tableWidgetAddressBook.setGeometry(QtCore.QRect(9, 64, 851, 421))
        self.tableWidgetAddressBook.setAlternatingRowColors(False)
        self.tableWidgetAddressBook.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidgetAddressBook.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetAddressBook.setObjectName(_fromUtf8("tableWidgetAddressBook"))
        self.tableWidgetAddressBook.setColumnCount(2)
        self.tableWidgetAddressBook.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddressBook.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetAddressBook.setHorizontalHeaderItem(1, item)
        self.tableWidgetAddressBook.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetAddressBook.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidgetAddressBook.horizontalHeader().setHighlightSections(False)
        self.tableWidgetAddressBook.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetAddressBook.verticalHeader().setVisible(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/addressbook.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.addressbook, icon6, _fromUtf8(""))
        self.blackwhitelist = QtGui.QWidget()
        self.blackwhitelist.setObjectName(_fromUtf8("blackwhitelist"))
        self.gridLayout_7 = QtGui.QGridLayout(self.blackwhitelist)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.radioButtonBlacklist = QtGui.QRadioButton(self.blackwhitelist)
        self.radioButtonBlacklist.setChecked(True)
        self.radioButtonBlacklist.setObjectName(_fromUtf8("radioButtonBlacklist"))
        self.gridLayout_7.addWidget(self.radioButtonBlacklist, 0, 0, 1, 2)
        self.radioButtonWhitelist = QtGui.QRadioButton(self.blackwhitelist)
        self.radioButtonWhitelist.setObjectName(_fromUtf8("radioButtonWhitelist"))
        self.gridLayout_7.addWidget(self.radioButtonWhitelist, 1, 0, 1, 2)
        self.pushButtonAddBlacklist = QtGui.QPushButton(self.blackwhitelist)
        self.pushButtonAddBlacklist.setObjectName(_fromUtf8("pushButtonAddBlacklist"))
        self.gridLayout_7.addWidget(self.pushButtonAddBlacklist, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(689, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 2, 1, 1, 1)
        self.tableWidgetBlacklist = QtGui.QTableWidget(self.blackwhitelist)
        self.tableWidgetBlacklist.setAlternatingRowColors(False)
        self.tableWidgetBlacklist.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetBlacklist.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetBlacklist.setObjectName(_fromUtf8("tableWidgetBlacklist"))
        self.tableWidgetBlacklist.setColumnCount(2)
        self.tableWidgetBlacklist.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetBlacklist.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetBlacklist.setHorizontalHeaderItem(1, item)
        self.tableWidgetBlacklist.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetBlacklist.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidgetBlacklist.horizontalHeader().setHighlightSections(False)
        self.tableWidgetBlacklist.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetBlacklist.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetBlacklist.verticalHeader().setVisible(False)
        self.gridLayout_7.addWidget(self.tableWidgetBlacklist, 3, 0, 1, 2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/blacklist.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.blackwhitelist, icon7, _fromUtf8(""))
        self.networkstatus = QtGui.QWidget()
        self.networkstatus.setObjectName(_fromUtf8("networkstatus"))
        self.pushButtonStatusIcon = QtGui.QPushButton(self.networkstatus)
        self.pushButtonStatusIcon.setGeometry(QtCore.QRect(680, 440, 21, 23))
        self.pushButtonStatusIcon.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/redicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStatusIcon.setIcon(icon8)
        self.pushButtonStatusIcon.setFlat(True)
        self.pushButtonStatusIcon.setObjectName(_fromUtf8("pushButtonStatusIcon"))
        self.tableWidgetConnectionCount = QtGui.QTableWidget(self.networkstatus)
        self.tableWidgetConnectionCount.setGeometry(QtCore.QRect(20, 70, 241, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.955, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(63, 109, 184))
        gradient.setColorAt(1.0, QtGui.QColor(90, 155, 209))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.955, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(63, 109, 184))
        gradient.setColorAt(1.0, QtGui.QColor(90, 155, 209))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 53, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.955, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(63, 109, 184))
        gradient.setColorAt(1.0, QtGui.QColor(90, 155, 209))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tableWidgetConnectionCount.setPalette(palette)
        self.tableWidgetConnectionCount.setStyleSheet(_fromUtf8(""))
        self.tableWidgetConnectionCount.setFrameShape(QtGui.QFrame.Box)
        self.tableWidgetConnectionCount.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidgetConnectionCount.setProperty("showDropIndicator", False)
        self.tableWidgetConnectionCount.setAlternatingRowColors(False)
        self.tableWidgetConnectionCount.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidgetConnectionCount.setObjectName(_fromUtf8("tableWidgetConnectionCount"))
        self.tableWidgetConnectionCount.setColumnCount(2)
        self.tableWidgetConnectionCount.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetConnectionCount.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetConnectionCount.setHorizontalHeaderItem(1, item)
        self.tableWidgetConnectionCount.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetConnectionCount.horizontalHeader().setHighlightSections(False)
        self.tableWidgetConnectionCount.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetConnectionCount.verticalHeader().setVisible(False)
        self.labelTotalConnections = QtGui.QLabel(self.networkstatus)
        self.labelTotalConnections.setGeometry(QtCore.QRect(20, 30, 401, 16))
        self.labelTotalConnections.setObjectName(_fromUtf8("labelTotalConnections"))
        self.labelStartupTime = QtGui.QLabel(self.networkstatus)
        self.labelStartupTime.setGeometry(QtCore.QRect(320, 110, 331, 20))
        self.labelStartupTime.setObjectName(_fromUtf8("labelStartupTime"))
        self.labelMessageCount = QtGui.QLabel(self.networkstatus)
        self.labelMessageCount.setGeometry(QtCore.QRect(350, 130, 361, 16))
        self.labelMessageCount.setObjectName(_fromUtf8("labelMessageCount"))
        self.labelPubkeyCount = QtGui.QLabel(self.networkstatus)
        self.labelPubkeyCount.setGeometry(QtCore.QRect(350, 170, 331, 16))
        self.labelPubkeyCount.setObjectName(_fromUtf8("labelPubkeyCount"))
        self.labelBroadcastCount = QtGui.QLabel(self.networkstatus)
        self.labelBroadcastCount.setGeometry(QtCore.QRect(350, 150, 351, 16))
        self.labelBroadcastCount.setObjectName(_fromUtf8("labelBroadcastCount"))
        self.labelLookupsPerSecond = QtGui.QLabel(self.networkstatus)
        self.labelLookupsPerSecond.setGeometry(QtCore.QRect(320, 210, 291, 16))
        self.labelLookupsPerSecond.setObjectName(_fromUtf8("labelLookupsPerSecond"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/images/networkstatus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.networkstatus, icon9, _fromUtf8(""))
        self.tabWidget_2.addTab(self.Advenced_messaging, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(True)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionImport_keys = QtGui.QAction(MainWindow)
        self.actionImport_keys.setObjectName(_fromUtf8("actionImport_keys"))
        self.actionManageKeys = QtGui.QAction(MainWindow)
        self.actionManageKeys.setCheckable(False)
        self.actionManageKeys.setEnabled(True)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("dialog-password"))
        self.actionManageKeys.setIcon(icon)
        self.actionManageKeys.setObjectName(_fromUtf8("actionManageKeys"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("application-exit"))
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHelp = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-contents"))
        self.actionHelp.setIcon(icon)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-about"))
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-properties"))
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionRegenerateDeterministicAddresses = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("view-refresh"))
        self.actionRegenerateDeterministicAddresses.setIcon(icon)
        self.actionRegenerateDeterministicAddresses.setObjectName(_fromUtf8("actionRegenerateDeterministicAddresses"))
        self.actionDeleteAllTrashedMessages = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("user-trash"))
        self.actionDeleteAllTrashedMessages.setIcon(icon)
        self.actionDeleteAllTrashedMessages.setObjectName(_fromUtf8("actionDeleteAllTrashedMessages"))
        self.actionJoinChan = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("contact-new"))
        self.actionJoinChan.setIcon(icon)
        self.actionJoinChan.setObjectName(_fromUtf8("actionJoinChan"))
        self.menuFile.addAction(self.actionManageKeys)
        self.menuFile.addAction(self.actionDeleteAllTrashedMessages)
        self.menuFile.addAction(self.actionRegenerateDeterministicAddresses)
        self.menuFile.addAction(self.actionJoinChan)
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BitXBay", None))
        self.label_49.setText(_translate("MainWindow", "Transactions", None))
        self.label_9.setText(_translate("MainWindow", "Unconfirmed:", None))
        self.label_7.setText(_translate("MainWindow", "Wallet", None))
        self.label_8.setText(_translate("MainWindow", "Balance:", None))
        self.bitcoinaddresses.setSortingEnabled(True)
        item = self.bitcoinaddresses.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Label", None))
        item = self.bitcoinaddresses.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        item = self.bitcoinaddresses.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount", None))
        self.label_ucbalance.setText(_translate("MainWindow", "0", None))
        self.pushButton.setText(_translate("MainWindow", "New btc address", None))
        self.sync_label.setText(_translate("MainWindow", "(out of sync)", None))
        self.label_11.setText(_translate("MainWindow", "Amount must be >0", None))
        self.label_balance.setText(_translate("MainWindow", "0", None))
        self.label_48.setText(_translate("MainWindow", "Pay to:", None))
        self.label_50.setText(_translate("MainWindow", "Label:", None))
        self.label_51.setText(_translate("MainWindow", "Amount:", None))
        self.sendbtc.setText(_translate("MainWindow", "Send", None))
        self.label_52.setText(_translate("MainWindow", "My addresses", None))
        self.label_44.setText(_translate("MainWindow", "Send", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.Main), _translate("MainWindow", "Main", None))
        self.label_10.setText(_translate("MainWindow", "Be careful to use these functions. Be sure to backup wallet.dat. Here you can solve common problems. Dump/import priv keys, remove forever unconfirmed transactions and unnecessary addresses. Don\'t forget that these addresses can have unspent transactions. To see changings, start bitcoin-qt with -rescan.", None))
        self.importprivkey.setText(_translate("MainWindow", "Import private key", None))
        self.privkey.setPlaceholderText(_translate("MainWindow", "Input here private key", None))
        self.label_13.setText(_translate("MainWindow", "You can find it in escrow messages in {private*{ }private*}", None))
        self.dumpkey.setText(_translate("MainWindow", "Dump private key", None))
        self.dumpaddress.setPlaceholderText(_translate("MainWindow", "Input here bitcoin address", None))
        self.privdump.setText(_translate("MainWindow", "Priv key:", None))
        self.deltx.setText(_translate("MainWindow", "Delete transaction", None))
        self.tx.setPlaceholderText(_translate("MainWindow", "Transaction. Copy it without \"-000\"", None))
        self.label_14.setText(_translate("MainWindow", "It is just for delete forever unconfirmed txs. Rescan after do it.", None))
        self.deltx_2.setText(_translate("MainWindow", "Delete address", None))
        self.tx_2.setPlaceholderText(_translate("MainWindow", "Input here bitcoin address", None))
        self.label_15.setText(_translate("MainWindow", "You can delete escrow or other address. Sometimes after deal you can see not your transactions. Delete unused escrow address can solve this.", None))
        self.savebtc.setText(_translate("MainWindow", "Send now", None))
        self.backupaddress.setPlaceholderText(_translate("MainWindow", "Input here bitcoin address", None))
        self.label_16.setText(_translate("MainWindow", "Send all money over amount to specified address. It is help save most funds if you lost actual wallet.dat. Be careful if you don\'t backup money you can loose it if new wallet.dat will be lost. Autosave don\'t send small amounts about 0.0001-0.005. To avoid bitcoin fee.", None))
        self.autosave.setText(_translate("MainWindow", "Send all bitcoins, when amount on wallet more then 0.005 over this amount.", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.expert), _translate("MainWindow", "Expert", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Wallet", None))
        self.label_24.setText(_translate("MainWindow", "Auto deal:", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "BitXBay escrow address of merchant", None))
        self.pushButtonManualEscrowBuyer.setText(_translate("MainWindow", "Start deal", None))
        self.label_28.setText(_translate("MainWindow", "Auto escrow deals that not finished:", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.escrowlabelforbuyer.setPlaceholderText(_translate("MainWindow", "Label for escrow deal", None))
        self.frombox.setItemText(0, _translate("MainWindow", "Select bitmessage sender\'s address", None))
        self.pushButton_2.setText(_translate("MainWindow", " New address", None))
        self.comment.setPlainText(_translate("MainWindow", "Comment for merchant. Type here the shipping address or other important information.", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.buyer), _translate("MainWindow", "Buyer", None))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_40.setText(_translate("MainWindow", "Auto escrow deals that not finished:", None))
        self.newmerchantaddress.setText(_translate("MainWindow", " New merchant escrow address", None))
        self.youids.setSortingEnabled(True)
        item = self.youids.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.merchant), _translate("MainWindow", "Merchant", None))
        self.label_20.setText(_translate("MainWindow", "Escrow is a deal type in which the money is stuck between the seller and the buyer. BitXBay escrow is a deal between two parties without intermediaries. Intermediaries replaced by 5% insurence payments from buyer and seller to multisig addresses. Both parties can get back insurent payments only when the deal completed successfully or canceled by both parties as well by both parties. The process takes place without the use of a third party, using multisig bitcoin addresses. These addresses are created with the public keys of both parties.\n"
" ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab6), _translate("MainWindow", "Escrow", None))
        self.checkBox.setText(_translate("MainWindow", "Auto refresh", None))
        self.offertype.setItemText(0, _translate("MainWindow", "Goods", None))
        self.offertype.setItemText(1, _translate("MainWindow", "Services", None))
        self.offertype.setItemText(2, _translate("MainWindow", "Currency exchange", None))
        self.pushButton_5.setText(_translate("MainWindow", "Refresh", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.blckchn.setText(_translate("MainWindow", "Get TXs from Blockchain.info", None))
        self.pushButton_4.setText(_translate("MainWindow", "Search", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Categories", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.board), _translate("MainWindow", "Board", None))
        self.label_17.setText(_translate("MainWindow", "Your offers", None))
        self.payandpost.setText(_translate("MainWindow", "Pay and post/change", None))
        self.labelsc.setText(_translate("MainWindow", "Address score:", None))
        self.lblscore.setText(_translate("MainWindow", "0", None))
        self.lab3el_3.setText(_translate("MainWindow", "Category. Everyone can create a category. But it is better to use an existing one.", None))
        self.la3bel_4.setText(_translate("MainWindow", "Product or service details", None))
        self.labelprice.setText(_translate("MainWindow", "Price:", None))
        self.onlyreted.setText(_translate("MainWindow", "Show only rated addresses", None))
        self.xcategory.setItemText(0, _translate("MainWindow", "Goods", None))
        self.xcategory.setItemText(1, _translate("MainWindow", "Services", None))
        self.xcategory.setItemText(2, _translate("MainWindow", "Currencies", None))
        self.label_18.setText(_translate("MainWindow", "Type of offer", None))
        self.label_19.setText(_translate("MainWindow", "For better position pay more.", None))
        self.ratinlbl.setText(_translate("MainWindow", "Rating payment:", None))
        self.contactsell.setItemText(0, _translate("MainWindow", "Contact address", None))
        self.label213.setText(_translate("MainWindow", "Contact address", None))
        self.newsellcont.setText(_translate("MainWindow", "New contact", None))
        self.label_4231.setText(_translate("MainWindow", "Bitcoin address for sign message and rating payment.", None))
        self.label_21.setText(_translate("MainWindow", "Location", None))
        self.label_22.setText(_translate("MainWindow", "Sign different offers by different addresses. For update, use the same address.", None))
        self.prolong.setText(_translate("MainWindow", "Prolong", None))
        self.resend.setText(_translate("MainWindow", "Prolong all offers", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.sell), _translate("MainWindow", "Sell", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab7), _translate("MainWindow", "Decentralized trade", None))
        self.inboxSearchLineEdit.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.inboxSearchOptionCB.setItemText(0, _translate("MainWindow", "All", None))
        self.inboxSearchOptionCB.setItemText(1, _translate("MainWindow", "To", None))
        self.inboxSearchOptionCB.setItemText(2, _translate("MainWindow", "From", None))
        self.inboxSearchOptionCB.setItemText(3, _translate("MainWindow", "Subject", None))
        self.inboxSearchOptionCB.setItemText(4, _translate("MainWindow", "Message", None))
        self.tableWidgetInbox.setSortingEnabled(True)
        item = self.tableWidgetInbox.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "To", None))
        item = self.tableWidgetInbox.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "From", None))
        item = self.tableWidgetInbox.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Subject", None))
        item = self.tableWidgetInbox.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Received", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inbox), _translate("MainWindow", "Inbox", None))
        self.pushButtonLoadFromAddressBook.setText(_translate("MainWindow", "Load from Address book", None))
        self.pushButtonFetchNamecoinID.setText(_translate("MainWindow", "Fetch Namecoin ID", None))
        self.label_4.setText(_translate("MainWindow", "Message:", None))
        self.label_3.setText(_translate("MainWindow", "Subject:", None))
        self.radioButtonSpecific.setText(_translate("MainWindow", "Send to one or more specific people", None))
        self.textEditMessage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "To:", None))
        self.label_2.setText(_translate("MainWindow", "From:", None))
        self.radioButtonBroadcast.setText(_translate("MainWindow", "Broadcast to everyone who is subscribed to your address", None))
        self.pushButtonSend.setText(_translate("MainWindow", "Send", None))
        self.labelSendBroadcastWarning.setText(_translate("MainWindow", "Be aware that broadcasts are only encrypted with your address. Anyone who knows your address can read them.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.send), _translate("MainWindow", "Send", None))
        self.sentSearchLineEdit.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.sentSearchOptionCB.setItemText(0, _translate("MainWindow", "All", None))
        self.sentSearchOptionCB.setItemText(1, _translate("MainWindow", "To", None))
        self.sentSearchOptionCB.setItemText(2, _translate("MainWindow", "From", None))
        self.sentSearchOptionCB.setItemText(3, _translate("MainWindow", "Subject", None))
        self.sentSearchOptionCB.setItemText(4, _translate("MainWindow", "Message", None))
        self.tableWidgetSent.setSortingEnabled(True)
        item = self.tableWidgetSent.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "To", None))
        item = self.tableWidgetSent.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "From", None))
        item = self.tableWidgetSent.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Subject", None))
        item = self.tableWidgetSent.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sent), _translate("MainWindow", "Sent", None))
        self.pushButtonNewAddress.setText(_translate("MainWindow", "New", None))
        self.tableWidgetYourIdentities.setSortingEnabled(True)
        item = self.tableWidgetYourIdentities.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Label (not shown to anyone)", None))
        item = self.tableWidgetYourIdentities.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        item = self.tableWidgetYourIdentities.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Stream", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.youridentities), _translate("MainWindow", "Your Identities", None))
        self.label_5.setText(_translate("MainWindow", "Here you can subscribe to \'broadcast messages\' that are sent by other users. Messages will appear in your Inbox. Addresses here override those on the Blacklist tab.", None))
        self.pushButtonAddSubscription.setText(_translate("MainWindow", "Add new Subscription", None))
        self.tableWidgetSubscriptions.setSortingEnabled(True)
        item = self.tableWidgetSubscriptions.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Label", None))
        item = self.tableWidgetSubscriptions.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subscriptions), _translate("MainWindow", "Subscriptions", None))
        self.label_6.setText(_translate("MainWindow", "The Address book is useful for adding names or labels to other people\'s Bitmessage addresses so that you can recognize them more easily in your inbox. You can add entries here using the \'Add\' button, or from your inbox by right-clicking on a message.", None))
        self.pushButtonAddAddressBook.setText(_translate("MainWindow", "Add new entry", None))
        self.tableWidgetAddressBook.setSortingEnabled(True)
        item = self.tableWidgetAddressBook.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name or Label", None))
        item = self.tableWidgetAddressBook.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addressbook), _translate("MainWindow", "Address Book", None))
        self.radioButtonBlacklist.setText(_translate("MainWindow", "Use a Blacklist (Allow all incoming messages except those on the Blacklist)", None))
        self.radioButtonWhitelist.setText(_translate("MainWindow", "Use a Whitelist (Block all incoming messages except those on the Whitelist)", None))
        self.pushButtonAddBlacklist.setText(_translate("MainWindow", "Add new entry", None))
        self.tableWidgetBlacklist.setSortingEnabled(True)
        item = self.tableWidgetBlacklist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name or Label", None))
        item = self.tableWidgetBlacklist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.blackwhitelist), _translate("MainWindow", "Blacklist", None))
        item = self.tableWidgetConnectionCount.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stream #", None))
        item = self.tableWidgetConnectionCount.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Connections", None))
        self.labelTotalConnections.setText(_translate("MainWindow", "Total connections: 0", None))
        self.labelStartupTime.setText(_translate("MainWindow", "Since startup at asdf:", None))
        self.labelMessageCount.setText(_translate("MainWindow", "Processed 0 person-to-person message.", None))
        self.labelPubkeyCount.setText(_translate("MainWindow", "Processed 0 public key.", None))
        self.labelBroadcastCount.setText(_translate("MainWindow", "Processed 0 broadcast.", None))
        self.labelLookupsPerSecond.setText(_translate("MainWindow", "Inventory lookups per second: 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networkstatus), _translate("MainWindow", "Network Status", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Advenced_messaging), _translate("MainWindow", "Advanced messaging", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionImport_keys.setText(_translate("MainWindow", "Import keys", None))
        self.actionManageKeys.setText(_translate("MainWindow", "Manage keys", None))
        self.actionExit.setText(_translate("MainWindow", "Quit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionRegenerateDeterministicAddresses.setText(_translate("MainWindow", "Regenerate deterministic addresses", None))
        self.actionDeleteAllTrashedMessages.setText(_translate("MainWindow", "Delete all trashed messages", None))
        self.actionJoinChan.setText(_translate("MainWindow", "Join / Create chan", None))

import bitmessage_icons_rc
