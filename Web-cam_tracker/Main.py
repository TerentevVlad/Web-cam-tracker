import sys
#Импорт интерфейся из файла
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,  QDesktopWidget
from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import cv2

import Controller

class MyWin(QtWidgets.QMainWindow):

    StartMouse = False
    cbH = False
    cbS = False
    cbV = False
    width_screen= None
    height_screen = None

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #получение размеров экрана
        q = QDesktopWidget().availableGeometry()
        self.width_screen = q.width()
        self.height_screen = q.height()

        # Здесь прописываем события нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.StartController)
        self.ui.pushButton_2.clicked.connect(self.defStartMouse)

        self.ui.checkBox.stateChanged.connect(self.canalH)
        self.ui.checkBox_2.stateChanged.connect(self.canalS)
        self.ui.checkBox_3.stateChanged.connect(self.canalV)

        self.ui.horizontalSlider.valueChanged[int].connect(self.sliderH_Value)
        self.ui.horizontalSlider_2.valueChanged[int].connect(self.sliderS_Value)
        self.ui.horizontalSlider_3.valueChanged[int].connect(self.sliderV_Value)



    #Функции событий

    #=====ЧЕКБОКСЫ============================
    def canalH(self, state):
        if state == Qt.Checked:
            self.cbH = True
        else:
            self.cbH = False
    def canalS(self, state):
        if state == Qt.Checked:
            self.cbS = True
        else:
            self.cbS = False
    def canalV(self, state):
        if state == Qt.Checked:
            self.cbV = True
        else:
            self.cbV = False
    #==========================================


    #=====СЛАЙДЕРЫ=============================
    def sliderH_Value(self, value):
        self.ui.label.setText(str(value))
    def sliderS_Value(self, value):
        self.ui.label_2.setText(str(value))
    def sliderV_Value(self, value):
        self.ui.label_3.setText(str(value))
    #==========================================

    def defStartMouse(self):
        if self.StartMouse:
            self.StartMouse = False
        else:
            self.StartMouse = True
    def StartController(self):
        while True:
            H = self.ui.horizontalSlider.value()
            S = self.ui.horizontalSlider_2.value()
            V = self.ui.horizontalSlider_3.value()

            Controller.ActivateController(H, S, V, self.cbH, self.cbS, self.cbV, self.StartMouse, self.height_screen,
                                          self.width_screen)
            key = cv2.waitKey(1)
            if key == 27:
                self.StartMouse = False
                Controller.destroyWindows()
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())