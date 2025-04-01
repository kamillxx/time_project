self.bouton_plan = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_plan.sizePolicy().hasHeightForWidth())
        self.bouton_plan.setSizePolicy(sizePolicy)
        self.bouton_plan.setMinimumSize(QtCore.QSize(200,200))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bouton_plan.setFont(font)
        self.bouton_plan.setStyleSheet("background-color: rgb(63, 57, 158);\n"
                                      "\n"
                                      "color: rgb(222, 234, 255);")
        self.bouton_plan.setObjectName("bouton_plan")
        self.gridLayout.addWidget(self.bouton_plan, 1, 2, 1, 1)

self.bouton_chaos_control = QtWidgets.QPushButton(self.centralwidget)
sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.bouton_chaos_control.sizePolicy().hasHeightForWidth())
self.bouton_chaos_control.setSizePolicy(sizePolicy)
self.bouton_chaos_control.setMinimumSize(QtCore.QSize(200, 200))
font = QtGui.QFont()
font.setFamily("Calibri")
font.setPointSize(12)
self.bouton_chaos_control.setFont(font)
self.bouton_chaos_control.setStyleSheet("background-color: rgb(63, 57, 158);\n"
                                        "\n"
                                        "color: rgb(222, 234, 255);")
self.bouton_chaos_control.setObjectName("bouton_chaos_control")
self.gridLayout.addWidget(self.bouton_chaos_control, 3, 2, 1, 1)


spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 0, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 2, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 4, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 4, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 0, 1, 1)


self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.bouton_home = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_home.sizePolicy().hasHeightForWidth())
        self.bouton_home.setSizePolicy(sizePolicy)
        self.bouton_home.setMinimumSize(QtCore.QSize(40, 30))
        self.bouton_home.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bouton_home.setFont(font)
        self.bouton_home.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bouton_home.setObjectName("bouton_home")
        self.horizontalLayout.addWidget(self.bouton_home)

        self.bouton_search = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_search.sizePolicy().hasHeightForWidth())
        self.bouton_search.setSizePolicy(sizePolicy)
        self.bouton_search.setMinimumSize(QtCore.QSize(40, 30))
        self.bouton_search.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bouton_search.setFont(font)
        self.bouton_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bouton_search.setObjectName("bouton_search")
        self.horizontalLayout.addWidget(self.bouton_search)

        self.bouton_plus_task = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_plus_task.sizePolicy().hasHeightForWidth())
        self.bouton_plus_task.setSizePolicy(sizePolicy)
        self.bouton_plus_task.setMinimumSize(QtCore.QSize(40, 30))
        self.bouton_plus_task.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bouton_plus_task.setFont(font)
        self.bouton_plus_task.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bouton_plus_task.setObjectName("bouton_plus_task")
        self.horizontalLayout.addWidget(self.bouton_plus_task)

        self.bouton_notes = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_notes.sizePolicy().hasHeightForWidth())
        self.bouton_notes.setSizePolicy(sizePolicy)
        self.bouton_notes.setMinimumSize(QtCore.QSize(40, 30))
        self.bouton_notes.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bouton_notes.setFont(font)
        self.bouton_notes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bouton_notes.setObjectName("bouton_notes")
        self.horizontalLayout.addWidget(self.bouton_notes)

        self.bouton_archive = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouton_archive.sizePolicy().hasHeightForWidth())
        self.bouton_archive.setSizePolicy(sizePolicy)
        self.bouton_archive.setMinimumSize(QtCore.QSize(40, 30))
        self.bouton_archive.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bouton_archive.setFont(font)
        self.bouton_archive.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bouton_archive.setObjectName("bouton_archive")
        self.horizontalLayout.addWidget(self.bouton_archive)