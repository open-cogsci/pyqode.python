# -*- coding: utf-8 -*-
"""
This is a simple test script to that is meant to be run by Travis CI to ensure
everything works properly foreach bindings on each supported python
version (3.2, 3.3, 3.4).

It runs a QApplication and shows a QPythonCodeEdit for 500ms.
"""
import sys
import logging

from PyQt4 import QtCore, QtGui

from pyqode.core import frontend
from pyqode.python.backend import server
from pyqode.python.frontend.code_edit import PyCodeEdit

logging.basicConfig(level=True)


def leave():
    app = QtGui.QApplication.instance()
    app.exit(0)


def test_editor():
    app = QtGui.QApplication(sys.argv)
    editor = PyCodeEdit()
    editor.show()
    frontend.start_server(editor, server.__file__)
    frontend.open_file(editor, __file__)
    QtCore.QTimer.singleShot(2000, leave)
    app.exec_()
    frontend.stop_server(editor)
    del editor
    del app