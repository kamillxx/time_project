from PyQt5 import QtWidgets, uic # создание виджетов , объектов (кнопки, надписи)
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel  #QApp - создание приложения ; QMain - создание окна
# приложение может содержать несколько открытых окон
from PyQt5.QtWidgets import QCalendarWidget

import sys

def osn_f(): # основная функция вызывается каждый раз при создании проекта
    app = QApplication(sys.argv)
    window = QMainWindow()

    # window.setWindowTitle('New') # название, надпись для окна
    # window.setGeometry(400, 500, 400,250) # смещение окна (первые два парметра: смещение вправо на..., смещение по координате Y), ширина высота
    #
    # text=QLabel('Задачи', window)
    uic.loadUi('untitled.ui', window)


    window.show() # вызов окна
    sys.exit(app.exec_()) # коректный выход из приложения

if __name__ == '__main__':
    osn_f()

# print(__name__)





