# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loteriasWeb.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 462)
        Form.setMinimumSize(QtCore.QSize(621, 462))
        Form.setMaximumSize(QtCore.QSize(621, 462))
        self.widget = QtWebEngineWidgets.QWebEngineView(Form)
        self.widget.setGeometry(QtCore.QRect(10, 58, 601, 391))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 5, 561, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonBack = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setWhatsThis("")
        self.pushButtonBack.setStyleSheet("")
        self.pushButtonBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Downloads/Custom-Icon-Design-Flatastic-1-Back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBack.setIcon(icon)
        self.pushButtonBack.setIconSize(QtCore.QSize(100, 24))
        self.pushButtonBack.setFlat(True)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.horizontalLayout.addWidget(self.pushButtonBack)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonReload = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonReload.setFont(font)
        self.pushButtonReload.setStyleSheet("")
        self.pushButtonReload.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/Downloads/Custom-Icon-Design-Flatastic-8-Refresh.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonReload.setIcon(icon1)
        self.pushButtonReload.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonReload.setFlat(True)
        self.pushButtonReload.setObjectName("pushButtonReload")
        self.horizontalLayout.addWidget(self.pushButtonReload)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonForward = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonForward.setFont(font)
        self.pushButtonForward.setStyleSheet("")
        self.pushButtonForward.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/Downloads/Custom-Icon-Design-Flatastic-1-Forward.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonForward.setIcon(icon2)
        self.pushButtonForward.setIconSize(QtCore.QSize(100, 24))
        self.pushButtonForward.setFlat(True)
        self.pushButtonForward.setObjectName("pushButtonForward")
        self.horizontalLayout.addWidget(self.pushButtonForward)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WEB"))
        self.pushButtonBack.setToolTip(_translate("Form", "Precedente"))
        self.pushButtonReload.setToolTip(_translate("Form", "Actualizar"))
        self.pushButtonForward.setToolTip(_translate("Form", "Seguinte"))


from PyQt5 import QtWebEngineWidgets
