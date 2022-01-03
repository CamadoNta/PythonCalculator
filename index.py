import time
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from datetime import datetime

ui, _ = loadUiType("main.ui")


class MainApp(QMainWindow, ui):
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+"]
    text = ""
    numbers_list = []

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_ui()
        self.Handle_buttons()
        self.Handle_time()

    def fill_numbers_list(self):
        for i in range(0, 10):
            self.numbers_list.append(i)

    def Handle_ui(self):
        self.setWindowTitle("Mouhrach Choaib")
        self.setFixedSize(390, 683)

    def Handle_buttons(self):
        self.pushButton_equal.clicked.connect(self.Handle_equal)
        self.pushButton_0.clicked.connect(self.Handle_0)
        self.pushButton.clicked.connect(self.Handle_1)
        self.pushButton_2.clicked.connect(self.Handle_2)
        self.pushButton_3.clicked.connect(self.Handle_3)
        self.pushButton_4.clicked.connect(self.Handle_4)
        self.pushButton_5.clicked.connect(self.Handle_5)
        self.pushButton_6.clicked.connect(self.Handle_6)
        self.pushButton_7.clicked.connect(self.Handle_7)
        self.pushButton_8.clicked.connect(self.Handle_8)
        self.pushButton_9.clicked.connect(self.Handle_9)
        self.pushButton_point.clicked.connect(self.Handele_point)
        self.pushButton_14.clicked.connect(self.Handle_plus)
        self.pushButton_minus.clicked.connect(self.Handle_minus)
        self.pushButton_multiple.clicked.connect(self.Handle_multiple)
        self.pushButton_devide.clicked.connect(self.Handle_devide)
        self.pushButton_delete.clicked.connect(self.Handle_delete)
        self.pushButton_16.clicked.connect(self.Handle_clear)

        self.pushButton_exit.clicked.connect(self.Handle_exit)

    def Handle_0(self):
        self.Handele_numbers(0)

    def Handle_1(self):
        self.Handele_numbers(1)

    def Handle_2(self):
        self.Handele_numbers(2)

    def Handle_3(self):
        self.Handele_numbers(3)

    def Handle_4(self):
        self.Handele_numbers(4)

    def Handle_5(self):
        self.Handele_numbers(5)

    def Handle_6(self):
        self.Handele_numbers(6)

    def Handle_7(self):
        self.Handele_numbers(7)

    def Handle_8(self):
        self.Handele_numbers(9)

    def Handle_9(self):
        self.Handele_numbers(9)

    def Handele_numbers(self, num):
        self.lineEdit_3.setText("")
        if self.text != "0":
            self.text = self.text + str(num)
            self.lineEdit.setText(self.text)
        else:
            if num != 0:
                self.text = self.text + str(num)
                self.lineEdit.setText(self.text)

    def Handele_point(self):
        self.text = self.text + "."
        self.lineEdit.setText(self.text)

    def Handle_plus(self):
        self.text = str(self.text)
        if self.text != "" and self.text[-1] != "+":
            if self.text[-1] == "-" or self.text[-1] == "x":
                self.Handle_delete()
            self.text = self.text + "+"
            self.lineEdit.setText(self.text)

    def Handle_minus(self):
        self.text = str(self.text)
        if self.text != "" and self.text[-1] != "-":
            if self.text[-1] == "+":
                self.Handle_delete()
            self.text = self.text + "-"
            self.lineEdit.setText(self.text)

    def Handle_multiple(self):
        self.text = str(self.text)
        if self.text != "" and self.text[-1] != "x":
            if (
                self.text[-1] == "+" or self.text[-1] == "-" or self.text[-1] == "/"
            ) and self.text[-2] != "x":
                self.Handle_delete()
            self.text = self.text + "x"
            self.lineEdit.setText(self.text)
            if self.text[-2:] == "-x":
                for i in range(2):
                    self.Handle_delete()

    def Handle_devide(self):
        self.text = str(self.text)
        if self.text != "" and self.text[-1] != "/":
            if (
                self.text[-1] == "+" or self.text[-1] == "-" or self.text[-1] == "*"
            ) and self.text[-2] != "/":
                self.Handle_delete()
            self.text = self.text + "/"
            self.lineEdit.setText(self.text)
            if self.text[-2:] == "-/":
                for i in range(2):
                    self.Handle_delete()

    def Handle_delete(self):
        if self.text != "":
            self.text = str(self.text)[:-1]
            self.lineEdit.setText(self.text)

    def Handle_clear(self):
        self.text = ""
        self.lineEdit.setText(self.text)
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")

    def Handle_exit(self):
        exit()

    def Handle_equal(self):
        self.lineEdit_3.setText("")
        try:
            self.text = str(self.text).replace("x", "*")
            if self.text[0] != "0":
                final_form = eval(self.text, {"__builtins__": None})
                self.lineEdit_2.setText(str(final_form))
            else:
                self.text = self.text[1:]
                final_form = eval(self.text, {"__builtins__": None})
                self.lineEdit_2.setText(str(final_form))
        except ZeroDivisionError:
            self.lineEdit_3.setText("division by zero is not possible")
        except Exception:
            self.lineEdit_3.setText("Error")

    def Handle_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        QApplication.processEvents()
        self.lineEdit_time.setText(current_time)
        time.sleep(1)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
