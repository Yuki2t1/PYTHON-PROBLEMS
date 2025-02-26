from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem

def play():
    display=" "
    l1=f.l1.toPlainText()
    msg1="Interface graphique"
    msg2="ESP 32"
    msg3="Analyse de données"
    ch1=f.ch1.isChecked()
    ch2=f.ch2.isChecked()
    ch3=f.ch3.isChecked()
    if ch1:
        display+=msg1+" "
    if ch2:
        display+=msg2+" "
    if ch3:
        display+=msg3+" "
    f.l1.setText(display)
app = QApplication([])
f = loadUi("EX3.ui")
f.show()
# Connect the button's click event to the function
f.btn1.clicked.connect(play)
app.exec_()

