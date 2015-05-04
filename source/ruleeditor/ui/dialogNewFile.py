# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ifontarensky/Workspace/yara/RuleEditor/source_core/ruleeditor/ui/dialogNewFile.ui'
#
# Created: Sun May  3 17:41:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(350, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listPlugin = QtGui.QTableWidget(Dialog)
        self.listPlugin.setAlternatingRowColors(True)
        self.listPlugin.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listPlugin.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listPlugin.setShowGrid(False)
        self.listPlugin.setCornerButtonEnabled(True)
        self.listPlugin.setObjectName(_fromUtf8("listPlugin"))
        self.listPlugin.setColumnCount(3)
        self.listPlugin.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.listPlugin.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.listPlugin.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.listPlugin.setHorizontalHeaderItem(2, item)
        self.listPlugin.horizontalHeader().setVisible(False)
        self.listPlugin.horizontalHeader().setHighlightSections(True)
        self.listPlugin.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.listPlugin)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create New File", None))
        item = self.listPlugin.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Icon", None))
        item = self.listPlugin.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name", None))
        item = self.listPlugin.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Extension", None))

