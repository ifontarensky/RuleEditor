#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""


__docformat__ = 'restructuredtext'
__author__ = 'ifontarensky'

from PyQt4 import QtCore
from PyQt4 import QtGui

from ruleeditor.ui.dialogSettings import Ui_DialogSettings as Ui_DialogSettings

from ruleeditor.core.stylesheet import stylesheet_darkorange
from ruleeditor.core.stylesheet import stylesheet_darkstyle
from ruleeditor.core.stylesheet import stylesheet_xmas
from ruleeditor.core.stylesheet import stylesheet_oxygen
from ruleeditor.core.stylesheet import stylesheet_metal



class Settings():

    def __init__(self, app):
        self.app = app
        self.ui=Ui_DialogSettings()
        self.dialog=QtGui.QDialog()
        self.ui.setupUi(self.dialog)

        self.defaultStyleSheet = self.app.styleSheet()
        self.ui.rbSchemeDefault.clicked.connect(self.clickRadioButton)
        self.ui.rbSchemeDarkOrange.clicked.connect(self.clickRadioButton)
        self.ui.rbSchemeDarkStyle.clicked.connect(self.clickRadioButton)
        self.ui.rbSchemeMetal.clicked.connect(self.clickRadioButton)
        self.ui.rbSchemeXMas.clicked.connect(self.clickRadioButton)
        self.ui.rbSchemeOxygen.clicked.connect(self.clickRadioButton)


    def set_plugins(self, plugins_mgr):
        self.plugins_mgr = plugins_mgr
        for plugin, instance in self.plugins_mgr.loaded_plugins.iteritems():
            name = plugin.split("#@#")[1]
            item = QtGui.QTreeWidgetItem(self.ui.treePlugin)
            item.setText(0, name)
            item.setText(1, 'v%s' % instance.version)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled )
            item.setCheckState(0, QtCore.Qt.Checked)
        self.ui.treePlugin.resizeColumnToContents(0)


    def clickRadioButton(self, value):

        self.app.setStyleSheet("")

        if self.ui.rbSchemeDarkOrange.isChecked():
            self.app.setStyleSheet(stylesheet_darkorange)

        if self.ui.rbSchemeDarkStyle.isChecked():
            self.app.setStyleSheet(stylesheet_darkstyle)

        if self.ui.rbSchemeMetal.isChecked():
            self.app.setStyleSheet(stylesheet_metal)

        if self.ui.rbSchemeXMas.isChecked():
            self.app.setStyleSheet(stylesheet_xmas)

        if self.ui.rbSchemeOxygen.isChecked():
            self.app.setStyleSheet(stylesheet_oxygen)
        #


    def exec_(self):

        self.dialog.exec_()
