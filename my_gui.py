# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_gui.ui'
#
# Created: Fri Jul  3 09:15:45 2015
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(775, 581)
        MainWindow.setMinimumSize(QtCore.QSize(616, 474))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_previous = QtGui.QToolButton(self.centralwidget)
        self.toolButton_previous.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_previous.setIcon(icon1)
        self.toolButton_previous.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_previous.setObjectName(_fromUtf8("toolButton_previous"))
        self.horizontalLayout.addWidget(self.toolButton_previous)
        self.toolButton_next = QtGui.QToolButton(self.centralwidget)
        self.toolButton_next.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_next.setIcon(icon2)
        self.toolButton_next.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_next.setObjectName(_fromUtf8("toolButton_next"))
        self.horizontalLayout.addWidget(self.toolButton_next)
        self.toolButton_stop = QtGui.QToolButton(self.centralwidget)
        self.toolButton_stop.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_stop.setIcon(icon3)
        self.toolButton_stop.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_stop.setObjectName(_fromUtf8("toolButton_stop"))
        self.horizontalLayout.addWidget(self.toolButton_stop)
        self.toolButton_home = QtGui.QToolButton(self.centralwidget)
        self.toolButton_home.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_home.setIcon(icon4)
        self.toolButton_home.setIconSize(QtCore.QSize(34, 32))
        self.toolButton_home.setObjectName(_fromUtf8("toolButton_home"))
        self.horizontalLayout.addWidget(self.toolButton_home)
        self.toolButton_refresh = QtGui.QToolButton(self.centralwidget)
        self.toolButton_refresh.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_refresh.setIcon(icon5)
        self.toolButton_refresh.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_refresh.setObjectName(_fromUtf8("toolButton_refresh"))
        self.horizontalLayout.addWidget(self.toolButton_refresh)
        self.lineEdit_url = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(9)
        self.lineEdit_url.setFont(font)
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.toolButton_go = QtGui.QToolButton(self.centralwidget)
        self.toolButton_go.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_go.setIcon(icon6)
        self.toolButton_go.setIconSize(QtCore.QSize(28, 20))
        self.toolButton_go.setObjectName(_fromUtf8("toolButton_go"))
        self.horizontalLayout.addWidget(self.toolButton_go)
        self.toolButton_zoom_in = QtGui.QToolButton(self.centralwidget)
        self.toolButton_zoom_in.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_zoom_in.setIcon(icon7)
        self.toolButton_zoom_in.setIconSize(QtCore.QSize(30, 25))
        self.toolButton_zoom_in.setObjectName(_fromUtf8("toolButton_zoom_in"))
        self.horizontalLayout.addWidget(self.toolButton_zoom_in)
        self.toolButton_zoom_out = QtGui.QToolButton(self.centralwidget)
        self.toolButton_zoom_out.setStyleSheet(_fromUtf8("QToolButton{\n"
"border:none;\n"
"background-color:transparent;\n"
"\n"
"}"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_zoom_out.setIcon(icon8)
        self.toolButton_zoom_out.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_zoom_out.setObjectName(_fromUtf8("toolButton_zoom_out"))
        self.horizontalLayout.addWidget(self.toolButton_zoom_out)
        self.label_current_zoom = QtGui.QLabel(self.centralwidget)
        self.label_current_zoom.setObjectName(_fromUtf8("label_current_zoom"))
        self.horizontalLayout.addWidget(self.label_current_zoom)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar{\n"
"border:none;\n"
"background:transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                      stop: 0 #219DA3, stop: 1 #2FE4ED);\n"
"}"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.webView = QtWebKit.QWebView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://www.google.com.pk/?gws_rd=cr&ei=wXqKVfyLMuKE7gaSv4HoDA")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PySurf", None))
        self.toolButton_previous.setToolTip(_translate("MainWindow", "Go back one page", None))
        self.toolButton_previous.setText(_translate("MainWindow", "Previous", None))
        self.toolButton_next.setToolTip(_translate("MainWindow", "Go forward one page", None))
        self.toolButton_next.setText(_translate("MainWindow", "Next", None))
        self.toolButton_stop.setToolTip(_translate("MainWindow", "Stop loading this page", None))
        self.toolButton_stop.setText(_translate("MainWindow", "...", None))
        self.toolButton_home.setToolTip(_translate("MainWindow", "Go to home page", None))
        self.toolButton_home.setText(_translate("MainWindow", "Home", None))
        self.toolButton_refresh.setToolTip(_translate("MainWindow", "Refresh", None))
        self.toolButton_refresh.setText(_translate("MainWindow", "Home", None))
        self.toolButton_go.setToolTip(_translate("MainWindow", "Go", None))
        self.toolButton_go.setText(_translate("MainWindow", "GO", None))
        self.toolButton_zoom_in.setToolTip(_translate("MainWindow", "Zoom in", None))
        self.toolButton_zoom_in.setText(_translate("MainWindow", "...", None))
        self.toolButton_zoom_out.setToolTip(_translate("MainWindow", "Zoom out", None))
        self.toolButton_zoom_out.setText(_translate("MainWindow", "...", None))
        self.label_current_zoom.setToolTip(_translate("MainWindow", "Current zoom", None))
        self.label_current_zoom.setText(_translate("MainWindow", "100%", None))
        self.progressBar.setToolTip(_translate("MainWindow", "Page load progress", None))

from PyQt4 import QtWebKit
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

