from random import randint
#skill = {'运':1, '小波':2, '小挡':3,  '中运':4, '中波':5, '中档':6,'吸星大法':7, '小李飞刀':8}
class player():
    Qi = 0
    Blood = 30
    cont = 0
    
    def Yun(self,Opponent):
        self.Qi += 1
    def Bo_x(self,Opponent):
        if (Opponent.cont == 3 or Opponent.cont == 4 or Opponent.cont == 6 ):
            self.Qi -= 1
        elif Opponent.cont == 7:
            pass
        else:
            Opponent.Blood -= 1
            self.Qi -= 1
    def Dang_x(self,Opponent):
        if Opponent.cont == 2 or Opponent.cont == 5 or Opponent.cont == 7 or Opponent.cont == 8:
            self.Qi -=1
        else:
            pass
    def XXDF(self,Opponent):
        if Opponent.cont == 3 or Opponent.cont == 6:
            self.Qi -= 5
            pass
        elif Opponent.cont == 1:
            temp = Opponent.Qi 
            Opponent.Qi =0
            self.Qi = temp + self.Qi -5
        else:
            self.Qi = Opponent.Qi + self.Qi -5
            Opponent.Qi = 0 
    def Yun_z(self,Opponent):
        self.Qi += 2
    def Bo_z(self,Opponent):
        self.Qi -= 2
        if Opponent.cont == 3:
            Opponent.Blood -= 1
        elif Opponent.cont == 6 or Opponent.cont == 7:
            pass
        else:
            Opponent.Blood -= 1 
    def Dang_z(self, Opponent):
        if (Opponent.cont == 2 or Opponent.cont== 5 or Opponent.cont == 7 or Opponent.cont == 8):
            self.Qi -=2
        else:
            pass
    def XLFD(self,Opponent):
        if Opponent.cont == 3:
            Opponent.Blood -= 4
            self.Qi -= 5
        elif  Opponent.cont ==7:
            pass
        elif Opponent.cont == 6:
            Opponent.Blood -= 3
            self.Qi -= 5
        else:
            Opponent.Blood -= 5
            self.Qi -= 5
        
    def run(self,opp):
        if self.cont == 1:
            self.Yun(opp)
            return('运')
        elif self.cont == 2:
            self.Bo_x(opp)
            return('小波')
        elif self.cont == 3:
            self.Dang_x(opp)
            return('小挡')
        elif self.cont == 4:
            self.Yun_z(opp)
            return('中运')
        elif self.cont == 5:
            self.Bo_z(opp)
            return('中波')
        elif self.cont == 6:
            self.Dang_z(opp)
            return('中挡')
        elif self.cont == 7:
            self.XXDF(opp)
            return('吸星大法')
        elif self.cont == 8:
            self.XLFD(opp)
            return('小李飞刀')
        
class computer(player):
    def Ai(self):
        if self.Qi < 1:
            self.cont =1
        elif(2 >= self.Qi >= 1):
            self.cont = randint(1, 6)
        else:
            self.cont = randint(1, 8)
            
           
       
       
       
       
       
