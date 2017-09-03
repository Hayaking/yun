from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_yun import Ui_MainWindow
import Player
import sys
skill = {'运':1, '小波':2, '挡':3, '吸星大法':4}
class MainWindow(QMainWindow,Ui_MainWindow):
    player = Player.player()
    com = Player.computer()
    def __init__(self,parent = None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonclicked)
        self.pushButton_2.clicked.connect(self.buttonclicked)
        self.pushButton_3.clicked.connect(self.buttonclicked)
        self.pushButton_4.clicked.connect(self.buttonclicked)
        Update_status(self)


    @pyqtSlot()
    def buttonclicked(self):
        sender = self.sender()
        self.player.cont = skill[sender.text()]
        self.com.Ai()
        self.textEdit_3.append('玩家使用了' +  self.player.run(self.com))        
        self.textEdit_3.append('电脑使用了' + self.com.run(self.player)+'\n')
        Button_switch(self, self.player)
        Update_status(self)
        judge(self, self.player, self.com)
       
def Button_switch(self, obj):
    #按钮开关
        if (obj.Qi >= 1 ):
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
        else :
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
        if (obj.Qi >= 5 ):
            self.pushButton_4.setEnabled(True)
        else :
            self.pushButton_4.setEnabled(False)
def Update_status(self):
        self.textEdit_2.setText("玩家血量:"  + str(self.player.Blood) + "\n" + "玩家的气:"+str(self.player.Qi))
        self.textEdit.setText("电脑血量:"  + str(self.com.Blood) + "\n" + "电脑的气:"+str(self.com.Qi)) 
        
def judge(self, obj1, obj2):
    if obj1.Blood <= 0 or obj2.Blood <=0 :
        if obj1.Blood >0:
            print('p获胜')
            QMessageBox.about(self,"结束","玩家胜利")
        elif obj1.Blood == obj2.Blood:
            QMessageBox.about(self,"结束","平均")
        else:
            QMessageBox.about(self,"结束","电脑胜利")
    
if __name__ == "__main__":
        app = QApplication(sys.argv)
        action = MainWindow()
        action.show()
        sys.exit(app.exec_())
