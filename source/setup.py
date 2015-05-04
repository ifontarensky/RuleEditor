#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@twitter:      @ifontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""

from setuptools import setup

setup(
    name = 'rule-editor',
    version = '1.0.0',
    packages=[
        'ruleeditor',
        'ruleeditor/ui',
        'ruleeditor/core/',
        'ruleeditor/plugins',
        'ruleeditor/plugins/codeeditor',
        'ruleeditor/plugins/ioceditor',
        'ruleeditor/plugins/snorteditor',
        'ruleeditor/plugins/yaraeditor'],
    scripts = ['bin/rule-editor'],
    # Metadata
    author = 'Ivan Fontarensky',
    author_email = 'ivan.fontarensky_at_gmail.com',
    description = 'rule-editor is a free editor to create rule.',
    license = 'GPLv3',
#    requires=["somepackage (>1.0, !=1.5)"],
    # keywords = '',

)



# vim:ts=4:expandtab:sw=4
