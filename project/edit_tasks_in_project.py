from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QTabWidget, QListWidget, QVBoxLayout, QListWidgetItem,  QComboBox
import infprojects
import json
import os


class Window_new_task(QtWidgets.QDialog):
    def __init__(self, main_w, t):
        super().__init__(main_w)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setObjectName("EditTaskDialog")
        self.setModal(True)
        self.setWindowTitle('Task Planner')
        self.setWindowIcon(QtGui.QIcon('img.ico'))
        self.setGeometry(400,300,400,250)


        self.lay_2=QtWidgets.QVBoxLayout(self)

        if t is None:
            self.task=infprojects.Task('')
        else:
            self.task=t

        self.name_new_task=QtWidgets.QLineEdit(self.task.name_task)
        self.task_date = QtWidgets.QDateEdit(self.task.date)
        self.task_date.setCalendarPopup(True)
        self.task_date.setDisplayFormat("dd.MM.yyyy")
        self.pushbotton_save=QtWidgets.QPushButton('b_save')
        self.combo = QComboBox()
        self.combo.addItems(self.task.PRIORITIES.values())
        self.combo.setCurrentIndex(self.task.priority)

        self.__apply__styles()

        self.lay_2.addWidget(QtWidgets.QLabel('Название задачи:'))
        self.lay_2.addWidget(self.name_new_task)
        self.lay_2.addWidget(QtWidgets.QLabel('Дата выполнения:'))
        self.lay_2.addWidget(self.task_date)
        self.lay_2.addWidget(QtWidgets.QLabel('Приоритет:'))
        self.lay_2.addWidget(self.combo)
        self.lay_2.addWidget(self.pushbotton_save)


        self.pushbotton_save.clicked.connect(self.save_task)
        self.combo.currentIndexChanged.connect(lambda state, t=self.task: self.change_priority(t, state))
        self.last_win=main_w

        self.setLayout(self.lay_2)

    def __apply__styles(self):
        with open("styles.css", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def save_task(self):
        self.task.rename_task(self.name_new_task.text())
        self.task.change_time(
            self.task_date.date().day(),
            self.task_date.date().month(),
            self.task_date.date().year()
        )
        if self.task not in self.last_win.project.tasks:
            self.last_win.project.add_task(self.task)
        self.last_win.update_list()

        self.accept()

    def change_priority(self, task, priority):
        task.change_priority_1(priority)
        self.save_task()


