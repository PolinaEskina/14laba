from PyQt5 import QtWidgets, QtCore
import sys


app = QtWidgets.QApplication([])

win = QtWidgets.QMainWindow()
win.show()
win.setWindowTitle("Калькулятор")
win.setGeometry(0, 0, 740, 360)
win.setMinimumSize(740, 360)
win.setMaximumSize(740, 360)

digits_board = QtWidgets.QWidget(win)
ops_board = QtWidgets.QWidget(win)

digits_layout = QtWidgets.QGridLayout(digits_board)
ops_layout = QtWidgets.QGridLayout(ops_board)
digits_board.setGeometry(QtCore.QRect(0, 60, 400, 300))
ops_board.setGeometry(QtCore.QRect(440, 60, 300, 300))

output = QtWidgets.QLineEdit(win)
output.setReadOnly(True)
output.setGeometry(QtCore.QRect(0,0,740, 60))


def put_symbol(str):
    output.setText(output.text() + str)

def evaluate():
    try:
        statement = output.text()
        output.clear()
        i = str(eval(statement))
        output.setText(i)
    except ZeroDivisionError:
        QtWidgets.QMessageBox.warning(win, win.windowTitle(), "Нельзя делить на ноль!")
    except SyntaxError:
        QtWidgets.QMessageBox.warning(win, win.windowTitle(), "Некорректное выражение задано!")




digits_list = []
ops_list = []

ops_list.append(QtWidgets.QPushButton(win, text="+"))
ops_list.append(QtWidgets.QPushButton(win, text="-"))
ops_list.append(QtWidgets.QPushButton(win, text="*"))
ops_list.append(QtWidgets.QPushButton(win, text="/"))
ops_list.append(QtWidgets.QPushButton(win, text="E"))
ops_list.append(QtWidgets.QPushButton(win, text="("))
ops_list.append(QtWidgets.QPushButton(win, text=")"))
ops_list.append(QtWidgets.QPushButton(win, text="="))



for i in range(10):
    digits_list.append(QtWidgets.QPushButton(win, text=str( (i+1) % 10)))

    # https://stackoverflow.com/questions/6784084/
    digits_list[i].clicked.connect(lambda _, x=str((i+1)%10): put_symbol(x))

digits_list.append(QtWidgets.QPushButton(win, text=str(".")))
digits_list[10].clicked.connect(lambda _, x=".": put_symbol(x))

for i in range(11):
    digits_layout.addWidget(digits_list[i], i // 3, i  % 3)
    digits_list[i].show()

for i in range(8):
    ops_layout.addWidget(ops_list[i], i % 4, i // 4)
    if i != 7:
        ops_list[i].clicked.connect(lambda _, x=ops_list[i].text(): put_symbol(x))
    ops_list[i].show()


ops_list[4].clicked.connect(lambda: output.clear())
ops_list[7].clicked.connect(evaluate)


digits_board.show()
ops_board.show()
output.show()
sys.exit(app.exec_())
