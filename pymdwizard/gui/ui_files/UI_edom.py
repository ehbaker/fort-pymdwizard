# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edom.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fgdc_edom(object):
    def setupUi(self, fgdc_edom):
        fgdc_edom.setObjectName("fgdc_edom")
        fgdc_edom.resize(360, 134)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fgdc_edom)
        self.verticalLayout_2.setContentsMargins(0, 4, 0, 8)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(fgdc_edom)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fgdc_edomv = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_edomv.sizePolicy().hasHeightForWidth())
        self.fgdc_edomv.setSizePolicy(sizePolicy)
        self.fgdc_edomv.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_edomv.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_edomv.setToolTip("")
        self.fgdc_edomv.setStyleSheet("font: bold 10pt ;")
        self.fgdc_edomv.setClearButtonEnabled(False)
        self.fgdc_edomv.setObjectName("fgdc_edomv")
        self.horizontalLayout_8.addWidget(self.fgdc_edomv)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.label_21 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_21.setIndent(7)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fgdc_edomvd = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_edomvd.sizePolicy().hasHeightForWidth())
        self.fgdc_edomvd.setSizePolicy(sizePolicy)
        self.fgdc_edomvd.setObjectName("fgdc_edomvd")
        self.horizontalLayout_9.addWidget(self.fgdc_edomvd)
        self.label_25 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(15, 20))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_25.setIndent(0)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.label_22 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_22.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_22.setIndent(7)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fgdc_edomvds = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_edomvds.sizePolicy().hasHeightForWidth())
        self.fgdc_edomvds.setSizePolicy(sizePolicy)
        self.fgdc_edomvds.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_edomvds.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_edomvds.setObjectName("fgdc_edomvds")
        self.horizontalLayout_10.addWidget(self.fgdc_edomvds)
        self.label_26 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(15, 20))
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_26.setIndent(0)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(fgdc_edom)
        QtCore.QMetaObject.connectSlotsByName(fgdc_edom)

    def retranslateUi(self, fgdc_edom):
        _translate = QtCore.QCoreApplication.translate
        fgdc_edom.setWindowTitle(_translate("fgdc_edom", "Form"))
        self.label_21.setText(_translate("fgdc_edom", "Definition of this Value"))
        self.label_25.setToolTip(_translate("fgdc_edom", "Required"))
        self.label_25.setText(_translate("fgdc_edom", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#55aaff;\">*</span></p></body></html>"))
        self.label_22.setText(_translate("fgdc_edom", "Definition Source"))
        self.fgdc_edomvds.setToolTip(_translate("fgdc_edom", "Address -- an address line for the address.\n"
"Type: text\n"
"Domain: free text\n"
"Short Name: address"))
        self.fgdc_edomvds.setText(_translate("fgdc_edom", "Producer defined"))
        self.label_26.setToolTip(_translate("fgdc_edom", "Required"))
        self.label_26.setText(_translate("fgdc_edom", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#55aaff;\">*</span></p></body></html>"))

