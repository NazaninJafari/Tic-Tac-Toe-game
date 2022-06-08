import random
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('form1.ui',None)
        self.ui.show()
        
        self.game = [[self.ui.Btn_1, self.ui.Btn_2, self.ui.Btn_3],
                     [self.ui.Btn_4, self.ui.Btn_5, self.ui.Btn_6],
                     [self.ui.Btn_7, self.ui.Btn_8, self.ui.Btn_9]]
        self.score_x = 0
        self.score_o = 0
        self.score_equal = 0
        
        self.count = 0
        
        self.end_game = False
        self.flag = 'x'
        self.click = 1
 
        #self.ui.radioButton.clicked.connect(self.start)
        #self.ui.radioButton_1.clicked.connect(self.start)
        self.ui.restart_button.clicked.connect(self.restart_func)
        self.ui.about_Button.clicked.connect(self.about_func)
        
    #def start(self):
        for i in range (3):
            for j in range (3):
                self.game[i][j].clicked.connect(partial(self.play, i ,j))
                    
                
    def play(self, i, j):
        #run two player 
        if self.ui.radioButton_1.isChecked():
            if self.game[i][j].text() == '' and self.end_game == False :
                if self.flag == 'x':
                    self.game[i][j].setText('X')
                    self.game[i][j].setStyleSheet('color: purple ; background-color: black')
                    self.flag = 'o'
                else:
                    self.game[i][j].setText('O')
                    self.game[i][j].setStyleSheet('color: white; background-color: black')
                    self.flag = 'x'
            self.count += 1         
        #run one player               
        if self.ui.radioButton.isChecked():
            if self.game[i][j].text() == '' and self.end_game == False :
                if self.flag == 'x':
                    self.game[i][j].setText('X')
                    self.game[i][j].setStyleSheet('color: purple ; background-color: black')
                    self.flag = 'o'
                else:
                    while True:
                        i = random.randint(0,2)
                        j = random.randint(0,2)
                        if self.game[i][j].text() == '' and self.end_game == False :
                            self.game[i][j].setText('O')
                            self.game[i][j].setStyleSheet('color: white; background-color: black')
                            self.flag = 'x'
                            break 
                self.count += 1
        self.check()

    def check(self):

        if self.game[0][0].text()==self.game[0][1].text()==self.game[0][2].text() : 
            if self.game[0][2].text()== 'X':
                self.show_winner('X')
                self.end_game = True
            elif self.game[0][2].text()== 'O':          
                self.show_winner('O')
                self.end_game = True

        elif self.game[1][0].text()==self.game[1][1].text()==self.game[1][2].text() :
            if self.game[1][2].text()== 'X':
                self.show_winner('X')
                self.end_game = True
            elif self.game[1][2].text()== 'O':
                self.show_winner('O')
                self.end_game = True

        elif self.game[2][0].text()==self.game[2][1].text()==self.game[2][2].text() :
            if self.game[2][2].text()== 'X': 
                self.show_winner('X')
                self.end_game = True           
            elif self.game[2][2].text()== 'O':         
                self.show_winner('O')
                self.end_game = True

        elif self.game[0][0].text()==self.game[1][0].text()==self.game[2][0].text() :
            if self.game[2][0].text()== 'X':
                self.show_winner('X')
                self.end_game = True
            elif self.game[2][0].text()== 'O':
                self.show_winner('O')
                self.end_game = True         
          
        elif self.game[0][1].text()==self.game[1][1].text()==self.game[2][1].text() :
            if self.game[2][1].text()== 'X':
                self.show_winner('X')
                self.end_game = True 
            elif self.game[2][1].text()== 'O':
                self.show_winner('O')
                self.end_game = True

        elif self.game[0][2].text()==self.game[1][2].text()==self.game[2][2].text() :
            if self.game[2][2].text()== 'X': 
                self.show_winner('X')
                self.end_game = True
            elif self.game[2][2].text()== 'O':
                self.show_winner('O')
                self.end_game = True

        elif self.game[0][0].text()==self.game[1][1].text()==self.game[2][2].text() :
            if self.game[2][2].text()== 'X':
                self.show_winner('X') 
            elif self.game[2][2].text()== 'O':
                self.show_winner('O')

        elif self.game[0][2].text()==self.game[1][1].text()==self.game[2][0].text() :
            if self.game[2][0].text()== 'X':
                self.show_winner('X') 
            elif self.game[2][0].text()== 'O':
                self.show_winner('O')     
        
        #there is not empty button
        elif self.count == 9 and self.end_game == False:
            self.show_equality()    
             
    def restart_func(self):
        for i in range (3):
            for j in range (3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color: rgb(39, 39, 39);')
        self.flag = 'x'
        self.end_game = False
        self.count = 0
        self.click = 1

    def show_winner(self,p):
        msgBox = QMessageBox()
        msgBox.setText('player '+ p +' wins')
        msgBox.exec()
        if p == 'X' and self.click == 1 :
            self.score_x += 1

        elif p == 'O' and self.click == 1 :
            self.score_o += 1

        self.ui.label.setText('Player X: ' +str(self.score_x))
        self.ui.label_1.setText('Player O: ' +str(self.score_o)) 
        self.click = 0    
    
    def show_equality(self):
        msgBox = QMessageBox()
        msgBox.setText('equality')
        msgBox.exec()
        if self.click == 1 :
            self.score_equal += 1
        self.ui.label_2.setText('Equality: ' +str(self.score_equal)) 
        self.click = 0
        self.end_game = True
            
    def about_func(self):
        msgBox = QMessageBox()
        msgBox.setText('Tic Tac Toe game\nThis game programmed with Python \nprogrammer: Nazanin\n "5 June 2021"')
        msgBox.exec()

app = QApplication()
window = TicTacToe()
app.exec()
