
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 584)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 261, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 241, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 251, 20))
        self.label_4.setObjectName("label_4")
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setGeometry(QtCore.QRect(410, 120, 291, 41))
        self.searchbutton.setObjectName("searchbutton")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(20, 240, 441, 21))
        self.result.setObjectName("result")
        self.endresult = QtWidgets.QLabel(self.centralwidget)
        self.endresult.setGeometry(QtCore.QRect(20, 280, 751, 211))
        self.endresult.setText("")
        self.endresult.setTextFormat(QtCore.Qt.AutoText)
        self.endresult.setObjectName("endresult")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.add_functions()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Вычисление производной"))
        self.label.setText(_translate("mainWindow", "Вычисление производной"))
        self.label_2.setText(_translate("mainWindow", "Выражения"))
        self.label_3.setText(_translate("mainWindow", "( х**2 )"))
        self.label_4.setText(_translate("mainWindow", "(1/ ( l +x) )"))
        self.searchbutton.setText(_translate("mainWindow", "Старт"))
        self.result.setText(_translate("mainWindow", "Результат:"))

    def add_functions(self):
        self.searchbutton.clicked.connect(self.sortAB)

    def pr(self,f):
        # Функция для . вычисления производной
        def D(f):
        #Вложенная функция . Вычисляет
        # приближенное значение производной
        def df(x, dx=0.001):
            return (f(x + dx) - f(x)) / dx
        # Результат функции - производная
        return df

        # Первая функция для дифференцирования
        def f1(х):
            return х ** 2

        # Вторая функция для дифференцирования
        def f2(х):
            return 1 / (l + x)

        # Функция для отображения производной в
        # нескольких точках . Аргументы такие :
        # F - производная ( приближенная )
        # Nmax - количество т очек (минус один )
        # Xmax - правая граница по аргументу
        # dx - пр�ращение аргумента
        # f - производная ( аналитически)
        def show(F, Nmax, Xmax, dx, f):
            for i in range(Nmax + l):
                x = i * Xmax / Nmax  # Значение аргумента
            # Приближенное и точное значение произв одной
            print(F(x), F(x, dx), f(x), sep=" -> ")
        # Производная для первой функции
        Fl = D(fl)
        # Производная для второй функции
        F2 = D(f2)
        # Значения в разных точках
        # производной для первой функции ·
        рrint(" Производная ( х**2) ' =2х : ")
        show(Fl, 5, l, 0.01, lambda х: 2 * х)
        рrint(" Производная ( х**2) ' =2х : ")
        show(Fl, 5, l, 0.01, lambda х: 2 * х)

    if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
