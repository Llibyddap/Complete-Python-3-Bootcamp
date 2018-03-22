#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 20:14:15 2018

@author: Bill Armstrong
         GitHub:  Libbyddap
"""

import sys
from PyQt5 import QtWidgets, QtGui


def window():

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt 5 - First Window")
    window.setGeometry(50, 50, 500, 300)
    l1 = QtWidgets.QLabel(window)
    l2 = QtWidgets.QLabel(window)
    l1.setText("Hello World")
    l2.setPixmap(QtGui.QPixmap('globe.png'))
    l1.move(130, 20)
    l2.move(120, 100)
    window.show()
    sys.exit(app.exec_())


window()
