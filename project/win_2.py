from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QTabWidget, QListWidget, QVBoxLayout, QListWidgetItem, QCheckBox, QComboBox
import infprojects
import json
import win_project


class Window_2(QtWidgets.QWidget):
    def __init__(self, main_w, p):
        super().__init__(main_w)
        self.lay_2=QtWidgets.QVBoxLayout(self)
        self.lay_2.setObjectName("projectsWindow")
        self.lay_3=QtWidgets.QHBoxLayout(self)

        self.bn_2=QtWidgets.QPushButton('<-')


        self.b_new_p= QtWidgets.QPushButton('+')

        self.lay_3.addWidget(self.bn_2)
        self.lay_3.addWidget(self.b_new_p)

        self.image_project=QListWidget()

        self.__apply__styles()

        self.lay_2.addLayout(self.lay_3)
        self.lay_2.addWidget(self.image_project)

        self.b_new_p.clicked.connect(self.create_project)
        self.bn_2.clicked.connect (lambda: main_w.w.setCurrentWidget(main_w.w_1))

        self.projects=p
        self.update_list()


    def save_json(self):
        with open('json.json', 'w', encoding='utf-8') as file_1:
            json.dump([p.dictionary() for p in self.projects], file_1,indent=4)

    def update_list(self):
        self.image_project.clear()

        sorted_projects = sorted(self.projects,
                              key=lambda x: (x.is_done, not x.priority))

        for i in sorted_projects:
            s=QtWidgets.QWidget()
            d=QtWidgets.QHBoxLayout()


            pushbottom_open=QtWidgets.QPushButton(i.name_project)
            pushbottom_open.setObjectName("openButton")
            pushbottom_close = QtWidgets.QPushButton('удалить')
            check_mark=QCheckBox()
            check_mark.setChecked(i.is_done)
            check_mark.raise_()
            l=check_mark.isChecked()
            combo=QComboBox()
            combo.addItems(i.PRIORITIES.values())
            combo.setCurrentIndex(i.priority)
            deadline_label=QtWidgets.QLabel(i.date.toString("dd.MM.yyyy"))

            if i.priority==1:
                pushbottom_open.setStyleSheet("color: #d32f2f;")
            else:
                pushbottom_open.setStyleSheet("color: #388e3c;")

            if i.is_done:
                pushbottom_open.setProperty("class", "completed-task")
                deadline_label.setProperty("class", "completed-task")
                pushbottom_close.setProperty("class", "completed-task")
                combo.setProperty("class", "completed-task")

            d.addWidget(check_mark)
            d.addWidget(pushbottom_open)
            d.addWidget(deadline_label)
            d.addWidget(combo)
            d.addWidget(pushbottom_close)

            combo.currentIndexChanged.connect(lambda state, p=i: self.change_priority(p, state))
            check_mark.stateChanged.connect(lambda state, p=i: self.change_status(p))
            pushbottom_open.clicked.connect(lambda g, h=i: self.open_project(h))
            pushbottom_close.clicked.connect(lambda g, h=i: self.delete_project(h) )

            s.setLayout(d)
            u=QListWidgetItem(self.image_project)
            u.setSizeHint(s.sizeHint())
            self.image_project.addItem(u)
            self.image_project.setItemWidget(u, s)


    def open_project(self, p):
        self.w_with_project=win_project.Window_task(self, p)
        self.w_with_project.show()



    def delete_project(self, p):
        self.projects.remove(p)
        self.update_list()
        self.save_json()

    def create_project(self):
        self.w_with_project=win_project.Window_task(self, None)
        self.w_with_project.show()

    def change_status(self, pr):
        self.projects[self.projects.index(pr)].change_status_1()
        self.update_list()
        self.save_json()

    def change_priority(self, project, priority):
        self.projects[self.projects.index(project)].change_priority_1(priority)
        self.save_json()
        self.update_list()

    def __apply__styles(self):
        with open("styles.css", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

        # добавить измениния в файл json
