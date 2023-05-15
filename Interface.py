# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfaceGsNjYq.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


import MyIcon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(586, 469)
        icon = QIcon()
        icon.addFile(u":/Icon/BlueGreen/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"border-radius:25px;\n"
"border:2px solid #2596be;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#label_3{\n"
"background:transparent;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"#pushButton_10::hover,#pushButton_11::hover\n"
"{\n"
"background-color : lightgreen;\n"
"}\n"
"\n"
"#widget_4,#widget_2{\n"
"background-color: black;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.widget_8.setMinimumSize(QSize(300, 200))
        self.widget_8.setMaximumSize(QSize(900, 700))
        self.widget_8.setLayoutDirection(Qt.LeftToRight)
        self.widget_8.setAutoFillBackground(False)
        self.formLayout_3 = QFormLayout(self.widget_8)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(920, 700))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.label_3)


        self.gridLayout_3.addWidget(self.widget_8, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(15, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.frame_8 = QFrame(self.widget_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setLayoutDirection(Qt.LeftToRight)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_10 = QPushButton(self.frame_8)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(120, 60))
        self.pushButton_10.setMaximumSize(QSize(170, 60))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/BlueGreen/BlueGreen/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(120, 60))
        self.pushButton_11.setMaximumSize(QSize(170, 60))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/Icon/BlueGreen/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.pushButton_11)


        self.horizontalLayout_6.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.widget_4)


        self.verticalLayout_8.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JackCamera", None))
        self.label_3.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Detect Face", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Video", None))
    # retranslateUi

