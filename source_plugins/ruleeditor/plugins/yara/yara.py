# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'
__version__ = '0.9'
plugin_class = 'Editor'
plugin_name = 'YaraEditor'

import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)

from ruleeditor.plugins.yara.yaraeditor import YaraEditor
from ruleeditor.plugins.yara.highlighter import YaraHighlighter

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Editor(object):

    def __init__(self):
        pass


    def setupPlugin(self, tabContent):
        self.tabContent = tabContent

    def allowFormat(self):
        """
        All format supported

        :return: List of Supported format
        """
        return [".yara", ".yar"]

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
        self.tabContent.addTab(self.tab, _fromUtf8(path))
        self.tab.setObjectName(_fromUtf8(path))
        self.yaraEdit.setPlainText(unistr)


        return True


    def newFile(self):
        """
        New File
        :return:
        """
        self.setupUi()


    def setupUi(self):
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("Untitled"))
        self.tabContent.addTab(self.tab, _fromUtf8("Untitled"))

        self.widgetEditor = self.tab
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetEditor)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.yaraEdit = YaraEditor(self.widgetEditor)
        self.yaraEdit.setObjectName(_fromUtf8("yaraEdit"))
        self.horizontalLayout.addWidget(self.yaraEdit)
        self.widgetEditor.setAcceptDrops(True)

        allStrings = ["all","and","any","ascii","at",
                      "condition","contains","entrypoint","false",
                      "filesize","fullword","for","global",
                      "in","include","index","indexes","int8",
                      "int16","int32","matches","meta","nocase",
                      "not","or","of","private","rule","rva",
                      "section","strings","them","true","uint8",
                      "uint16","uint32","wide"]

        completer = QtGui.QCompleter(allStrings)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setWrapAround(False)
        self.yaraEdit.setCompleter(completer)

        #Create our YaraHighlighter derived from QSyntaxHighlighter
        self.yaraEdit = self.yaraEdit
        self.highlighter = YaraHighlighter(self.yaraEdit.document())


        return
        self.yaraEdit.document().modificationChanged.connect(
                self.actionSave.setEnabled)
        self.yaraEdit.document().modificationChanged.connect(
                self.mainwindow.setWindowModified)
        self.yaraEdit.document().undoAvailable.connect(
                self.actionUndo.setEnabled)
        self.yaraEdit.document().redoAvailable.connect(
                self.actionRedo.setEnabled)
        self.mainwindow.setWindowModified(self.yaraEdit.document().isModified())
        self.actionSave.setEnabled(self.yaraEdit.document().isModified())
        self.actionUndo.setEnabled(self.yaraEdit.document().isUndoAvailable())
        self.actionRedo.setEnabled(self.yaraEdit.document().isRedoAvailable())
        self.actionUndo.triggered.connect(self.yaraEdit.undo)
        self.actionRedo.triggered.connect(self.yaraEdit.redo)
        self.actionCut.setEnabled(False)
        self.actionCopy.setEnabled(False)
        self.actionCut.triggered.connect(self.yaraEdit.cut)
        self.actionCopy.triggered.connect(self.yaraEdit.copy)
        self.actionPaste.triggered.connect(self.yaraEdit.paste)
        self.yaraEdit.copyAvailable.connect(self.actionCut.setEnabled)
        self.yaraEdit.copyAvailable.connect(self.actionCopy.setEnabled)
        QtGui.QApplication.clipboard().dataChanged.connect(
                self.clipboardDataChanged)


