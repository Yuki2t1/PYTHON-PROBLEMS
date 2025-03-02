from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem
#check if the number is first
def premier(x):
    ok=True
    i=2
    x=int(x)
    while not(i>x//2 and ok):
        if(x%2!=0):
            i+=1
        else:
            ok=False
        return(ok)

#checks if the first number equals the constarins


def verif(ch):
    i=0
    ok=False
    while i<len(ch) and ("1"<=ch[i]<="9") :
        i+=1
        ok=True
    return(ok and (ch[0]in["2","4","5","9"]))

#calculates the sum of all of the numbers multiplied by their own place in the string
def chances(ch):
    ch=str(ch)
    totalsum=0
    for i in range(len(ch)):
        index=int(ch[i])
        totalsum+=index*i
    print(totalsum)
    return(totalsum)

def play():
    l1=f.l1.text()
    l1=str(l1)
    chance=0
    msg=""
    if(l1==""or l1==" " ):
        QMessageBox.critical(f,"veuillez","saisir un nombre")
    if(verif(l1)==False):
        QMessageBox.critical(f,"veuillez","saisir un numéro de téléphone valide")
    else:
        total=chances(l1)
        if (premier(total)==True):
            msg=("Félicitation vous avez gagné")
        if(premier(total)==False):
            msg=("Désolé,vous avez pas gagné")
    f.l2.setText(msg)
app = QApplication([])
def reset():
     l1=f.l1.clear()
     l1=""
f = loadUi("ex2.ui")
f.show()

# Connect the button's click event to the function
f.btn1.clicked.connect(play)
f.btn2.clicked.connect(reset)
app.exec_()

#CODED BY AYOUB
