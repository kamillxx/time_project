from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QTabWidget, QListWidget, QVBoxLayout, QListWidgetItem
import json
import infprojects, event



class Window_task(QtWidgets.QWidget):
    def __init__(self, projects, e):
        super().__init__()
        self.setGeometry(300, 100, 600, 800)
        self.setWindowTitle('Task Planner')
        self.setWindowIcon(QtGui.QIcon('img.ico'))

        self.lay=QtWidgets.QVBoxLayout(self)

        self.b_back=QtWidgets.QPushButton('back')
        self.b_plus=QtWidgets.QPushButton('+')
        self.calendar_1=QtWidgets.QCalendarWidget()
        self.list_p_t=QtWidgets.QListWidget()

        self.__apply__styles()

        self.lay.addWidget(self.calendar_1)
        self.lay.addWidget(self.list_p_t)
        self.lay.addWidget(self.b_back)
        self.lay.addWidget(self.b_plus)

        self.p=projects
        self.event=e

        self.b_back.clicked.connect(self.close)
        self.b_plus.clicked.connect(self.create_event)
        self.calendar_1.selectionChanged.connect(self.new_date)

        self.setLayout(self.lay)

        self.new_date()

    def save_json_e(self):
        with open('json_event.json', 'w', encoding='utf-8') as file:
            json.dump([e.dictionary() for e in self.event], file, indent=4)

    def new_date(self):
        self.date_1=self.calendar_1.selectedDate()
        self.list_p_t.clear()
        for i in self.event:
            if i.date==self.date_1:
                s=QtWidgets.QWidget()
                d=QtWidgets.QHBoxLayout()

                label_type = QtWidgets.QLabel("Событие")
                pushbottom_open=QtWidgets.QPushButton(i.name_event)
                pushbottom_open.setObjectName("openButton")
                pushbottom_close = QtWidgets.QPushButton('удалить')

                d.addWidget(label_type)
                d.addWidget(pushbottom_open)
                d.addWidget(pushbottom_close)

                pushbottom_open.clicked.connect(lambda g, h=i: self.open_event(h))
                pushbottom_close.clicked.connect(lambda g, h=i: self.delete_event(h) )

                s.setLayout(d)
                u=QListWidgetItem(self.list_p_t)
                u.setSizeHint(s.sizeHint())
                self.list_p_t.addItem(u)
                self.list_p_t.setItemWidget(u, s)

        for i in self.p:
            if i.date == self.date_1:
                s = QtWidgets.QWidget()
                d = QtWidgets.QHBoxLayout()

                label_type = QtWidgets.QLabel("Проект")
                label_name = QtWidgets.QLabel(i.name_project)

                d.addWidget(label_type)
                d.addWidget(label_name)

                s.setLayout(d)
                u = QListWidgetItem(self.list_p_t)
                u.setSizeHint(s.sizeHint())
                self.list_p_t.addItem(u)
                self.list_p_t.setItemWidget(u, s)

        for i in self.p:
            for t in i.tasks:
                if t.date == self.date_1:
                    s = QtWidgets.QWidget()
                    d = QtWidgets.QHBoxLayout()

                    label_type = QtWidgets.QLabel("Задача")
                    label_name = QtWidgets.QLabel(t.name_task)

                    d.addWidget(label_type)
                    d.addWidget(label_name)

                    s.setLayout(d)
                    u = QListWidgetItem(self.list_p_t)
                    u.setSizeHint(s.sizeHint())
                    self.list_p_t.addItem(u)
                    self.list_p_t.setItemWidget(u, s)


    def open_event(self,ee):
        self.w_with_project = event.Window_new_event(self, ee)
        self.w_with_project.show()

    def delete_event(self,ee):
        self.event.remove(ee)
        self.new_date()
        self.save_json_e()

    def create_event(self):
        self.event_1 = infprojects.Event('', self.date_1)
        self.w_with_project=event.Window_new_event(self, self.event_1)
        self.w_with_project.show()

    def __apply__styles(self):
        with open("styles.css", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())