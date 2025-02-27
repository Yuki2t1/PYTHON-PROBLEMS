from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from numpy import array
from random import *
c=dict(
    identifiant=str,ntel=int,ville=str,genre=str,etat=str
    )

def remplir(T2):
    for i in range(6):
        T2[i]=randint(1,9)


#tests if the name of the user is alphanum and its first letter is upper case
def alphanum(ch):
    i=1
    while i<len(ch) and ('A'<=ch[i].upper()<='Z' or('0'<=ch[i]<='9')):
        i=i+1
    return (i==len(ch) and 'A'<=ch[0]<='Z'  and len(ch)<=10)


#calculates the sum of the toatal numbers and makes sure to keep it under 10 if it reaches 10 or 11
def cc(val):
    s=0
    val=str(val)
    for i in range(len(val)):
            s+=int(val[i])
    print(s)
    if(s>=10):
        res=str(s)
        s=0
        for i in range(len(res)):
            s+=int(res[i])

    return(s)

#checks if the sum from the previous function is inside the list T2 and return a bool
def sum(T2,s):
    ok=False
    for i in range(6):
        if (s==T2[i]):
            ok=True
            print("test passed")
    return ok


#this function calls out the erorrs and passes in the correct values inside the dict
def play():
    T1=array([int]*6)
    counter=0

    if not (alphanum(f.l1.text())):
        QMessageBox.critical(f,"Ereurr"," identifiant invalide")
    else:
        if(f.l1.text()==""):
                    QMessageBox.critical(f,"Ereurr ","veuillez saisir tous les information")
        if(f.l1.text()!=""):
            c["identifiant"]=f.l1.text()

            
        if not ((f.l2.text().isdecimal() )):
            QMessageBox.critical(f,"Ereurr ","nombre telephone est invalide")
        if(len(f.l2.text())!=8 ):
            QMessageBox.critical(f,"Ereurr ","nombre telephone est invalide")
        if(f.l2.text()==""):
            QMessageBox.critical(f,"Ereurr ","nombre telephone est invalide")
        if(f.l2.text()!="" ) :
                c["ntel"]=f.l2.text()
                
        if(f.rd1.isChecked()):
            c["genre"]="homme"
        if(f.rd2.isChecked()):
            c["genre"]="femme"
        
        
        if(f.comboBox.currentText()=="--Choix--"):
            QMessageBox.critical(f,"Ereurr","selctioner un option valide")
        if(f.comboBox.currentText()!="--Choix--"):
            c["ville"]=f.comboBox.currentText()
     
        
        if(f.checkbox1.isChecked()):
            c["etat"]="inscrit"
        else:
            c["etat"]="pas inscrit"
        if(c["identifiant"]!="" and c["ntel"]!=""and c["genre"]!="" and c["ville"]!="" and c["etat"]!=""):
            f.l3.setText(c["identifiant"]+" "+c["ntel"]+" "+c["genre"]+" "+c["ville"]+" "+c["etat"])



#this function declares the winner on screen
def affichage():
     T2=array([int]*6)
     remplir(T2)
     s=cc(c["ntel"])
     msg="congartulation"+" "+ c["identifiant"]+" "+" avec le numéro de telephone: "+c["ntel"]+" "+" de la ville: "+c["ville"]+" "+"vouz avez gagné :)"
     if  sum(T2,s):
        f.l4.setText(msg)
     else:
        f.l4.setText("desolé vous navez pas gagné :(")
     print(c["ntel"])
     print(T2)
#this function resets all of the values
def annuler():
    f.l1.clear()
    f.l2.clear()
    f.l3.clear()
    f.l4.clear()
    f.rd1.setChecked(False)
    f.rd2.setChecked(False)
    f.checkbox1.setChecked(False)
    f.comboBox.setCurrentText("--Choix--")
    
     
    
app = QApplication([])
f = loadUi("ex5.ui")
f.show()
f.bt1.clicked.connect(play)
f.bt2.clicked.connect(affichage)
f.bt3.clicked.connect(annuler)
app.exec_()

#coded by ayoub

