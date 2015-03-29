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
    name = 'plugins-ruleeditor',
    version = '1.0.0',
    packages=[
        'ruleeditor',
        'ruleeditor/plugins',
        'ruleeditor/plugins/yara'
        ],
    # Metadata
    author = 'Ivan Fontarensky',
    author_email = 'ivan.fontarensky_at_gmail.com',
    description = 'Plugin "Yara" for a rule-editor.',
    license = 'GPLv3',


)



# vim:ts=4:expandtab:sw=4
