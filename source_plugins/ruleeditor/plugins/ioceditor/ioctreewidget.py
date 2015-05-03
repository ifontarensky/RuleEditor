__author__ = 'ifontarensky'

import os
import xml.etree.ElementTree as ET

from PyQt4 import QtCore, QtGui

from ruleeditor.plugins.ioceditor.IOCWidget import Ui_FormIOC
from ruleeditor.plugins.ioceditor.iocterms import iocterms

SCHEMAS = '{http://schemas.mandiant.com/2010/ioc}'

ELEMENTS = ["short_description", "description", "authored_by", "authored_date",
          "links", "link", "definition", "Indicator", "IndicatorItem",
          "Context", "Content", "keywords", "keyword"]

CONDITIONS = ["is", "contains", "matches", "starts-with", "ends-with", "greater-than", "less-than"]

ATTRIB = ["operator"]

class IOCTreeWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(IOCTreeWidget, self).__init__(parent)
        self.elements = ELEMENTS
        self.attrib = ATTRIB

    def setupUi(self):
        self.uiPanel=Ui_FormIOC()
        self.uiPanel.setupUi(self)
        self.uiPanel.wEditItem.setVisible(False)
        self.uiPanel.treeWidget.itemChanged.connect(self.itemChanged)
        self.uiPanel.treeWidget.itemSelectionChanged.connect(self.itemSelectionChanged)
        self.uiPanel.cbOperand.currentIndexChanged.connect(self.cbOperandChanged)
        self.uiPanel.cbItem.currentIndexChanged.connect(self.cbItemChanged)
        self.uiPanel.cbCondition.currentIndexChanged.connect(self.cbConditionChanged)
        self.uiPanel.editItem.textChanged.connect(self.editItemChanged)
        self.loadiocterms()


    def set_xmlns(self, xmlns):
        self.xmlns = xmlns
        for element in ELEMENTS:
            setattr(self, "tag_"+element, self.xmlns+element)

    def set_short_description(self, value):
        self.short_description = value
        self.uiPanel.editShortDescription.setText(value)

    def set_description(self, value):
        self.description = value
        self.uiPanel.editDescription.insertPlainText(value)


    def set_authored_by(self, value):
        self.authored_by = value
        self.uiPanel.editAuthoredBy.setText(value)

    def set_authored_date(self, value):
        from datetime import datetime, date, time
        self.authored_date = value
        try:
            dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
        except:
            dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        self.uiPanel.dateTimeEdit.setDateTime(dt)

    def set_links(self, value):
        self.links = value
        for link in self.links:
            self.uiPanel.links.insertItem(0,link)

    def set_keywords(self, value):
        self.keywords = value
        for keyword in self.keywords:
            self.uiPanel.keywords.insertItem(0, keyword)

    def loadiocterms(self):
        root = ET.fromstring(iocterms)
        self.iocterms = dict()
        for child in root:
            self.uiPanel.cbItem.insertItem(0, child.attrib['text'])
            self.iocterms[child.attrib['text']]= {
                "description" : child.attrib['title'],
                "type" : child.attrib['display-type']

            }
        self.uiPanel.cbCondition.insertItems(0, CONDITIONS)


    def load_ioc(self, data):
        self.root = ET.fromstring(data)
        self.parse_root(self.root)

    def toPlainText(self):

        self.root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        self.root.attrib["xmlns:xsd"] = "http://www.w3.org/2001/XMLSchema"
        plaintext = ET.tostring(self.root)
        plaintext = plaintext.replace('ns0:','')
        plaintext = plaintext.replace(':ns0','')
        return plaintext


    def parse_root(self, root):
        self.set_xmlns(SCHEMAS)
        for child in root:
            if child.tag == self.tag_short_description:
                self.set_short_description(child.text)

            elif child.tag == self.tag_description:
                self.set_description(child.text)

            elif child.tag == self.tag_authored_by:
                self.set_authored_by(child.text)

            elif child.tag == self.tag_authored_date:
                self.set_authored_date(child.text)

            elif child.tag == self.tag_links:
                self.parse_links(child)

            elif child.tag == self.tag_definition:
                self.parse_definition(child)

            elif child.tag == self.tag_keywords:
                self.parse_keywords(child)

            else:
                print "! Error : When trying to parse root", child.tag

    def parse_links(self, root):
        links = list()
        for child in root:
            if child.tag == self.tag_link:
                links.append(child.text)
            else:
                print "! Error : When trying to parse links", child.tag
        self.set_links(links)

    def parse_keywords(self, root):
        keywords = list()
        for child in root:
            if child.tag == self.tag_keyword:
                keywords.append(child.text)
            else:
                print "! Error : When trying to parse links", child.tag
        self.uiPanel.keywords.setPlainText(";".join(keywords))

    def parse_definition(self, root):
        self.indicators = dict()
        for child in  root:
            if child.tag == self.tag_Indicator:
                self.indicators[child.attrib["id"]] = QtGui.QTreeWidgetItem(self.uiPanel.treeWidget)
                self.indicators[child.attrib["id"]].setText(0, child.attrib["operator"])
                self.indicators[child.attrib["id"]].setText(1, "operator")
                self.indicators[child.attrib["id"]].setText(5, child.attrib["id"])
                self.indicators[child.attrib["id"]].setExpanded(True)
                self.parse_indicator(child, child.attrib["id"])
            else:
                print "! Error : When trying to parse definition", child.tag

    def parse_indicator(self, root, parent_id):
        for child in root:
            if child.tag == self.tag_Indicator:
                self.indicators[child.attrib["id"]] = QtGui.QTreeWidgetItem(self.indicators[parent_id])
                self.indicators[child.attrib["id"]].setText(0, child.attrib["operator"])
                self.indicators[child.attrib["id"]].setText(1, "operator")
                self.indicators[child.attrib["id"]].setText(5, child.attrib["id"])
                self.indicators[child.attrib["id"]].setExpanded(True)
                self.parse_indicator(child, child.attrib["id"])
            elif child.tag == self.tag_IndicatorItem:
                condition = child.attrib["condition"]
                self.parse_indicatoritem(child,  child.attrib["id"], parent_id, condition)
            else:
                print "! Error : When trying to parse definition", child.tag

    def parse_indicatoritem(self, root, current_id, parent_id, condition):
        for child in root:
            if child.tag == self.tag_Context:
                op1 = child.attrib["search"]
            elif child.tag == self.tag_Content:
                op2 = child.text
            else:
                print "! Error : When trying to parse definition", child.tag

        self.indicators[current_id] = QtGui.QTreeWidgetItem(self.indicators[parent_id])
        value = "{0} {1} {2}".format(op1, condition, op2)
        self.indicators[current_id].setText(0, value)
        self.indicators[current_id].setText(1, "indicatoritem")
        self.indicators[current_id].setText(2, op1)
        self.indicators[current_id].setText(3, condition)
        self.indicators[current_id].setText(4, op2)
        self.indicators[current_id].setText(5, current_id)
        self.indicators[current_id].setExpanded(True)
        flags = self.indicators[current_id].flags()
        flags |= QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        self.indicators[current_id].setFlags(flags)

    def itemChanged(self, item, column):
        #print "itemChanged", item
        pass

    def itemSelectionChanged(self):
        for item in self.uiPanel.treeWidget.selectedItems ():
            if item.text(1) == "operator":
                self.uiPanel.wEditOperand.setVisible(True)
                self.uiPanel.wEditItem.setVisible(False)
                self.select_text_in_combobox(self.uiPanel.cbOperand, item.text(0))
            if item.text(1) == "indicatoritem":
                self.uiPanel.wEditItem.setVisible(True)
                self.uiPanel.wEditOperand.setVisible(False)
                self.select_text_in_combobox(self.uiPanel.cbItem, item.text(2))
                self.select_text_in_combobox(self.uiPanel.cbCondition, item.text(3))
                self.uiPanel.editItem.setText(item.text(4))

    def select_text_in_combobox(self, combobox, value):
        index = combobox.findText(value)
        combobox.setCurrentIndex(index)

    def cbOperandChanged(self, index):
        value = self.uiPanel.cbOperand.itemText(index)
        for item in self.uiPanel.treeWidget.selectedItems ():
            item.setText(0,value)

            for target in self.root.findall(".//%s"%self.tag_Indicator):
                if target.attrib["id"] == item.text(5):
                    target.attrib["operator"] = item.text(0)

    def cbItemChanged(self, index):
        text = self.uiPanel.cbItem.itemText(index)
        for item in self.uiPanel.treeWidget.selectedItems ():
            item.setText(2,text)
            value = "{0} {1} {2}".format(text, item.text(3), item.text(4))
            item.setText(0, value)

            # Modify Tree in memory
            for target in self.root.findall(".//%s"%self.tag_IndicatorItem):
                if target.attrib["id"] == item.text(5):
                    for child in target:
                        if 'document' in child.attrib.keys():
                            type =  self.iocterms[text]['type']
                            child.attrib['search'] = text
                            child.attrib['document'] = text.split('/')[0]
                            if child.attrib['document'] == "Network":
                                child.attrib['type'] = "network"
                            else:
                                child.attrib['type'] = "mir"

    def cbConditionChanged(self, index):
        text = self.uiPanel.cbCondition.itemText(index)
        for item in self.uiPanel.treeWidget.selectedItems ():
            item.setText(3,text)
            value = "{0} {1} {2}".format(item.text(2), item.text(3), item.text(4))
            item.setText(0, value)
            # Modify Tree in memory
            for target in self.root.findall(".//%s"%self.tag_IndicatorItem):
                if target.attrib["id"] == item.text(5):
                    target.attrib["condition"]=text

    def editItemChanged(self, text):

        for item in self.uiPanel.treeWidget.selectedItems ():
            item.setText(4,text)
            value = "{0} {1} {2}".format(item.text(2), item.text(3), item.text(4))
            item.setText(0, value)

            # Modify Tree in memory
            for target in self.root.findall(".//%s"%self.tag_IndicatorItem):
                if target.attrib["id"] == item.text(5):
                    for child in target:
                        if 'document' in child.attrib.keys():
                            c1 = child
                        else:
                            c2 = child
                    c2.text = text
                    search = c1.attrib['search']
                    c2.attrib["type"] = self.iocterms[search]['type']