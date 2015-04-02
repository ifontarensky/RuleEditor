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
            

class SnortHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(SnortHighlighter, self).__init__(parent)

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkBlue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)


        SnortRuleAction = ["\\bactivate\\b", "\\balert\\b", "\\bdrop\\b",
                           "\\bdynamic\\b", "\\blog\\b", "\\bpass\\b",
                           "\\breject\\b", "\\bsdrop\\b", "\\bsblock\\b"]

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in SnortRuleAction]

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkCyan)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        SnortRuleProto  = ["\\bip\\b", "\\bicmp\\b", "\\btcp\\b", "\\budp\\b"]

        self.highlightingRules += [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in SnortRuleProto]

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.black)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        SnortRuleOptions = ["\\bmsg\\b", "\\breference\\b", "\\bgid\\b",
                            "\\bsid\\b", "\\brev\\b", "\\bclasstype\\b",
                            "\\bpriority\\b", "\\bmetadata\\b", "\\bcontent\\b",
                            "\\bnocase\\b", "\\brawbytes\\b","\\bdepth\\b",
                            "\\boffset\\b", "\\bdistance\\b", "\\bwithin\\b",
                            "\\bhttp_client_body\\b", "\\bhttp_cookie\\b",
                            "\\bhttp_raw_cookie\\b", "\\bhttp_header\\b",
                            "\\bhttp_raw_header\\b", "\\bhttp_method\\b",
                            "\\bhttp_uri\\b", "\\bhttp_raw_uri\\b",
                            "\\bhttp_stat_code\\b", "\\bhttp_stat_msg\\b",
                            "\\bfast_pattern\\b", "\\buricontent\\b",
                            "\\burilen\\b", "\\bisdataat\\b", "\\bpcre\\b",
                            "\\bpkt_data\\b", "\\bfile_data\\b", "\\bbase64_decode\\b",
                            "\\bbase64_data\\b","\\bbyte_test\\b", "\\bbyte_jump\\b",
                            "\\bbyte_extract\\b", "\\bftpbounce\\b", "\\basn1\\b",
                            "\\bcvs\\b", "\\bdce_iface\\b", "\\bdce_opnum\\b",
                            "\\bdce_stub_data\\b","\\bsip_method\\b",
                            "\\bsip_stat_code\\b", "\\bsip_header\\b",
                            "\\bsip_body\\b", "\\bgtp_type\\b", "\\bgtp_info\\b",
                            "\\bgtp_version\\b", "\\bssl_version\\b",
                            "\\bssl_state\\b", "\\bfragoffset\\b", "\\bttl\\b", "\\btos\\b", "\\bid\\b", "\\bipopts\\b", "\\bfragbits\\b", "\\bdsize\\b", "\\bflags\\b", "\\bflow\\b", "\\bflowbits\\b", "\\bseq\\b", "\\back\\b", "\\bwindow\\b",
"\\bitype\\b", "\\bicode\\b", "\\bicmp_id\\b", "\\bicmp_seq\\b", "\\brpc\\b", "\\bip_proto\\b", "\\bsameip\\b", "\\bstream_reassemble\\b", "\\bstream_size\\b",
"\\blogto\\b", "\\bsession\\b", "\\bresp\\b", "\\breact\\b", "\\btag\\b", "\\bactivates\\b", "\\bactivated_by\\b", "\\bcount\\b", "\\breplace\\b", "\\bdetection_filter\\b",
"\\bthreshold\\b"]


        self.highlightingRules += [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in SnortRuleOptions]


        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.red)
        regexp = QtCore.QRegExp("\".*\"")
        regexp.setMinimal(True)
        self.highlightingRules.append((regexp,
                quotationFormat))
        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("#[^\n]*"),
                singleLineCommentFormat))


    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)




# vim:ts=4:expandtab:sw=4