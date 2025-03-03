from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem


def premier(x):
    x=int(x)
    i=2
    while(i<=x//2 and x%i!=0):
        i+=1
    return(i>x//2 and x>1)

def premier_circ(x):
    ok=False
    if (premier(x)):
        nb=1
        ok=True
        ch=str(x)
        while nb<len(ch) and ok:
            ch=ch[1:]+ch[0]
            x=int(ch)
            print("x = ",x)
            ok=premier(x)
            if ok:
                nb+=1
    return(ok)

def puissance(x,y):
    p=1
    for i in range(y):
        p*=x
    return(p)

def primaire(x):
    x=int(x)
    if premier(x):
        ok=True
    else:
        ok=False
        counter=2
        
        while counter<=x and not ok:
            i=1
            while puissance(counter,i)<x:
                i+=1
            if puissance(counter,i)==x:
                ok=True
            else:
                counter+=1
            while not(premier(counter)):
                counter+=1

    return(ok)

def premier_equilibre(x):
    x=int(x)
    front=x+1
    back=x-1
    while premier(front)==False:
        front+=1
    while premier(back)==False:
        back-=1
    ok=(front+back)//2
    return(ok==x)

def  tester():
    ch1=f.ch1.isChecked()
    ch2=f.ch2.isChecked()
    ch3=f.ch3.isChecked()
    msg=""
        
    if f.l1.text()=="" or int(f.l1.text())<=1 or f.l1.text().isdecimal==False:
        QMessageBox.critical(f,"error","veuillez saisir un entier superieur a 1")
    if ch1==False and ch2==False  and ch3==False:
        QMessageBox.critical(f,"error","veuillez selectioner un choix")
    else:
        x=f.l1.text()
        if ch1==True:
            if premier_circ(f.l1.text())==True:
                 msg+=(x+'est premier circulaire \n')
            elif(premier_circ(f.l1.text())==False):
                msg+=(x+' pas premier circulaire \n ')
        
        if ch2==True:
            if primaire(f.l1.text())==True:
                msg+=(x+' est un nombre primair  \n ')
            elif(primaire(f.l1.text())==False):
                msg+=(x+' pas primair  \n ')
                
        if ch3==True:
            if  premier_equilibre(f.l1.text())==True:
                msg+=(x+'est un nombre Equilibré  ')
            elif( premier_equilibre(f.l1.text())==False):
                msg+=(x+'pas un nombre Equilibré  ')
        f.l2.setText(msg)         
def reset():
    f.l1.clear()
    f.l2.clear()
    f.ch1.setChecked(False)
    f.ch2.setChecked(False)
    f.ch3.setChecked(False)
app = QApplication([])
f = loadUi("ex1.ui")
f.show()
f.btn1.clicked.connect(tester)
f.btn2.clicked.connect(reset)
app.exec_()
