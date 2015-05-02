# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'
__version__ = '0.9'
plugin_class = 'Editor'
plugin_name = 'IOCEditor'

import os


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)

from ruleeditor.plugins.ioceditor.ioctreewidget import IOCTreeWidget
from ruleeditor.plugins.ioceditor.highlighter import IOCHighlighter
from ruleeditor.plugins.codeeditor.codeeditor import CodeEditor
from ruleeditor.plugins.ioceditor.icons import IOC_XPM

from PyQt4.QtCore import QThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Editor(object):


    def __init__(self):
        self.icon = QtGui.QIcon(QtGui.QPixmap(IOC_XPM))
        pass


    def setupPlugin(self, tabContent):
        """
        Setup variable

        :param tabContent:
        :return:
        """
        self.tabContent = tabContent


    def allowFormat(self):
        """
        All format supported

        :return: List of Supported format
        """
        return [".ioc"]


    def isSupported(self, path):
        """
        Return if the path can be support by this Editor

        :param path:
        :return: Boolean
        """
        return os.path.splitext(path)[1] in self.allowFormat()


    def loadFile(self,path):

        if not QtCore.QFile.exists(path):
            return False

        fh = QtCore.QFile(path)
        if not fh.open(QtCore.QFile.ReadOnly):
            return False

        data = fh.readAll()
        codec = QtCore.QTextCodec.codecForHtml(data)
        unistr = codec.toUnicode(data)

        if QtCore.Qt.mightBeRichText(unistr):

            doc = QtGui.QTextDocument()
            doc.setHtml(unistr)
            text = doc.toPlainText()

            unistr = text

        #self.setCurrentFileName(path)

        self.setupUi()
        position = self.tabContent.addTab(self.tab, _fromUtf8(os.path.basename(path)))
        self.tab.setObjectName(_fromUtf8(path))
        self.iocEditor.setPlainText(unistr)
        self.tabContent.setCurrentIndex(position)
        self.tabContent.setTabIcon(position, self.icon)

        self.iocWidget.load_ioc(unistr)
        self.path = path
        return True


    def newFile(self, path):
        """
        New File
        :return:
        """
        self.setupUi()
        position = self.tabContent.addTab(self.tab, _fromUtf8(path))
        self.tab.setObjectName(_fromUtf8(path))
        self.tabContent.setCurrentIndex(position)
        ## Define COlor
        self.tabContent.tabBar().setTabTextColor(position, QtCore.Qt.red)


    def get_document(self):
        return self.iocEditor.document()

    def get_icon(self):
        return self.icon

    def fileSave(self, path, document):

        with open(path, 'w') as handle:
            handle.write(str(document.toPlainText()))

        document.setModified(False)

        return True

    def fileSaveAs(self, document):
        fn = QtGui.QFileDialog.getSaveFileName(self.tabContent, "Save as...", None,
                "IOC files (*.ioc);;HTML-Files (*.htm *.html);;All Files (*)")

        if not fn:
            return False

        lfn = fn.lower()
        if not lfn.endswith(('.ioc', '.htm', '.html')):
            # The default.
            fn += '.ioc'

        if self.fileSave(fn, document):
            return fn
        else:
            return None


    def setupUi(self):
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("Untitled IOC"))
        index = self.tabContent.addTab(self.tab, _fromUtf8("Untitled IOC"))
        self.tabContent.setCurrentIndex(index)
        self.tabContent.setTabIcon(index, QtGui.QIcon(QtGui.QPixmap(IOC_XPM)))

        self.widgetEditor = self.tab
        self.globalLayout = QtGui.QVBoxLayout(self.widgetEditor)
        self.globalLayout.setMargin(0)
        self.globalLayout.setObjectName(_fromUtf8("globalLayout"))

        # Create Simple ToolBar for View mode
        self.widgetViewMode = QtGui.QWidget(self.widgetEditor)
        self.widgetViewMode.setMaximumSize(QtCore.QSize(16777215, 32))
        self.widgetViewMode.setObjectName(_fromUtf8("widgetViewMode"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widgetViewMode)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnTreeView = QtGui.QPushButton(self.widgetViewMode)
        self.btnTreeView.setObjectName(_fromUtf8("btnTreeView"))
        self.btnTreeView.setText("Tree")
        self.horizontalLayout_4.addWidget(self.btnTreeView)
        self.btnTextView = QtGui.QPushButton(self.widgetViewMode)
        self.btnTextView.setObjectName(_fromUtf8("btnTextView"))
        self.btnTextView.setText("Text")
        self.horizontalLayout_4.addWidget(self.btnTextView)
        spacerItem = QtGui.QSpacerItem(719, 11, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.globalLayout.addWidget(self.widgetViewMode)

        self.iocEditor = CodeEditor(self.widgetEditor)
        self.iocWidget = IOCTreeWidget(self.widgetEditor)
        self.iocWidget.setupUi()

        self.globalLayout.addWidget(self.iocWidget)
        self.globalLayout.addWidget(self.iocEditor)

        self.iocEditor.setVisible(False)


        allStrings = self.iocWidget.elements + self.iocWidget.attrib

        completer = QtGui.QCompleter(allStrings)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setWrapAround(False)
        self.iocEditor.setCompleter(completer)

        self.highlighter = IOCHighlighter(self.iocEditor.document())

        #Define Actions
        self.btnTextView.clicked.connect(self.display_text_view)
        self.btnTreeView.clicked.connect(self.display_tree_view)



    def display_text_view(self):
        self.iocEditor.setVisible(True)
        self.iocWidget.setVisible(False)

    def display_tree_view(self):
        self.iocEditor.setVisible(False)
        self.iocWidget.setVisible(True)