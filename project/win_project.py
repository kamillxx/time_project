from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTabWidget, QListWidget, QVBoxLayout, QListWidgetItem, QCheckBox,QComboBox

import infprojects
import json
import edit_tasks_in_project
import os


class Window_task(QtWidgets.QWidget):
    def __init__(self, main_w, p):
        super().__init__()
        self.setGeometry(300,100,600,800)
        self.setWindowTitle('Task Planner')
        self.setWindowIcon(QtGui.QIcon('img.ico'))
        self.lay_2_vertical=QtWidgets.QVBoxLayout(self)
        self.lay_2_vertical.setObjectName("tasksWindow")

        if p is None:
            self.project = infprojects.Project('')
        else:
            self.project = p


        self.lay_h_3= QtWidgets.QHBoxLayout()
        self.lay_h_3.setSpacing(5)
        spacerItem_1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lay_h_3.addWidget(QtWidgets.QLabel('Название проекта:'))
        self.lay_h_3.addItem(spacerItem_1)
        self.lay_h_3.addWidget(QtWidgets.QLabel('Дата выполнения:'))

        self.hor_Layout_2 = QtWidgets.QHBoxLayout()
        self.hor_Layout_2.setSpacing(5)
        self.name_p=QtWidgets.QLineEdit(self.project.name_project)
        self.project_date = QtWidgets.QDateEdit(self.project.date)
        self.project_date.setCalendarPopup(True)
        self.project_date.setDisplayFormat("dd.MM.yyyy")


        self.hor_Layout_2.addWidget(self.name_p)
        self.hor_Layout_2.addWidget(self.project_date)

        self.image_task=QListWidget()

        self.hor_Layout_1 = QtWidgets.QHBoxLayout()

        self.bn_3 = QtWidgets.QPushButton('save')
        self.bn_3.setGeometry(30, 30, 40, 40)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bn_2 = QtWidgets.QPushButton('+')
        self.bn_2.setGeometry(30, 30, 40, 40)

        self.hor_Layout_1.addWidget(self.bn_3)
        self.hor_Layout_1.addItem(spacerItem)
        self.hor_Layout_1.addWidget(self.bn_2)

        self.__apply__styles()

        self.lay_2_vertical.addLayout(self.lay_h_3)
        self.lay_2_vertical.addLayout(self.hor_Layout_2)
        self.lay_2_vertical.addWidget(self.image_task)
        self.lay_2_vertical.addLayout(self.hor_Layout_1)

        self.last_win=main_w
        self.project_date.dateChanged.connect(self.save_project_date)
        self.bn_3.clicked.connect(self.save_project)
        self.bn_2.clicked.connect(self.new_task)

        self.update_list()



    def update_list(self):
        self.image_task.clear()

        sorted_tasks=sorted(self.project.tasks,
                            key= lambda x: (x.is_done, not x.priority ))

        for i in sorted_tasks:
            s=QtWidgets.QWidget()
            s.setProperty("class","task-item")
            d=QtWidgets.QHBoxLayout()

            check_mark = QCheckBox()
            check_mark.setChecked(i.is_done)
            check_mark.raise_()
            l = check_mark.isChecked()

            pushbottom_open = QtWidgets.QPushButton(i.name_task)
            pushbottom_open.setObjectName("openButton")
            deadline_label = QtWidgets.QLabel(i.date.toString("dd.MM.yyyy"))
            priority_label = QtWidgets.QLabel("высокий !" if i.priority==1 else "низкий")
            pushbottom_close = QtWidgets.QPushButton('Удалить')

            if i.priority==1:
                priority_label.setProperty("class", "high-priority ")
            else:
                priority_label.setProperty("class", "low-priority ")

            if i.is_done:
                pushbottom_open.setProperty("class", "completed-task")
                deadline_label.setProperty("class", "completed-task")
                pushbottom_close.setProperty("class", "completed-task")
                priority_label.setProperty("class", "completed-task")


            d.addWidget(check_mark)
            d.addWidget(pushbottom_open)
            d.addWidget(deadline_label)
            d.addWidget(priority_label)
            d.addWidget(pushbottom_close)

            check_mark.stateChanged.connect(lambda state, t=i: self.change_status(t))
            pushbottom_close.clicked.connect(lambda g, h=i: self.delete_task(h) )
            pushbottom_open.clicked.connect(lambda g, h=i: self.open_task(h))


            s.setLayout(d)
            u=QListWidgetItem(self.image_task)
            u.setSizeHint(s.sizeHint())
            self.image_task.addItem(u)
            self.image_task.setItemWidget(u, s)

    def open_task(self, t):
        self.w_t=edit_tasks_in_project.Window_new_task(self,t)
        self.w_t.show()


    def delete_task(self, t):
        self.project.tasks.remove(t)
        self.update_list()

    def new_task(self):
        self.w_t = edit_tasks_in_project.Window_new_task(self, None)
        self.w_t.show()

    def save_project(self):
        self.project.rename_project(self.name_p.text())
        if self.project not in self.last_win.projects:
            self.last_win.projects.append(self.project)
        self.last_win.update_list()
        self.last_win.save_json()

        self.close()

    def change_status(self, tt):
        tt.change_status_1()
        self.update_list()
        self.last_win.save_json()
        # self.save_project()

    def change_priority(self, task, priority):
        task.change_priority_1(priority)
        self.update_list()
        self.last_win.save_json()

    def save_project_date(self, new_date):
        self.project.change_time(
            new_date.day(),
            new_date.month(),
            new_date.year()
        )
        self.last_win.save_json()

    def __apply__styles(self):
        with open("styles.css", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())
    # добавить измениния в файл json
