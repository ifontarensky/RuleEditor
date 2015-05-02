#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""

__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'
__version__ = '1.0'
plugin_class = 'Editor'

import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)

from ruleeditor.plugins.codeeditor.codeeditor import CodeEditor
from ruleeditor.core.REPlugin import REPlugin


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str


class Editor(REPlugin):


    def setupPlugin(self, tabContent):
        """
        Setup environnement.

        :param tabContent:
        :return:
        """
        self.tabContent = tabContent

    def allowFormat(self):
        """
        All format supported

        :return: List of Supported format
        """

        return [".log", ".txt"]


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
        self.add_instance(path)
        inst = self.get_instance(path)
        self.setupUi(inst)
        self.tabContent.addTab(inst.tab, _fromUtf8(path))
        inst.tab.setObjectName(_fromUtf8(path))
        inst.codeEdit.setPlainText(unistr)


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


    def get_document(self, path):
        inst = self.get_instance(path)
        return inst.codeEdit.document()


    def fileSave(self, path, document):

        with open(path, 'w') as handle:
            handle.write(str(document.toPlainText()))

        document.setModified(False)

        return True


    def setupUi(self, inst):
        inst.tab = QtGui.QWidget()
        inst.tab.setObjectName(_fromUtf8("Untitled"))
        index = self.tabContent.addTab(inst.tab, _fromUtf8("Untitled"))
        inst.widgetEditor = inst.tab
        inst.horizontalLayout = QtGui.QHBoxLayout(inst.widgetEditor)
        inst.horizontalLayout.setMargin(0)
        inst.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        inst.codeEdit = CodeEditor(inst.widgetEditor)
        inst.codeEdit.setObjectName(_fromUtf8("codeEdit"))
        inst.horizontalLayout.addWidget(inst.codeEdit)
        inst.widgetEditor.setAcceptDrops(True)

        completer = QtGui.QCompleter([])
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setWrapAround(False)
        inst.codeEdit.setCompleter(completer)

        return

