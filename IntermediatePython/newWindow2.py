#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 21:20:09 2018

@author: Bill Armstrong
         GitHub:  Libbyddap
"""

import sys
from PyQt5 import QtWidgets, QtGui


def window():

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt 5 - Button Window")
    window.setGeometry(50, 50, 500, 300)
    button = QtWidgets.QPushButton(window)
    button.setText("Push Button")
    button.move(130, 50)
    label = QtWidgets.QLabel(window)
    label.setText("Check out the TEXT")
    label.move(130, 90)
    window.show()
    sys.exit(app.exec_())


window()
