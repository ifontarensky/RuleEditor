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

from PyQt4.QtCore import QThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



class Editor(object):


    def __init__(self):
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

        #self.setCurrentFileName(path)

        self.setupUi()
        position = self.tabContent.addTab(self.tab, _fromUtf8(path))
        self.tab.setObjectName(_fromUtf8(path))
        self.snortEdit.setPlainText(unistr)
        self.tabContent.setCurrentIndex(position)

        return True


    def newFile(self):
        """
        New File
        :return:
        """
        self.setupUi()


    def setupUi(self):
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("Untitled Snort"))
        index = self.tabContent.addTab(self.tab, _fromUtf8("Untitled Snort"))
        self.tabContent.setCurrentIndex(index)
        self.widgetEditor = self.tab
        self.globalLayout = QtGui.QVBoxLayout(self.widgetEditor)
        self.globalLayout.setMargin(0)
        self.globalLayout.setObjectName(_fromUtf8("globalLayout"))
        self.snortEdit = SnortCodeEditor(self.widgetEditor)
        self.snortEdit.setObjectName(_fromUtf8("snortEdit"))
        self.globalLayout.addWidget(self.snortEdit)
        self.widgetEditor.setAcceptDrops(True)

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
        self.snortEdit.setCompleter(completer)

        #Create our SnortHighlighter derived from QSyntaxHighlighter
        self.snortEdit = self.snortEdit
        self.highlighter = SnortHighlighter(self.snortEdit.document())



