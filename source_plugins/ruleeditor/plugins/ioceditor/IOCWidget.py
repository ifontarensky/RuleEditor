# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ifontarensky/Workspace/yara/RuleEditor/source_plugins/ruleeditor/plugins/ioceditor/IOCWidget.ui'
#
# Created: Sun Apr  5 13:08:29 2015
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

class Ui_FormIOC(object):
    def setupUi(self, FormIOC):
        FormIOC.setObjectName(_fromUtf8("FormIOC"))
        FormIOC.resize(930, 473)
        self.verticalLayout = QtGui.QVBoxLayout(FormIOC)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(FormIOC)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.widget)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget.header().setVisible(False)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblShortDescription = QtGui.QLabel(self.groupBox)
        self.lblShortDescription.setObjectName(_fromUtf8("lblShortDescription"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblShortDescription)
        self.editShortDescription = QtGui.QLineEdit(self.groupBox)
        self.editShortDescription.setObjectName(_fromUtf8("editShortDescription"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.editShortDescription)
        self.lblDescription = QtGui.QLabel(self.groupBox)
        self.lblDescription.setObjectName(_fromUtf8("lblDescription"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblDescription)
        self.lblAuthoredBy = QtGui.QLabel(self.groupBox)
        self.lblAuthoredBy.setObjectName(_fromUtf8("lblAuthoredBy"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblAuthoredBy)
        self.editAuthoredBy = QtGui.QLineEdit(self.groupBox)
        self.editAuthoredBy.setObjectName(_fromUtf8("editAuthoredBy"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.editAuthoredBy)
        self.editDescription = QtGui.QPlainTextEdit(self.groupBox)
        self.editDescription.setObjectName(_fromUtf8("editDescription"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.editDescription)
        self.lblDate = QtGui.QLabel(self.groupBox)
        self.lblDate.setObjectName(_fromUtf8("lblDate"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblDate)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.dateTimeEdit)
        self.lblLinks = QtGui.QLabel(self.groupBox)
        self.lblLinks.setObjectName(_fromUtf8("lblLinks"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblLinks)
        self.links = QtGui.QComboBox(self.groupBox)
        self.links.setEditable(True)
        self.links.setObjectName(_fromUtf8("links"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.links)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label)
        self.keywords = QtGui.QTextEdit(self.groupBox)
        self.keywords.setLineWidth(-12)
        self.keywords.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.keywords.setObjectName(_fromUtf8("keywords"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.keywords)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.widget)
        self.wEditOperand = QtGui.QWidget(FormIOC)
        self.wEditOperand.setObjectName(_fromUtf8("wEditOperand"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.wEditOperand)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Operand = QtGui.QLabel(self.wEditOperand)
        self.Operand.setObjectName(_fromUtf8("Operand"))
        self.horizontalLayout_2.addWidget(self.Operand)
        self.cbOperand = QtGui.QComboBox(self.wEditOperand)
        self.cbOperand.setObjectName(_fromUtf8("cbOperand"))
        self.cbOperand.addItem(_fromUtf8(""))
        self.cbOperand.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cbOperand)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.wEditOperand)
        self.wEditItem = QtGui.QWidget(FormIOC)
        self.wEditItem.setObjectName(_fromUtf8("wEditItem"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.wEditItem)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbItem = QtGui.QComboBox(self.wEditItem)
        self.cbItem.setMinimumSize(QtCore.QSize(200, 0))
        self.cbItem.setObjectName(_fromUtf8("cbItem"))
        self.horizontalLayout_3.addWidget(self.cbItem)
        self.cbCondition = QtGui.QComboBox(self.wEditItem)
        self.cbCondition.setObjectName(_fromUtf8("cbCondition"))
        self.horizontalLayout_3.addWidget(self.cbCondition)
        self.editItem = QtGui.QLineEdit(self.wEditItem)
        self.editItem.setMinimumSize(QtCore.QSize(300, 0))
        self.editItem.setObjectName(_fromUtf8("editItem"))
        self.horizontalLayout_3.addWidget(self.editItem)
        self.verticalLayout.addWidget(self.wEditItem)

        self.retranslateUi(FormIOC)
        QtCore.QMetaObject.connectSlotsByName(FormIOC)

    def retranslateUi(self, FormIOC):
        FormIOC.setWindowTitle(_translate("FormIOC", "Form", None))
        self.groupBox.setTitle(_translate("FormIOC", "Meta - Data", None))
        self.lblShortDescription.setText(_translate("FormIOC", "Short Description", None))
        self.lblDescription.setText(_translate("FormIOC", "Description", None))
        self.lblAuthoredBy.setText(_translate("FormIOC", "Authored By", None))
        self.lblDate.setText(_translate("FormIOC", "Autore Dated", None))
        self.lblLinks.setText(_translate("FormIOC", "Links", None))
        self.label.setText(_translate("FormIOC", "Keywords", None))
        self.Operand.setText(_translate("FormIOC", "Operand", None))
        self.cbOperand.setItemText(0, _translate("FormIOC", "OR", None))
        self.cbOperand.setItemText(1, _translate("FormIOC", "AND", None))

