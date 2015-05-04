# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ifontarensky/Workspace/yara/RuleEditor/source_core/ruleeditor/ui/dialogSettings.ui'
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

class Ui_DialogSettings(object):
    def setupUi(self, DialogSettings):
        DialogSettings.setObjectName(_fromUtf8("DialogSettings"))
        DialogSettings.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(DialogSettings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(DialogSettings)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabPlugin = QtGui.QWidget()
        self.tabPlugin.setObjectName(_fromUtf8("tabPlugin"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabPlugin)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.treePlugin = QtGui.QTreeWidget(self.tabPlugin)
        self.treePlugin.setAlternatingRowColors(True)
        self.treePlugin.setObjectName(_fromUtf8("treePlugin"))
        self.treePlugin.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.treePlugin)
        self.tabWidget.addTab(self.tabPlugin, _fromUtf8(""))
        self.tabAppareance = QtGui.QWidget()
        self.tabAppareance.setObjectName(_fromUtf8("tabAppareance"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabAppareance)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBoxScheme = QtGui.QGroupBox(self.tabAppareance)
        self.groupBoxScheme.setObjectName(_fromUtf8("groupBoxScheme"))
        self.formLayout = QtGui.QFormLayout(self.groupBoxScheme)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.rbSchemeDefault = QtGui.QRadioButton(self.groupBoxScheme)
        self.rbSchemeDefault.setObjectName(_fromUtf8("rbSchemeDefault"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.rbSchemeDefault)
        self.rbSchemeDarkStyle = QtGui.QRadioButton(self.groupBoxScheme)
        self.rbSchemeDarkStyle.setObjectName(_fromUtf8("rbSchemeDarkStyle"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.rbSchemeDarkStyle)
        self.rbSchemeDarkOrange = QtGui.QRadioButton(self.groupBoxScheme)
        self.rbSchemeDarkOrange.setObjectName(_fromUtf8("rbSchemeDarkOrange"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.rbSchemeDarkOrange)
        self.rbSchemeXMas = QtGui.QRadioButton(self.groupBoxScheme)
        self.rbSchemeXMas.setObjectName(_fromUtf8("rbSchemeXMas"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.rbSchemeXMas)
        self.rbSchemeOxygen = QtGui.QRadioButton(self.groupBoxScheme)
        self.rbSchemeOxygen.setObjectName(_fromUtf8("rbSchemeOxygen"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.rbSchemeOxygen)
        self.rbSchemeMetal = QtGui.QRadioButton(self.groupBoxScheme)
        self.rbSchemeMetal.setObjectName(_fromUtf8("rbSchemeMetal"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.rbSchemeMetal)
        self.verticalLayout_4.addWidget(self.groupBoxScheme)
        self.tabWidget.addTab(self.tabAppareance, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(DialogSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogSettings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSettings)

    def retranslateUi(self, DialogSettings):
        DialogSettings.setWindowTitle(_translate("DialogSettings", "Settings", None))
        self.treePlugin.headerItem().setText(0, _translate("DialogSettings", "check", None))
        self.treePlugin.headerItem().setText(1, _translate("DialogSettings", "name", None))
        self.treePlugin.headerItem().setText(2, _translate("DialogSettings", "path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlugin), _translate("DialogSettings", "Plugins", None))
        self.groupBoxScheme.setTitle(_translate("DialogSettings", "Skin", None))
        self.rbSchemeDefault.setText(_translate("DialogSettings", "Default", None))
        self.rbSchemeDarkStyle.setText(_translate("DialogSettings", "Dark Style", None))
        self.rbSchemeDarkOrange.setText(_translate("DialogSettings", "Dark Orange", None))
        self.rbSchemeXMas.setText(_translate("DialogSettings", "XMas", None))
        self.rbSchemeOxygen.setText(_translate("DialogSettings", "Oxygen", None))
        self.rbSchemeMetal.setText(_translate("DialogSettings", "Metal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAppareance), _translate("DialogSettings", "Apparence", None))

