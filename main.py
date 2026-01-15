import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QListWidget)










app = QApplication([])
main_win = QWidget()
main_win.resize(700, 400)
main_win.setWindowTitle('Список дел')
main_win.show()

button1 = QPushButton('удалить все')
button2 = QPushButton('удалить все')
button6 = QPushButton('удалить выбр. заметку')
button7 = QPushButton('удалить выбр. заметку')
button3 = QPushButton('Переместить в (сделанное)')
button4 = QPushButton('Переместить в (список дел)')
button5 = QPushButton('добавить')
New_task_text = QLineEdit()
spisok1 = QLabel('сделано')
spisok2 = QLabel('cписок дел')
add = QLabel('новое дело')
listLeft = QListWidget()
listRight = QListWidget()

v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
main_line = QHBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

# Левый столбец
v_line1.addWidget(spisok2)
v_line1.addWidget(listLeft)
v_line1.addWidget(button1)
v_line1.addWidget(button6)


v_line2.addWidget(spisok1)
v_line2.addWidget(listRight)
v_line2.addWidget(button2)
v_line2.addWidget(button7)


h_line1.addWidget(add)
h_line1.addWidget(New_task_text)
h_line1.addWidget(button5)
h_line2.addWidget(button3)
h_line2.addWidget(button4)

v_line3.addLayout(h_line1)
v_line3.addLayout(h_line2)


main_line.addLayout(v_line1)
main_line.addLayout(v_line3)  # ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad ddblad
main_line.addLayout(v_line2)

main_win.setLayout(main_line)
app.exec_()

