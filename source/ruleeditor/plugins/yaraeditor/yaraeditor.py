# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'
__version__ = '0.9'
plugin_class = 'Editor'
plugin_name = 'YaraEditor'

import os
try:
    import yara as yaraModule
    yara_lib_found = True
except Exception as error:
    print "Probleme when loading Yara library", error
    yara_lib_found = False


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)

from ruleeditor.plugins.codeeditor.codeeditor import CodeEditor as YaraCodeEditor
from ruleeditor.plugins.yaraeditor.highlighter import YaraHighlighter
from ruleeditor.plugins.yaraeditor.panelOptions import Ui_PanelOption
from ruleeditor.plugins.yaraeditor.icons import YARA_XPM
from PyQt4.QtCore import QThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Worker(QObject):


    def check_yara(self, path, rules):
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for i in files:
                    n = os.path.join(root, i)
                    try:
                        matches = rules.match(n)
                        if len(matches):
                            self.emit(SIGNAL("notify"), matches, n)
                    except UnicodeEncodeError, err:
                        print "! Error", n, err
        self.emit(SIGNAL("finish"))



class PluginYARAInstance():
    def open(self):
        path = QtGui.QFileDialog.getExistingDirectory(self.wPanel, "Load Malware...","")
        if path:
            self.uiPanel.editPathMalware.setText(path)


    def textChanged(self, text):
        if QDir(text).exists():
            self.uiPanel.btnTest.setEnabled(True)
        else:
            self.uiPanel.btnTest.setEnabled(False)

    def analyze(self):

        if self.uiPanel.btnTest.text() == "Test":
            source = self.yaraEdit.toPlainText()
            rules = yaraModule.compile(source=source)
            path = self.uiPanel.editPathMalware.text()

            self.uiPanel.editResult.document().clear()
            self.uiPanel.editResult.setVisible(True)

            self.worker.moveToThread(self.thread)


            QObject.connect(self.wPanel, SIGNAL("check_yara"), self.worker.check_yara)
            QObject.connect(self.worker, SIGNAL("notify"), self.notify_result)
            QObject.connect(self.worker, SIGNAL("finish"), self.finish)

            self.thread.start()
            self.wPanel.emit(SIGNAL("check_yara"), path, rules)

            self.uiPanel.btnTest.setText("Stop")
        else:
            self.wPanel.emit(SIGNAL("stop_analyse"))
            self.thread.terminate()
            self.uiPanel.btnTest.setText("Test")
            self.uiPanel.editResult.document().clear()

    def showhide(self):
        if self.uiPanel.editResult.isVisible():
            self.uiPanel.editResult.setVisible(False)
        else:
            self.uiPanel.editResult.setVisible(True)

    def notify_result(self, rules, path):
        self.cursor = self.uiPanel.editResult.textCursor()
        self.cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
        self.uiPanel.editResult.setTextCursor(self.cursor)
        for rule in rules:
            self.uiPanel.editResult.insertPlainText("{0} | {1}\n".format(rule, path))


    def finish(self):
        self.uiPanel.btnTest.setText("Test")




class Editor(object):


    def __init__(self):
        self.thread = QThread()
        self.worker = Worker()
        self.icon = QtGui.QIcon(QtGui.QPixmap(YARA_XPM))
        self.openedfile=dict()
        self.version = __version__
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


        self.add_instance(path)
        inst = self.get_instance(path)
        self.setupUi(inst)
        position = self.tabContent.addTab(inst.tab, _fromUtf8(path))
        inst.tab.setObjectName(_fromUtf8(path))
        inst.yaraEdit.setPlainText(unistr)
        self.tabContent.setCurrentIndex(position)
        self.tabContent.setTabIcon(position, self.icon)

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
        self.tabContent.setTabIcon(position, QtGui.QIcon(QtGui.QPixmap(YARA_XPM)))


    def get_document(self, path):
        return self.get_instance(path).yaraEdit.document()

    def get_instance(self,path):
        return self.openedfile[path]

    def add_instance(self, path):
        self.openedfile[path] = PluginYARAInstance()

    def get_icon(self):
        return self.icon


    def fileSave(self, path, document):

        with open(path, 'w') as handle:
            handle.write(str(document.toPlainText()))

        document.setModified(False)

        return True

    def fileSaveAs(self, document):
        fn = QtGui.QFileDialog.getSaveFileName(self.tabContent, "Save as...", None,
                "Yara files (*.yara);;HTML-Files (*.htm *.html);;All Files (*)")

        if not fn:
            return False

        lfn = fn.lower()
        if not lfn.endswith(('.yara', '.htm', '.html')):
            # The default.
            fn += '.yara'

        if self.fileSave(fn, document):
            return fn
        else:
            return None




    def setupUi(self, inst):
        inst.tab = QtGui.QWidget()
        inst.tab.setObjectName(_fromUtf8("Untitled"))
        index = self.tabContent.addTab(inst.tab, _fromUtf8("Untitled"))
        self.tabContent.setCurrentIndex(index)
        self.tabContent.setTabIcon(index, QtGui.QIcon(QtGui.QPixmap(YARA_XPM)))
        inst.widgetEditor = inst.tab
        inst.globalLayout = QtGui.QVBoxLayout(inst.widgetEditor)
        inst.globalLayout.setMargin(0)
        inst.globalLayout.setObjectName(_fromUtf8("globalLayout"))
        inst.yaraEdit = YaraCodeEditor(inst.widgetEditor)
        inst.yaraEdit.setObjectName(_fromUtf8("yaraEdit"))
        inst.globalLayout.addWidget(inst.yaraEdit)
        inst.widgetEditor.setAcceptDrops(True)

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
        inst.yaraEdit.setCompleter(completer)

        #Create our YaraHighlighter derived from QSyntaxHighlighter
        inst.yaraEdit = inst.yaraEdit
        inst.highlighter = YaraHighlighter(inst.yaraEdit.document())


        inst.wPanel=QtGui.QWidget()
        inst.uiPanel=Ui_PanelOption()

        if yara_lib_found:
            inst.uiPanel.setupUi(inst.wPanel)

            inst.uiPanel.btnBrowse.clicked.connect(inst.open)
            inst.uiPanel.btnTest.clicked.connect(inst.analyze)
            inst.uiPanel.btnHide.clicked.connect(inst.showhide)
            inst.uiPanel.editPathMalware.textChanged.connect(inst.textChanged)

            inst.globalLayout.addWidget(inst.wPanel)
        else:
            inst.wPanel.setVisible(False)


