#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""


__docformat__ = 'restructuredtext'
__author__ = 'ifontarensky'


"""
This module is the core of the application: it
controls the managers for specific tasks and contains the logic for reacting
to user's input i.e. the slots connected to every menu entry are defined here.
"""

from PyQt4 import QtCore
from PyQt4 import QtGui

import os

import ruleeditor.core.pluginsLoader as pluginsLoader

import ruleeditor.ui as reGUI

from ruleeditor.ui.dialogNewFile import Ui_Dialog as Ui_DialogNew

translate = QtGui.QApplication.translate

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class REApp(QtCore.QObject):

    """
    The application core.

    :Parameters:

    """


    def __init__(self):
        """
        Initialize the application.

        This method starts the application: makes the GUI, configure the
        app, instantiates managers needed to control the app. and connect
        signals to slots.
        """

        super(REApp, self).__init__()

        # Make the main window easily accessible for external modules
        self.setObjectName('REApp')

        # Create the GUI. This is done in 3 steps:
        # - create the main window
        # - create the model/view for the tree of databases
        # - setup the main window


        # création de la fenêtre principale
        self.gui=QtGui.QMainWindow()
        self.ui=reGUI.mainwindow.Ui_MainWindow()


        self.actions = {
            "browser" : {}
            }

        # Load plugins.
        # Some plugins modify existing menus so plugins must be loaded after
        # creating the user interface.
        # Some plugins modify datasets displaying so plugins must be loaded
        # before opening any file.
        self.plugins_mgr = \
            pluginsLoader.PluginsLoader([], [])
        self.plugins_mgr.loadAll()

        # Map Tree to know wich file are opened,
        self.mapdocuments = dict()

        # affichage de la fenêtre principal
        self.ui.setupUi(self.gui)
        self.setupActions()
        self.setupBrowser()
        self.setupBrowserContextMenu()
        self.setupPlugins()

        self.ui.tabContent.removeTab(0)


    def setupActions(self):
        self.actions["menu"] = {
            "new" : self.ui.actionNew,
            "open" : self.ui.actionOpen,
            "save" : self.ui.actionSave,
            "saveas" : self.ui.actionSaveAs,
            "settings" : self.ui.actionSettings
        }

        QtCore.QObject.connect(
            self.actions["menu"]["new"],
            QtCore.SIGNAL(_fromUtf8("triggered()")),
            self.fileNew)
        QtCore.QObject.connect(
            self.actions["menu"]["open"],
            QtCore.SIGNAL(_fromUtf8("triggered()")),
            self.fileOpen)
        QtCore.QObject.connect(
            self.actions["menu"]["save"],
            QtCore.SIGNAL(_fromUtf8("triggered()")),
            self.fileSave)
        QtCore.QObject.connect(
            self.actions["menu"]["saveas"],
            QtCore.SIGNAL(_fromUtf8("triggered()")),
            self.fileSaveAs)
        QtCore.QObject.connect(
            self.actions["menu"]["settings"],
            QtCore.SIGNAL(_fromUtf8("triggered()")),
            self.browserrefresh)

        self.ui.tabContent.tabCloseRequested.connect(self.close_handler)

    def close_handler(self, index):
        """
        Close Tab Edition
        :param index:
        :return:
        """

        indexToClose = self.ui.tabContent.currentIndex()

        plugin, document, path, ondisk = self.get_object_from_index(indexToClose)
        modified = document.isModified()

        if not ondisk or modified:
            ret = QtGui.QMessageBox.warning(self.gui, "Application",
                    "The document has been modified.\n"
                    "Do you want to save your changes?",
                    QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
                            QtGui.QMessageBox.Cancel)

            if ret == QtGui.QMessageBox.Cancel:
                return False

            if ret == QtGui.QMessageBox.Save:
                self.fileSaveWithInstance(plugin, document, path)

            if ret == QtGui.QMessageBox.Discard:
                pass

        self.ui.tabContent.removeTab(index)


    def setupBrowser(self):
        self.modelFileSystem = QtGui.QDirModel()
        self.ui.browser.setModel(self.modelFileSystem)
        self.ui.browser.setAnimated(False)
        self.ui.browser.setIndentation(20)
        self.ui.browser.setSortingEnabled(True)
        self.ui.browser.setColumnHidden(1,True)
        self.ui.browser.setColumnHidden(2,True)
        self.ui.browser.setColumnHidden(3,True)
        QtCore.QObject.connect(
            self.ui.browser,
            QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")),
            self.browserdoubleClicked)

        self.ui.browser.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        QtCore.QObject.connect(
            self.ui.browser,
            QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(const QPoint&)")),
            self.browserrightClicked)


    def setupBrowserContextMenu(self):

        self.actions["browser"] = {
            "new" : QtGui.QAction('New', self.gui),
            "refresh" : QtGui.QAction('Refresh', self.gui),
            "openwith": {}

        }


        # create context menu
        self.popMenu = QtGui.QMenu(self.gui)
        self.popMenu.addAction(self.actions["browser"]["new"])
        subMenuOpen = self.popMenu.addMenu("Open with ...")
        self.popMenu.addSeparator()
        self.popMenu.addAction(self.actions["browser"]["refresh"])
        QtCore.QObject.connect(
            self.actions["browser"]["refresh"],
            QtCore.SIGNAL(_fromUtf8("triggered()")),
            self.browserrefresh)

        for plugin, instance in self.plugins_mgr.loaded_plugins.iteritems():
            name = plugin.split("#@#")[1]
            self.actions["browser"]["openwith"][name] = QtGui.QAction(name, self.gui)
            subMenuOpen.addAction(self.actions["browser"]["openwith"][name])
            QtCore.QObject.connect(
                self.actions["browser"]["openwith"][name],
                QtCore.SIGNAL(_fromUtf8("triggered()")),
                self.fileOpenWith)



    def browserdoubleClicked(self, index):
        """

        Event doubleCLicked from Browser

        :param index:
        :return:
        """
        path = self.modelFileSystem.filePath(index)

        self.loadFile(path)


    def browserrightClicked(self, point):
        # show context menu
        self.popMenu.exec_(self.ui.browser.mapToGlobal(point))


    def browserrefresh(self):
        """
        Browser Refresh

        :return:
        """
        rootIndex = self.ui.browser.rootIndex()
        self.ui.browser.setRootIndex(rootIndex)
        self.modelFileSystem.refresh(rootIndex)

    def fileNew(self):
        """

        :return:
        """
        # création de la fenêtre principale
        newDialog=QtGui.QDialog()

        ui=Ui_DialogNew()
        ui.setupUi(newDialog)
        ui.listPlugin.setRowCount(len(self.plugins_mgr.loaded_plugins))
        plugins= dict()
        nRow =0
        for plugin, instance in self.plugins_mgr.loaded_plugins.iteritems():
            name = plugin.split("#@#")[1]

            item = QtGui.QTableWidgetItem()

            ui.listPlugin.setVerticalHeaderItem(nRow, item)

            itemName = QtGui.QTableWidgetItem()
            itemName.setText(name)
            itemExt = QtGui.QTableWidgetItem()
            itemExt.setText(";".join(instance.allowFormat()))
            itemIcon = QtGui.QTableWidgetItem()
            itemIcon.setData(QtCore.Qt.DecorationRole,instance.get_icon())

            itemName.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            itemExt.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            itemIcon.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)

            ui.listPlugin.setItem(nRow, 0, itemIcon)
            ui.listPlugin.setItem(nRow, 1, itemName)
            ui.listPlugin.setItem(nRow, 2, itemExt)


            plugins[name] = instance

            nRow += 1

        if newDialog.exec_() != 0 and len(ui.listPlugin.selectedItems()) > 0:
            plugin_name = ui.listPlugin.selectedItems()[1].text()
            self.newFileWith(plugins[plugin_name])


    def fileOpen(self):
        """
        Open File
        :return:
        """
        fn = QtGui.QFileDialog.getOpenFileName(self.gui, "Open File...", "",
                "All Files (*)")

        if fn:
            self.loadFile(fn)


    def fileOpenWith(self):
        pluginname = self.gui.sender().text()
        list = self.ui.browser.selectionModel().selectedIndexes()
        abspath = set()
        for index in list:
            fi =self.modelFileSystem.fileInfo(index)
            abspath.add(fi.absoluteFilePath())

        for path in abspath:
            for plugin, instance in self.plugins_mgr.loaded_plugins.iteritems():
                if plugin.split("#@#")[1] == pluginname:
                    self.loadFileWith(path, instance)



    def loadFile(self, path):
        if not QtCore.QFile.exists(path):
            return False

        for plugin, instance in self.plugins_mgr.loaded_plugins.iteritems():
            name = plugin.split("#@#")[1]
            if instance.isSupported(path):
                self.loadFileWith(path, instance)

    def newFileWith(self, plugin):
        path = "Untitled %d" % len(self.mapdocuments)
        plugin.newFile(path)
        self.mapdocuments[path] = {
                "tab" : plugin.get_instance(path).tab,
                "document" : plugin.get_document(path),
                "plugin" : plugin,
                "ondisk" : False
        }

    def loadFileWith(self, path, plugin):

        if path in self.mapdocuments.keys():
            index = self.ui.tabContent.indexOf(self.mapdocuments[path]["tab"])
            self.ui.tabContent.setPosition(index)

        else:
            plugin.loadFile(path)
            self.mapdocuments[path] = {
                "tab" : plugin.get_instance(path).tab,
                "document" : plugin.get_document(path),
                "plugin" : plugin,
                "ondisk" : True
            }

    def setupPlugins(self):

        for plugin, instance in self.plugins_mgr.loaded_plugins.iteritems():
            name = plugin.split("#@#")[1]
            instance.setupPlugin(self.ui.tabContent)


    def get_object_from_index(self, index):
        found = False
        modified = False
        path = None
        document = None
        plugin = None
        ondisk = None
        for key, value in self.mapdocuments.iteritems():
            if index == self.ui.tabContent.indexOf(value["tab"]):
                path = key
                document = value["document"]
                plugin = value["plugin"]
                ondisk = value["ondisk"]

        for objet in [path, document, plugin, ondisk]:
            if objet == None:
                ret = QtGui.QMessageBox.critical(self.gui, "Application",
                        "Problem occured whan trying to save the document.\n"
                        "Copy and Paste your work on other editor.")
                return None, None, None, None

        return plugin, document, path, ondisk


    def fileSave(self):
        index = self.ui.tabContent.currentIndex()

        plugin, document, path, ondisk = self.get_object_from_index(index)

        if ondisk:
            return self.fileSaveWithInstance(plugin, document, path)
        else:
            return self.fileSaveAs()



    def fileSaveAs(self):
        index = self.ui.tabContent.currentIndex()

        plugin, document, path, ondisk = self.get_object_from_index(index)

        path_new = self.fileSaveAsWithInstance(plugin, document)

        if path_new == None:
            ret = QtGui.QMessageBox.critical(self.gui, "Application",
                    "Problem occured whan trying to save the document.\n")
            return False

        self.mapdocuments[path_new] =  {
                "tab" : self.mapdocuments[path]["tab"],
                "document" : plugin.get_document(path),
                "plugin" : plugin,
                "ondisk" : True
            }


        del self.mapdocuments[path]
        self.ui.tabContent.setTabText(index,path_new)

        return True


    def fileSaveWithInstance(self,plugin, document, path):
        return plugin.fileSave(path, document)

    def fileSaveAsWithInstance(self,plugin, document):
        path = plugin.fileSaveAs(document)
        return path