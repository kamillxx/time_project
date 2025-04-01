from PyQt5 import QtWidgets, QtCore,QtGui
import calendar



class Window_1(QtWidgets.QWidget):
    def __init__(self, main_w, p,e):
        super().__init__(main_w)
        self.lay_1 = QtWidgets.QHBoxLayout(self)

        self.ev=e
        self.prs=p

        self.bouton_projects = QtWidgets.QPushButton("Проекты")
        self.bouton_projects.setObjectName("mainButton")
        self.bouton_projects.setFixedSize(200, 200)
        self.bouton_calendar = QtWidgets.QPushButton("Календарь", )
        self.bouton_calendar.setObjectName("mainButton")
        self.bouton_calendar .setFixedSize(200, 200)

        self.__apply__styles()

        self.lay_1.addWidget(self.bouton_projects)
        self.lay_1.addWidget(self.bouton_calendar)
        #
        # self.setStyleSheet("""
        #             QPushButton {
        #                 background-color: rgb(63, 57, 158);
        #                 color: white;
        #                 border-radius: 8px;
        #                 font-family: Calibri;
        #                 font-size: 25px;
        #                 font-weight: bold;
        #             }
        #             QPushButton:hover {
        #                 background-color: #153662;
        #             }
        #         """)

        self.bouton_projects.clicked.connect(lambda: main_w.w.setCurrentWidget(main_w.w_2))
        self.bouton_calendar.clicked.connect(self.open_calendar_window)


    def open_calendar_window(self):
        self.w=calendar.Window_task(self.prs, self.ev)
        self.w.show()


    def __apply__styles(self):
        with open("styles.css", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())
