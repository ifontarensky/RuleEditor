
Install RuleEditor
-------------------

:: 

    $ sudo apt-get update
    $ sudo apt-get install libtool
    $ sudo apt-get install autoconf
    $ sudo apt-get install automake
    $ sudo apt-get install build-essential libtool autoconf automake


    $ sudo aptitude install qt4-qmake
    $ sudo aptitude install libqt4-dev


Install In Virtualenv
---------------------

::

    $ make env
    $ source virtualenv/bin/activate
    $ make install-pyqt
    $ make install-app install-plugins

Yara Editor
-----------
    To use Yara editor, you need to have libyara.so.3 linked. So in root add :
    $ sudo ldconfig -f $(VENVDIR)/etc/ld.so.conf

