from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTabWidget


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,200,500,700)

        self.w=QtWidgets.QStackedWidget(self)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.w)
        self.w_1=Window_1(self)
        self.w_2=Window_2(self)
        self.w.addWidget(self.w_1)
        self.w.addWidget(self.w_2)
        self.w.setCurrentWidget(self.w_2)


class Window_1(QtWidgets.QWidget):
    def __init__(self,main_w):
        super().__init__(main_w)
        self.lay=QtWidgets.QVBoxLayout(self)
        self.text=QtWidgets.QLabel('hello!')
        self.bn_1=QtWidgets.QPushButton('Print')
        self.bn_1.setGeometry(30,30,40,40)
        self.lay.addWidget(self.text)
        self.lay.addWidget(self.bn_1)
        self.bn_1.clicked.connect(lambda : main_w.w.setCurrentWidget(main_w.w_2))



class Window_2(QtWidgets.QWidget):
    def __init__(self, main_w):
        super().__init__(main_w)
        self.lay_2=QtWidgets.QVBoxLayout(self)
        self.text_1 = QtWidgets.QLabel('fdrec&')
        self.bn_2=QtWidgets.QPushButton('Back')
        self.bn_2.setGeometry(30, 30, 40, 40)
        self.lay_2.addWidget(self.text_1)
        self.lay_2.addWidget(self.bn_2)
        self.bn_2.clicked.connect(lambda: main_w.w.setCurrentWidget(main_w.w_1))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewWindow = MainWindow()
    NewWindow.show()
    sys.exit(app.exec_())