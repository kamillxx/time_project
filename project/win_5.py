# from PyQt5 import QtWidgets,QtCore
#
#
#
#
# class Window_1(QtWidgets.QWidget):
#     def __init__(self,main_w):
#         super().__init__(main_w)
#         self.lay_1=QtWidgets.QVBoxLayout(self)
#         self.centralwidget = QtWidgets.QWidget()
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout.setContentsMargins(5, 5, 5, 5)
#         self.verticalLayout.setSpacing(5)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.gridLayout = QtWidgets.QGridLayout()
#         self.gridLayout.setObjectName("gridLayout")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
#         self.pushButton.setSizePolicy(sizePolicy)
#         self.pushButton.setMinimumSize(QtCore.QSize(90, 90))
#         self.pushButton.setObjectName("pushButton")
#         self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
#         self.pushButton_2.setSizePolicy(sizePolicy)
#         self.pushButton_2.setMinimumSize(QtCore.QSize(90, 90))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.gridLayout.addWidget(self.pushButton_2, 1, 4, 1, 1)
#         spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
#         spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.gridLayout.addItem(spacerItem1, 3, 6, 1, 1)
#         spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
#         spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.gridLayout.addItem(spacerItem3, 1, 6, 1, 1)
#         spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
#         spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.gridLayout.addItem(spacerItem5, 3, 3, 1, 1)
#         spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
#         spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.gridLayout.addItem(spacerItem7, 0, 4, 1, 1)
#         spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.gridLayout.addItem(spacerItem8, 2, 4, 1, 1)
#         spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.gridLayout.addItem(spacerItem9, 4, 4, 1, 1)
#         spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.gridLayout.addItem(spacerItem10, 4, 2, 1, 1)
#         spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.gridLayout.addItem(spacerItem11, 1, 0, 1, 1)
#         self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
#         self.pushButton_5.setSizePolicy(sizePolicy)
#         self.pushButton_5.setMinimumSize(QtCore.QSize(90, 90))
#         self.pushButton_5.setObjectName("pushButton_5")
#         self.gridLayout.addWidget(self.pushButton_5, 3, 2, 1, 1)
#         self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
#         self.pushButton_4.setSizePolicy(sizePolicy)
#         self.pushButton_4.setMinimumSize(QtCore.QSize(90, 90))
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.gridLayout.addWidget(self.pushButton_4, 3, 4, 1, 1)
#         self.verticalLayout.addLayout(self.gridLayout)
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
#         self.horizontalLayout.setSpacing(0)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
#         self.pushButton_14.setSizePolicy(sizePolicy)
#         self.pushButton_14.setMinimumSize(QtCore.QSize(40, 30))
#         self.pushButton_14.setMaximumSize(QtCore.QSize(100, 30))
#         self.pushButton_14.setObjectName("pushButton_14")
#         self.horizontalLayout.addWidget(self.pushButton_14)
#         self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
#         self.pushButton_6.setSizePolicy(sizePolicy)
#         self.pushButton_6.setMinimumSize(QtCore.QSize(40, 30))
#         self.pushButton_6.setMaximumSize(QtCore.QSize(100, 30))
#         self.pushButton_6.setObjectName("pushButton_6")
#         self.horizontalLayout.addWidget(self.pushButton_6)
#         self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
#         self.pushButton_13.setSizePolicy(sizePolicy)
#         self.pushButton_13.setMinimumSize(QtCore.QSize(40, 30))
#         self.pushButton_13.setMaximumSize(QtCore.QSize(100, 30))
#         self.pushButton_13.setObjectName("pushButton_13")
#         self.horizontalLayout.addWidget(self.pushButton_13)
#         self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
#         self.pushButton_7.setSizePolicy(sizePolicy)
#         self.pushButton_7.setMinimumSize(QtCore.QSize(40, 30))
#         self.pushButton_7.setMaximumSize(QtCore.QSize(100, 30))
#         self.pushButton_7.setObjectName("pushButton_7")
#         self.horizontalLayout.addWidget(self.pushButton_7)
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
#         self.pushButton_3.setSizePolicy(sizePolicy)
#         self.pushButton_3.setMinimumSize(QtCore.QSize(40, 30))
#         self.pushButton_3.setMaximumSize(QtCore.QSize(100, 30))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.horizontalLayout.addWidget(self.pushButton_3)
#         self.verticalLayout.addLayout(self.horizontalLayout)
#         self.lay_1.addWidget(self.centralwidget)
#
#         self.pushButton_2.clicked.connect(lambda: main_w.w.setCurrentWidget(main_w.w_2))
#
#         self.retranslateUi()
#
#     def retranslateUi(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.pushButton.setText(_translate("MainWindow", "План на день"))
#         self.pushButton_2.setText(_translate("MainWindow", "Проекты"))
#         self.pushButton_5.setText(_translate("MainWindow", "Хаос контроль"))
#         self.pushButton_4.setText(_translate("MainWindow", "Календарь"))
#         self.pushButton_14.setText(_translate("MainWindow", "Дом"))
#         self.pushButton_6.setText(_translate("MainWindow", "Поиск"))
#         self.pushButton_13.setText(_translate("MainWindow", "+"))
#         self.pushButton_7.setText(_translate("MainWindow", "Заметки"))
#         self.pushButton_3.setText(_translate("MainWindow", "Архив"))
