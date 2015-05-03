# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'
__version__ = '1.0'
plugin_class = 'Editor'
plugin_name = 'IOCEditor'

import os


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)

from ruleeditor.plugins.ioceditor.ioctreewidget import IOCTreeWidget
from ruleeditor.plugins.ioceditor.highlighter import IOCHighlighter
from ruleeditor.plugins.codeeditor.codeeditor import CodeEditor
from ruleeditor.plugins.ioceditor.icons import IOC_XPM
from ruleeditor.core.REPlugin import REPlugin

from PyQt4.QtCore import QThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class PluginIOCInstance():

    def display_text_view(self):
        self.iocEditor.setVisible(True)
        self.iocWidget.setVisible(False)
        self.iocEditor.document().setPlainText(self.iocWidget.toPlainText())

    def display_tree_view(self):
        self.iocEditor.setVisible(False)
        self.iocWidget.setVisible(True)
        data=self.iocEditor.document().toPlainText()
        self.iocWidget.load_ioc(data)


class Editor(REPlugin):


    def __init__(self):
        self.icon = QtGui.QIcon(QtGui.QPixmap(IOC_XPM))
        self.openedfile=dict()
        self.version = __version__

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

    def get_instance(self,path):
        return self.openedfile[path]

    def add_instance(self, path):
        self.openedfile[path] = PluginIOCInstance()

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

        self.add_instance(path)
        inst = self.get_instance(path)
        self.setupUi(inst)
        position = self.tabContent.addTab(inst.tab, _fromUtf8(os.path.basename(path)))
        inst.tab.setObjectName(_fromUtf8(path))
        inst.iocEditor.setPlainText(unistr)
        self.tabContent.setCurrentIndex(position)
        self.tabContent.setTabIcon(position, self.icon)

        inst.iocWidget.load_ioc(unistr)
        inst.path = path
        return True


    def newFile(self, path):
        """
        New File
        :return:
        """
        self.add_instance(path)
        inst = self.get_instance(path)
        self.setupUi(inst)
        position = self.tabContent.addTab(inst.tab, _fromUtf8(path))
        inst.tab.setObjectName(_fromUtf8(path))
        self.tabContent.setCurrentIndex(position)
        ## Define COlor
        self.tabContent.tabBar().setTabTextColor(position, QtCore.Qt.red)


    def get_document(self, path):
        return self.get_instance(path).iocEditor.document()

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


    def setupUi(self, inst):
        inst.tab = QtGui.QWidget()
        inst.tab.setObjectName(_fromUtf8("Untitled IOC"))
        index = self.tabContent.addTab(inst.tab, _fromUtf8("Untitled IOC"))
        self.tabContent.setCurrentIndex(index)
        self.tabContent.setTabIcon(index, QtGui.QIcon(QtGui.QPixmap(IOC_XPM)))

        inst.widgetEditor = inst.tab
        inst.globalLayout = QtGui.QVBoxLayout(inst.widgetEditor)
        inst.globalLayout.setMargin(0)
        inst.globalLayout.setObjectName(_fromUtf8("globalLayout"))

        # Create Simple ToolBar for View mode
        inst.widgetViewMode = QtGui.QWidget(inst.widgetEditor)
        inst.widgetViewMode.setMaximumSize(QtCore.QSize(16777215, 32))
        inst.widgetViewMode.setObjectName(_fromUtf8("widgetViewMode"))
        inst.horizontalLayout_4 = QtGui.QHBoxLayout(inst.widgetViewMode)
        inst.horizontalLayout_4.setMargin(0)
        inst.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        inst.btnTreeView = QtGui.QPushButton(inst.widgetViewMode)
        inst.btnTreeView.setObjectName(_fromUtf8("btnTreeView"))
        inst.btnTreeView.setText("Tree")
        inst.horizontalLayout_4.addWidget(inst.btnTreeView)
        inst.btnTextView = QtGui.QPushButton(inst.widgetViewMode)
        inst.btnTextView.setObjectName(_fromUtf8("btnTextView"))
        inst.btnTextView.setText("Text")
        inst.horizontalLayout_4.addWidget(inst.btnTextView)
        spacerItem = QtGui.QSpacerItem(719, 11, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        inst.horizontalLayout_4.addItem(spacerItem)
        inst.globalLayout.addWidget(inst.widgetViewMode)

        inst.iocEditor = CodeEditor(inst.widgetEditor)
        inst.iocWidget = IOCTreeWidget(inst.widgetEditor)
        inst.iocWidget.setupUi()

        inst.globalLayout.addWidget(inst.iocWidget)
        inst.globalLayout.addWidget(inst.iocEditor)

        inst.iocEditor.setVisible(False)


        allStrings = inst.iocWidget.elements + inst.iocWidget.attrib

        completer = QtGui.QCompleter(allStrings)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setWrapAround(False)
        inst.iocEditor.setCompleter(completer)

        inst.highlighter = IOCHighlighter(inst.iocEditor.document())

        #Define Actions
        inst.btnTextView.clicked.connect(inst.display_text_view)
        inst.btnTreeView.clicked.connect(inst.display_tree_view)



