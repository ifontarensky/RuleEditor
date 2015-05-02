#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""


__author__ = 'ifontarensky'

from PyQt4 import QtGui
from PyQt4 import QtCore

DEFAULT_SYNTAX_CHAR		= QtCore.Qt.blue
DEFAULT_ELEMENT_NAME	= QtCore.Qt.darkRed
DEFAULT_COMMENT			= QtCore.Qt.darkGreen
DEFAULT_ATTRIBUTE_NAME	= QtCore.Qt.red
DEFAULT_ATTRIBUTE_VALUE	= QtCore.Qt.blue
DEFAULT_ERROR			= QtCore.Qt.darkMagenta
DEFAULT_OTHER			= QtCore.Qt.black

# Regular expressions for parsing XML borrowed from:
# http://www.cs.sfu.ca/~cameron/REX.html
EXPR_COMMENT			= "<!--[^-]*-([^-][^-]*-)*->";
EXPR_COMMENT_BEGIN		= "<!--";
EXPR_COMMENT_END		= "[^-]*-([^-][^-]*-)*->";
EXPR_ATTRIBUTE_VALUE	= "\"[^<\"]*\"|'[^<']*'";
EXPR_NAME				= "([A-Za-z_:]|[^\\x00-\\x7F])([A-Za-z0-9_:.-]|[^\\x00-\\x7F])*";



class IOCHighlighter(QtGui.QSyntaxHighlighter):

    def __init__(self, parent=None):
        super(IOCHighlighter, self).__init__(parent)

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(DEFAULT_ELEMENT_NAME)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        keywordPatterns = ["\\b?ioc\\b", "\\b?openioc\\b", "/>", ">", "<"]

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        xmlElementFormat = QtGui.QTextCharFormat()
        xmlElementFormat.setForeground(DEFAULT_ELEMENT_NAME)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=[\s/>])"), xmlElementFormat))

        xmlAttributeFormat = QtGui.QTextCharFormat()
        xmlAttributeFormat.setFontItalic(True)
        xmlAttributeFormat.setForeground(DEFAULT_ATTRIBUTE_NAME)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\=)"), xmlAttributeFormat))

        self.valueFormat = QtGui.QTextCharFormat()
        self.valueFormat.setForeground(DEFAULT_ATTRIBUTE_VALUE)

        self.valueStartExpression = QtCore.QRegExp("\"")
        self.valueEndExpression = QtCore.QRegExp("\"(?=[\s></])")

        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(DEFAULT_COMMENT)
        #self.highlightingRules.append((QtCore.QRegExp("<!--[^\n]*-->"), singleLineCommentFormat))
        self.highlightingRules.append((QtCore.QRegExp(EXPR_COMMENT), singleLineCommentFormat))


    def highlightBlock(self, text):

        #for every pattern
        for pattern, format in self.highlightingRules:
            #Create a regular expression from the retrieved pattern
            expression = QtCore.QRegExp(pattern)

            #Check what index that expression occurs at with the ENTIRE text
            index = expression.indexIn(text)

            #While the index is greater than 0
            while index >= 0:

                #Get the length of how long the expression is true, set the format from the start to the length with the text format
                length = expression.matchedLength()
                self.setFormat(index, length, format)

                #Set index to where the expression ends in the text
                index = expression.indexIn(text, index + length)


        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.valueStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.valueEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.valueEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength, self.valueFormat)

            startIndex = self.valueStartExpression.indexIn(text, startIndex + commentLength);
