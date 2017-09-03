from random import randint

class player():
    Qi = 0
    Blood = 10
    cont = 0
    
    def Yun(self,Opponent):
        self.Qi = 1 +self.Qi
    def Bo(self,Opponent):
        self.Qi -= 1
        if Opponent.cont == 3:
            pass
        else:
            Opponent.Blood -= 1
    def Dang(self,Opponent):
        if Opponent.cont == 2:
            self.Qi -=1
        else:
            pass
    def XXDF(self,Opponent):
        if Opponent.cont ==3 :
            self.Qi =self.Qi -5
            pass
        elif Opponent.cont == 1:
            temp = Opponent.Qi 
            Opponent.Qi =0
            self.Qi = temp + self.Qi -5
        else:
            self.Qi = Opponent.Qi + self.Qi -5
            Opponent.Qi = 0 

    def run(self,opp):
        if self.cont ==1:
            self.Yun(opp)
            return('运')
        elif self.cont ==2:
            self.Bo(opp)
            return('波')
        elif self.cont ==3:
            self.Dang(opp)
            return('挡')
        else:
            self.XXDF(opp)
            return('吸星大法')
        
class computer(player):
    def Ai(self):
        if self.Qi < 1:
            self.cont =1
        elif(5 > self.Qi >= 1):
            self.cont = randint(1, 3)
        else:
            self.cont = randint(1, 4)
            
           
       
       
       
       
       
