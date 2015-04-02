# -*- coding: utf-8 -*-
#!/usr/bin/env python


__author__ = 'ifontarensky'


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

class Ui_PanelOption(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(613, 243)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 32))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnHide = QtGui.QToolButton(self.widget_3)
        self.btnHide.setText(_fromUtf8(""))
        self.btnHide.setIconSize(QtCore.QSize(32, 4))
        self.btnHide.setObjectName(_fromUtf8("btnHide"))
        self.horizontalLayout_3.addWidget(self.btnHide)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_3)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblPath = QtGui.QLabel(Form)
        self.lblPath.setObjectName(_fromUtf8("lblPath"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblPath)
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.editPathMalware = QtGui.QLineEdit(self.widget)
        self.editPathMalware.setObjectName(_fromUtf8("editPathMalware"))
        self.horizontalLayout.addWidget(self.editPathMalware)
        self.btnBrowse = QtGui.QToolButton(self.widget)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.widget)
        self.verticalLayout.addLayout(self.formLayout)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnTest = QtGui.QPushButton(self.widget_2)
        self.btnTest.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnTest.setObjectName(_fromUtf8("btnTest"))
        self.btnTest.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.btnTest)
        self.verticalLayout.addWidget(self.widget_2)
        self.editResult = QtGui.QPlainTextEdit(Form)
        self.editResult.setReadOnly(True)
        self.editResult.setObjectName(_fromUtf8("editResult"))
        self.editResult.setVisible(False)
        self.verticalLayout.addWidget(self.editResult)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
















    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lblPath.setText(_translate("Form", "Malware", None))
        self.btnBrowse.setText(_translate("Form", "...", None))
        self.btnTest.setText(_translate("Form", "Test", None))
