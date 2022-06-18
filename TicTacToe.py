from time import sleep
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel
from PyQt5.QtGui import QFont
import sys
class Kn(QWidget):
    def __init__(self):
        self.k=0
        super().__init__()
        self.label1=QLabel("X: Winner")
        self.setfont(self.label1)
        self.label2=QLabel("O: Winner")
        self.label3=QLabel("No one Won")
        self.setfont(self.label2)
        self.setfont(self.label3)
        self.button1=QPushButton(" ")
        self.setfont(self.button1)
        self.button2=QPushButton(" ")
        self.setfont(self.button2)
        self.button3=QPushButton(" ")
        self.setfont(self.button3)
        self.button4=QPushButton(" ")
        self.setfont(self.button4)
        self.button5=QPushButton(" ")
        self.setfont(self.button5)
        self.button6=QPushButton(" ")
        self.setfont(self.button6)
        self.button7=QPushButton(" ")
        self.setfont(self.button7)
        self.button8=QPushButton(" ")
        self.setfont(self.button8)
        self.button9=QPushButton(" ")
        self.setfont(self.button9)
        self.box1=QHBoxLayout()
        self.box2=QHBoxLayout()
        self.box3=QHBoxLayout()
        self.vbox=QVBoxLayout()
        self.box1.addWidget(self.button1)
        self.box1.addWidget(self.button2)
        self.box1.addWidget(self.button3)
        self.box2.addWidget(self.button4)
        self.box2.addWidget(self.button5)
        self.box2.addWidget(self.button6)
        self.box3.addWidget(self.button7)
        self.box3.addWidget(self.button8)
        self.box3.addWidget(self.button9)
        self.vbox.addLayout(self.box1)
        self.vbox.addLayout(self.box2)
        self.vbox.addLayout(self.box3)
        self.setLayout(self.vbox)
        self.setFixedSize(350,350)
        self.show()
        self.button1.clicked.connect(lambda: self.XO(self.button1))
        self.button2.clicked.connect(lambda: self.XO(self.button2))
        self.button3.clicked.connect(lambda: self.XO(self.button3))
        self.button4.clicked.connect(lambda: self.XO(self.button4))
        self.button5.clicked.connect(lambda: self.XO(self.button5))
        self.button6.clicked.connect(lambda: self.XO(self.button6))
        self.button7.clicked.connect(lambda: self.XO(self.button7))
        self.button8.clicked.connect(lambda: self.XO(self.button8))
        self.button9.clicked.connect(lambda: self.XO(self.button9))
    def XO(self,player):
        if self.k % 2 != 0 and player.text() == " ":
            player.setText("X")
            self.k+=1
        elif self.k % 2 == 0 and player.text() == " ":
            player.setText("O")
            self.k+=1
        q=0
        if self.button1.text() == "X" and self.button2.text() == "X" and self.button3.text() == "X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button1.text() == "X" and self.button4.text() == "X" and self.button7.text() =="X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button1.text() == "X" and self.button5.text() == "X" and self.button9.text() == "X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button2.text() == "X" and self.button5.text() == "X" and self.button8.text() == "X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button4.text() == "X" and self.button5.text() == "X" and self.button6.text() == "X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button3.text() == "X" and self.button6.text() == "X" and self.button9.text() == "X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button7.text() == "X" and self.button8.text() == "X" and self.button9.text() == "X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button3.text() == "X" and self.button5.text() == "X" and self.button7.text() == "X":
                self.label1.show()
                self.again()
                q+=1
        elif self.button1.text() == "O" and self.button2.text() == "O" and self.button3.text() =="O":
                self.label2.show()
                self.again()
                q+=1
        elif self.button1.text() == "O" and self.button4.text() == "O" and self.button7.text() =="O":
                self.label2.show()
                self.again()
                q+=1
        elif self.button1.text() == "O" and self.button5.text() == "O" and self.button9.text() == "O":
                self.label2.show()
                self.again()
                q+=1
        elif self.button2.text() == "O" and self.button5.text() == "O" and self.button8.text() == "O":
                self.label2.show()
                self.again()
                q+=1
        elif self.button4.text() == "O" and self.button5.text() == "O" and self.button6.text() == "O":
                self.label2.show()
                self.again()
                q+=1
        elif self.button3.text() == "O" and self.button6.text() == "O" and self.button9.text() == "O":
                self.label2.show()
                self.again()
                q+=1
        elif self.button7.text() == "O" and self.button8.text() == "O" and self.button9.text() == "O":
                self.label2.show()
                self.again()
                q+=1
        elif self.button3.text() == "O" and self.button5.text() == "O" and self.button7.text() == "O":
                self.label2.show()
                self.again()
                q+=1
        elif q == 0 and self.button1.text() != " " and self.button2.text() != " " and self.button3.text() != " " and self.button4.text() != " " and self.button5.text() != " " and self.button6.text() != " " and self.button7.text() != " " and self.button8.text() != " " and self.button9.text() != " ":
                self.label3.show()
                self.again()
    def again(self):
                self.button1.setText(" ")
                self.button2.setText(" ")
                self.button3.setText(" ")
                self.button4.setText(" ")
                self.button5.setText(" ")
                self.button6.setText(" ")
                self.button7.setText(" ")
                self.button8.setText(" ")
                self.button9.setText(" ")
    def setfont(self,font):
        font.setFont(QFont("Comic Sans MS",40))
app=QApplication([])
window=Kn()
sys.exit(app.exec())