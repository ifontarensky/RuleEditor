# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'
__version__ = '0.9'
plugin_class = 'Editor'
plugin_name = 'SnortEditor'

import os


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)

from ruleeditor.plugins.codeeditor.codeeditor import CodeEditor as SnortCodeEditor
from ruleeditor.plugins.snorteditor.highlighter import SnortHighlighter
from ruleeditor.plugins.snorteditor.icons import SNORT_XPM
from ruleeditor.core.REPlugin import REPlugin

from PyQt4.QtCore import QThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



class Editor(REPlugin):


    def __init__(self):
        self.icon = QtGui.QIcon(QtGui.QPixmap(SNORT_XPM))
        self.openedfile=dict()


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
        return [".rules", ".snort"]


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
        inst.snortEdit.setPlainText(unistr)
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

    def get_document(self, path):
        """

        :return:
        """
        return self.get_instance(path).snortEdit.document()

    def get_instance(self,path):
        """
        Get all data for on file
        :param path:
        :return:
        """
        return self.openedfile[path]


    def get_icon(self):
        return self.icon

    def fileSave(self, path, document):

        with open(path, 'w') as handle:
            handle.write(str(document.toPlainText()))

        document.setModified(False)

        return True

    def fileSaveAs(self, document):
        fn = QtGui.QFileDialog.getSaveFileName(self.tabContent, "Save as...", None,
                "Snort files (*.rules *snort);;HTML-Files (*.htm *.html);;All Files (*)")

        if not fn:
            return False

        lfn = fn.lower()
        if not lfn.endswith(('.rules', '.snort', '.htm', '.html')):
            # The default.
            fn += '.rules'

        if self.fileSave(fn, document):
            return fn
        else:
            return None


    def setupUi(self, inst):
        inst.tab = QtGui.QWidget()
        inst.tab.setObjectName(_fromUtf8("Untitled Snort"))
        index = self.tabContent.addTab(inst.tab, _fromUtf8("Untitled Snort"))
        self.tabContent.setCurrentIndex(index)
        self.tabContent.setTabIcon(index, self.get_icon())
        inst.widgetEditor = inst.tab
        inst.globalLayout = QtGui.QVBoxLayout(inst.widgetEditor)
        inst.globalLayout.setMargin(0)
        inst.globalLayout.setObjectName(_fromUtf8("globalLayout"))
        inst.snortEdit = SnortCodeEditor(inst.widgetEditor)
        inst.snortEdit.setObjectName(_fromUtf8("snortEdit"))
        inst.globalLayout.addWidget(inst.snortEdit)
        inst.widgetEditor.setAcceptDrops(True)

        allStrings = ["msg", "reference", "gid", "sid", "rev", "classtype",
                      "priority", "metadata", "content", "nocase", "rawbytes",
                      "depth", "offset", "distance", "within",
                      "http_client_body", "http_cookie", "http_raw_cookie",
                      "http_header", "http_raw_header", "http_method",
                      "http_uri", "http_raw_uri", "http_stat_code",
                      "http_stat_msg", "fast_pattern", "uricontent", "urilen",
                      "isdataat", "pcre", "pkt_data", "file_data",
                      "base64_decode", "base64_data", "byte_test", "byte_jump",
                      "byte_extract", "ftpbounce", "asn1", "cvs", "dce_iface",
                      "dce_opnum", "dce_stub_data", "sip_method",
                      "sip_stat_code", "sip_header", "sip_body", "gtp_type",
                      "gtp_info", "gtp_version", "ssl_version", "ssl_state",
                      "fragoffset", "ttl", "tos", "id", "ipopts", "fragbits",
                      "dsize", "flags", "flow", "flowbits", "seq", "ack",
                      "window", "itype", "icode", "icmp_id", "icmp_seq", "rpc",
                      "ip_proto", "sameip", "stream_reassemble", "stream_size",
                      "logto", "session", "resp", "react", "tag", "activates",
                      "activated_by", "count", "replace", "detection_filter",
                      "threshold", "activate", "alert", "drop", "dynamic",
                      "log", "pass", "reject", "sdrop", "sblock"]

        completer = QtGui.QCompleter(allStrings)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setWrapAround(False)
        inst.snortEdit.setCompleter(completer)

        #Create our SnortHighlighter derived from QSyntaxHighlighter
        inst.highlighter = SnortHighlighter(inst.snortEdit.document())



