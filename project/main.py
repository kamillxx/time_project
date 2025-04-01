from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import QTabWidget
import win_1, win_2
import json
import infprojects


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,100,600,800)
        self.setWindowTitle('Task Planner')
        self.setWindowIcon(QtGui.QIcon('img.ico'))
        self.events=[]
        self.projects = []
        self.download_json()


        self.w=QtWidgets.QStackedWidget(self)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.w)
        self.w_1=win_1.Window_1(self, self.projects, self.events)
        self.w_2=win_2.Window_2(self, self.projects)
        self.w.addWidget(self.w_1)
        self.w.addWidget(self.w_2)
        self.w.setCurrentWidget(self.w_1)



    def download_json(self):
        with open('json.json', 'r', encoding='utf-8') as file_2:
            f_1 = json.load(file_2)
            self.projects = [infprojects.Project.list_from_dictionary(pp) for pp in f_1]

        with open('json_event.json', 'r', encoding='utf-8') as file:
            f_1 = json.load(file)
            self.events = [infprojects.Event.list_from_dictionary(e) for e in f_1]





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open("styles.css", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())
    NewWindow = MainWindow()
    NewWindow.show()
    sys.exit(app.exec_())