


#TU ZROBIE POZNIEJ LICZNIK DO UPGRADU I ODEJMOWANIU ITD ITD
class Counter:
    def __init__(self):
        self.count = 0
        self.upgrade_cost=10
        self.click_power = 1

    def increment(self):
        self.count+=self.click_power
        return self.count

    def upgrade_coin(self):
       if self.count >= self.upgrade_cost:
           self.count-=self.upgrade_cost
           self.click_power+=1
           self.upgrade_cost=int(self.upgrade_cost*1.7)
           return True
       return False