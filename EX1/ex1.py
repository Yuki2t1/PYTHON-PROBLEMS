from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem
def permiers(x):
    ok=True
    i=2
    while not(i>x//2 and ok):
        if(x%2!=0):
            i+=1
        else:
            ok=False
        return(ok)

def test():
    l1=f.l1.text()
    num=int(l1)
    msg=""
    if(num<10):
        QMessageBox.critical(f,"Alert","veuillez utiliser un nombre superieur a 10")
    else:
        if(permiers(num)):
            msg="nombre premier circulaire"
        else:
            msg="pas un nombre premier circulaire"
    f.l2.setText(msg)
def reset():
    
    f.l1.clear()
app = QApplication([])
f = loadUi("ex1.ui")
f.show()

# Connect the button's click event to the function
f.bt1.clicked.connect(test)
f.bt2.clicked.connect(reset)
app.exec_()
