
 Rule Editor
==============

Description
------------


Requirements
------------

- Python 2.7

- virtualenv

- sip-4.16.6+ (http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.6/sip-4.16.6.zip)

- PyQt 4.11.3+ (http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.3/PyQt-x11-gpl-4.11.3.tar.gz)

- YARA 3.3.0 (https://github.com/plusvic/yara/archive/v3.3.0.tar.gz)




Install RuleEditor
-------------------

Without Virtualenv
^^^^^^^^^^^^^^^^^^

:: 

   $ pip install rule_editor-1.0.0-py2-none-any.whl
   $ pip install plugins_ruleeditor-1.0.0-py2-none-any.whl




With Virtualenv
^^^^^^^^^^^^^^^^^^^^^

::

    $ sudo apt-get update
    $ sudo apt-get install libtool
    $ sudo apt-get install autoconf
    $ sudo apt-get install automake
    $ sudo apt-get install build-essential libtool autoconf automake
    $ sudo apt-get install qt4-qmake
    $ sudo apt-get install libqt4-dev

::

    $ make env
    $ source virtualenv/bin/activate
    $ make install-pyqt
    $ make install-app install-plugins





