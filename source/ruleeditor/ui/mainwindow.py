# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ifontarensky/Workspace/yara/RuleEditor/source_core/ruleeditor/ui/mainwindow.ui'
#
# Created: Sun May  3 17:41:19 2015
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
        MainWindow.resize(1224, 629)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dockBrowser = QtGui.QDockWidget(self.centralwidget)
        self.dockBrowser.setMaximumSize(QtCore.QSize(400, 524287))
        self.dockBrowser.setObjectName(_fromUtf8("dockBrowser"))
        self.widgetBrowser = QtGui.QWidget()
        self.widgetBrowser.setObjectName(_fromUtf8("widgetBrowser"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetBrowser)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.browser = QtGui.QTreeView(self.widgetBrowser)
        self.browser.setMinimumSize(QtCore.QSize(400, 0))
        self.browser.setMaximumSize(QtCore.QSize(400, 16777215))
        self.browser.setObjectName(_fromUtf8("browser"))
        self.verticalLayout_3.addWidget(self.browser)
        self.dockBrowser.setWidget(self.widgetBrowser)
        self.horizontalLayout.addWidget(self.dockBrowser)
        self.tabContent = QtGui.QTabWidget(self.centralwidget)
        self.tabContent.setMinimumSize(QtCore.QSize(400, 0))
        self.tabContent.setTabsClosable(True)
        self.tabContent.setObjectName(_fromUtf8("tabContent"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabContent.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabContent)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuDocuments = QtGui.QMenu(self.menubar)
        self.menuDocuments.setObjectName(_fromUtf8("menuDocuments"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_QT = QtGui.QAction(MainWindow)
        self.actionAbout_QT.setObjectName(_fromUtf8("actionAbout_QT"))
        self.actionSave_All = QtGui.QAction(MainWindow)
        self.actionSave_All.setObjectName(_fromUtf8("actionSave_All"))
        self.actionClose_All = QtGui.QAction(MainWindow)
        self.actionClose_All.setObjectName(_fromUtf8("actionClose_All"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_QT)
        self.menuDocuments.addAction(self.actionSave_All)
        self.menuDocuments.addAction(self.actionClose_All)
        self.menuDocuments.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDocuments.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabContent.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RuleEditor", None))
        self.tabContent.setTabText(self.tabContent.indexOf(self.tab), _translate("MainWindow", "Untitled *", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "?", None))
        self.menuDocuments.setTitle(_translate("MainWindow", "Documents", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSaveAs.setText(_translate("MainWindow", "Save as ...", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout_QT.setText(_translate("MainWindow", "About &QT", None))
        self.actionSave_All.setText(_translate("MainWindow", "Save All", None))
        self.actionClose_All.setText(_translate("MainWindow", "Close All", None))

