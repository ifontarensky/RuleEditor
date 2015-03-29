
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