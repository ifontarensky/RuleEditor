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


import os

from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

class PluginInstance():
    pass

class REPlugin(object):

    def __init__(self):
        self.openedfile=dict()
        self.version = __version__


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

        return []

    def isSupported(self, path):
        """
        Return if the path can be support by this Editor

        :param path:
        :return: Boolean
        """
        return os.path.splitext(path)[1] in self.allowFormat()


    def get_instance(self,path):
        """
        Get all data for on file
        :param path:
        :return:
        """
        return self.openedfile[path]

    def add_instance(self, path):
        """
        Create an instance for one file
        :param path:
        :return:
        """
        self.openedfile[path] = PluginInstance()

    def loadFile(self,path):
        """

        :param path:
        :return: Boolean
        """
        return True


    def newFile(self, path):
        """
        New File
        :return:
        """
        return True


    def get_document(self, path):
        return None

    def get_icon(self):
        return None

    def fileSave(self, path, document):
        return None

    def fileSaveAs(self, document):
        fn = QtGui.QFileDialog.getSaveFileName(self.tabContent, "Save as...", None,
                "All Files (*)")

        if not fn:
            return False

        if self.fileSave(fn, document):
            return fn
        else:
            return None

    def setupUi(self, inst):
        """

        :param inst:
        :return:
        """
        return

