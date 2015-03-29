#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)

from ruleeditor.plugins.codeeditor.codeeditor import CodeEditor

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

class YaraEditor(CodeEditor):
    index=-1
    def __init__(self, parent):
        super(CodeEditor, self).__init__(parent)
        self.lineNumberArea = LineNumberArea(self)
        self.completer = None

        QtCore.QObject.connect(self, QtCore.SIGNAL(_fromUtf8("blockCountChanged(int)")), self.updateLineNumberAreaWidth)
        QtCore.QObject.connect(self, QtCore.SIGNAL(_fromUtf8("updateRequest(QRect,int)")), self.updateLineNumberArea)
        QtCore.QObject.connect(self, QtCore.SIGNAL(_fromUtf8("cursorPositionChanged()")), self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()

        self.setAcceptDrops(True)

        allStrings = ["all","and","any","ascii","at",
                           "condition","contains","entrypoint","false",
                           "filesize","fullword","for","global",
                           "in","include","index","indexes","int8",
                           "int16","int32","matches","meta","nocase",
                           "not","or","of","private","rule","rva",
                           "section","strings","them","true","uint8",
                           "uint16","uint32","wide"]


        completer = QtGui.QCompleter(allStrings)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setWrapAround(False)
        self.setCompleter(completer)


    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            event.accept()
        else:
            event.reject()


    def dragLeaveEvent(self, event):
        event.accept()


    def dropEvent(self, event):
        data = event.mimeData().data("text/plain")
        tc = self.textCursor()
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)

        self.setTextCursor(tc)
        QtGui.QPlainTextEdit.dropEvent(self,event);


    def lineNumberAreaWidth(self):
        digits = 1
        max = self.qMax(1, self.blockCount())
        while (max >= 10):
            max /= 10
            ++digits

        space = 3 + self.fontMetrics().width('9') * digits+15;

        return space;

    def qMax(self, a1,  a2):
        if a1 <= a2:
            return a2
        else:
            return a1

    def updateLineNumberAreaWidth(self,value):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self,rect, dy):
        if (dy):
            self.lineNumberArea.scroll(0, dy);
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height());

        if (rect.contains(self.viewport().rect())):
            self.updateLineNumberAreaWidth(0);

    def resizeEvent(self, event):
        QtGui.QPlainTextEdit.resizeEvent(self,event);
        cr = self.contentsRect();
        self.lineNumberArea.setGeometry(QtCore.QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def highlightCurrentLine(self):
        extraSelections = list()

        if (not self.isReadOnly()):

            selection = QtGui.QTextEdit.ExtraSelection()

            lineColor = QtGui.QColor(Qt.yellow).lighter(160)

            selection.format.setBackground(lineColor)
            selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)


        self.setExtraSelections(extraSelections);

    def lineNumberAreaPaintEvent(self,event):

        painter= QtGui.QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)



        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        # print block.isValid(),blockNumber,top,event.rect().bottom()

        while (block.isValid() and top <= event.rect().bottom()):

            if (block.isVisible() and bottom >= event.rect().top()):
                number = str(blockNumber + 1)

                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), self.fontMetrics().height(), Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber+=1

    def setCompleter(self, completer):
        if self.completer:
            self.disconnect(self.completer, QtCore.SIGNAL(""), self.insertCompletion)

        if not completer:
            return

        completer.setWidget(self)
        completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer = completer
        self.connect(self.completer,
            QtCore.SIGNAL("activated(const QString&)"), self.insertCompletion)

    def completer(self):
        return self.completer


    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (len(completion) - len(self.completer.completionPrefix()))
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)


    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QtGui.QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def focusInEvent(self,e):
        if (self.completer):
            self.completer.setWidget(self)
        QtGui.QPlainTextEdit.focusInEvent(self,e)



    def keyPressEvent(self, event):
        if self.completer and self.completer.popup().isVisible():
            if event.key() in (
            QtCore.Qt.Key_Enter,
            QtCore.Qt.Key_Return,
            QtCore.Qt.Key_Escape,
            QtCore.Qt.Key_Tab,
            QtCore.Qt.Key_Backtab):
                event.ignore()
                return

        ## has ctrl-E been pressed??
        isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and
                      event.key() == QtCore.Qt.Key_E)
        if (not self.completer or not isShortcut):
            QtGui.QPlainTextEdit.keyPressEvent(self, event)

        ## ctrl or shift key on it's own??
        ctrlOrShift = event.modifiers() in (QtCore.Qt.ControlModifier ,
                QtCore.Qt.ShiftModifier)
        if ctrlOrShift and len(event.text())==0:
            # ctrl or shift key on it's own
            return

        eow = "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="

        hasModifier = ((event.modifiers() != QtCore.Qt.NoModifier) and
                        not ctrlOrShift)

        completionPrefix = self.textUnderCursor()

        if (not isShortcut and (hasModifier or len(event.text())==0 or
        len(completionPrefix) < 3 or
        event.text()[-1] in eow )):
            self.completer.popup().hide()
            return

        if (completionPrefix != self.completer.completionPrefix()):
            self.completer.setCompletionPrefix(completionPrefix)
            popup = self.completer.popup()
            popup.setCurrentIndex(
                self.completer.completionModel().index(0,0))

        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr) ## popup it up!



class LineNumberArea(QtGui.QWidget):

    def __init__(self, parent):
    	super(LineNumberArea, self).__init__(parent)
    	self.codeEditor = parent

    def sizeHint(self):
        return QtCore.QSize(self.codeEditor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event);


# vim:ts=4:expandtab:sw=4
