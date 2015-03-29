# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
#       Author:  Vicent Mas - vmas@vitables.org

"""
Basic constant.

This module indicates contants use in ``ruleeditor`` package
Mac OS X boxes use the module as is.

Misc variables:

* __docformat__
* INSTALLDIR
* ICONDIR
* DOCDIR
* PLUGINSDIR
"""


__author__ = 'ifontarensky'
__docformat__ = 'restructuredtext'

import os.path

INSTALLDIR = os.path.dirname(__file__)
COREDIR = os.path.join(INSTALLDIR, "core")
ICONDIR = os.path.join(INSTALLDIR, "icons")
DOCDIR = os.path.join(INSTALLDIR, "htmldocs")
PLUGINSDIR = os.path.join(INSTALLDIR, "plugins")
