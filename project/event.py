from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTabWidget, QListWidget, QVBoxLayout, QListWidgetItem
import infprojects
import json


class Window_new_event(QtWidgets.QDialog):
    def __init__(self, main_w, e):
        super().__init__(main_w)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setObjectName("EditTaskDialog")
        self.setModal(True)
        self.setWindowTitle('Task Planner')
        self.setWindowIcon(QtGui.QIcon('img.ico'))
        self.setGeometry(400,300,400,150)

        self.lay_2=QtWidgets.QVBoxLayout(self)

        self.event_1=e
        self.name_new_event=QtWidgets.QLineEdit(self.event_1.name_event)
        self.pushbotton_save=QtWidgets.QPushButton('b_save')

        self.__apply__styles()

        self.lay_2.addWidget(QtWidgets.QLabel('Название события:'))
        self.lay_2.addWidget(self.name_new_event)
        self.lay_2.addWidget(self.pushbotton_save)

        self.pushbotton_save.clicked.connect(self.save_event)
        self.last_win=main_w

        self.setLayout(self.lay_2)


    def save_event(self):
        self.event_1.rename_event(self.name_new_event.text())
        if self.event_1 not in self.last_win.event:
            self.last_win.event.append(self.event_1)
        self.last_win.new_date()
        self.last_win.save_json_e()

        self.close()

    def __apply__styles(self):
        with open("styles.css", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())


