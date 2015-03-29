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


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import (QObject, Qt, QDir, SIGNAL, SLOT)


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

class CodeEditor(QtGui.QPlainTextEdit):
    index=-1
    def __init__(self, parent):
        super(CodeEditor, self).__init__(parent)
        self.lineNumberArea = LineNumberArea(self)

        QtCore.QObject.connect(self, QtCore.SIGNAL(_fromUtf8("blockCountChanged(int)")), self.updateLineNumberAreaWidth)
        QtCore.QObject.connect(self, QtCore.SIGNAL(_fromUtf8("updateRequest(QRect,int)")), self.updateLineNumberArea)
        QtCore.QObject.connect(self, QtCore.SIGNAL(_fromUtf8("cursorPositionChanged()")), self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()

        self.setAcceptDrops(True)


    def dragEnterEvent(self, event):
        pass

    def dragLeaveEvent(self, event):
        pass

    def dropEvent(self, event):
        pass

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
            self.lineNumberArea.update(0, rect.y(),
                                       self.lineNumberArea.width(),
                                       rect.height());

        if (rect.contains(self.viewport().rect())):
            self.updateLineNumberAreaWidth(0);

    def resizeEvent(self, event):
        QtGui.QPlainTextEdit.resizeEvent(self,event);
        cr = self.contentsRect();
        self.lineNumberArea.setGeometry(QtCore.QRect(cr.left(), cr.top(),
                                                     self.lineNumberAreaWidth(),
                                                     cr.height()))

    def highlightCurrentLine(self):
        extraSelections = list()

        if (not self.isReadOnly()):

            selection = QtGui.QTextEdit.ExtraSelection()

            lineColor = QtGui.QColor(Qt.yellow).lighter(160)

            selection.format.setBackground(lineColor)
            selection.format.setProperty(
                QtGui.QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)

        self.setExtraSelections(extraSelections);

    def lineNumberAreaPaintEvent(self,event):

        painter= QtGui.QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(
            self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        # print block.isValid(),blockNumber,top,event.rect().bottom()

        while (block.isValid() and top <= event.rect().bottom()):

            if (block.isVisible() and bottom >= event.rect().top()):
                number = str(blockNumber + 1)

                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(),
                                 self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber+=1


    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QtGui.QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def focusInEvent(self,e):
        pass


    def keyPressEvent(self, event):
        ## has ctrl-E been pressed??
        isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and
                      event.key() == QtCore.Qt.Key_E)
        if (not isShortcut):
            QtGui.QPlainTextEdit.keyPressEvent(self, event)


class LineNumberArea(QtGui.QWidget):

    def __init__(self, parent):
        super(LineNumberArea, self).__init__(parent)
        self.codeEditor = parent

    def sizeHint(self):
        return QtCore.QSize(self.codeEditor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event);


# vim:ts=4:expandtab:sw=4
