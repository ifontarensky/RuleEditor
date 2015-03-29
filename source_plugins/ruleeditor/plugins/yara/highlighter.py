#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""


from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import (QObject, Qt, SIGNAL, SLOT)
            

class YaraHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(YaraHighlighter, self).__init__(parent)

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkBlue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        keywordPatterns = ["\\ball\\b","\\band\\b","\\bany\\b","\\bascii\\b","\\bat\\b",
                           "\\bcondition\\b","\\bcontains\\b","\\bentrypoint\\b","\\bfalse\\b",
                           "\\bfilesize\\b","\\bfullword\\b","\\bfor\\b","\\bglobal\\b",
                           "\\bin\\b","\\binclude\\b","\\bindex\\b","\\bindexes\\b","\\bint8\\b",
                           "\\bint16\\b","\\bint32\\b","\\bmatches\\b","\\bmeta\\b","\\bnocase\\b",
                           "\\bnot\\b","\\bor\\b","\\bof\\b","\\bprivate\\b","\\brule\\b","\\brva\\b",
                           "\\bsection\\b","\\bstrings\\b","\\bthem\\b","\\btrue\\b","\\buint8\\b",
                           "\\buint16\\b","\\buint32\\b","\\bwide\\b"]


        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        classFormat = QtGui.QTextCharFormat()
        classFormat.setFontWeight(QtGui.QFont.Bold)
        classFormat.setForeground(QtCore.Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp("\\b\$[A-Za-z]+\\b"),
                classFormat))

        

        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.red)

        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""),
                quotationFormat))

        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength);


class OutputHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(OutputHighlighter, self).__init__(parent)

        keywordFormatError = QtGui.QTextCharFormat()
        keywordFormatError.setForeground(QtCore.Qt.red)
        keywordFormatGood = QtGui.QTextCharFormat()
        keywordFormatGood.setForeground(QtCore.Qt.green)
        keywordFormatError.setFontWeight(QtGui.QFont.Bold)
        keywordFormatGood.setFontWeight(QtGui.QFont.Bold)

        keywordError = ["\\Error\\b","\\Warning\\b","\\UnboundLocalError\\b","\\SyntaxError\\b",
                        "\\UnicodeEncodeError\\b"]

        keywordGood = ["\\Signature match\\b"]


        self.highlightingError = [(QtCore.QRegExp(pattern), keywordFormatError) for pattern in keywordError]
        self.highlightingGood = [(QtCore.QRegExp(pattern), keywordFormatGood) for pattern in keywordGood]


    def highlightBlock(self, text):
        for pattern, format in self.highlightingError:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        for pattern, format in self.highlightingGood:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)


        self.setCurrentBlockState(0)


# vim:ts=4:expandtab:sw=4