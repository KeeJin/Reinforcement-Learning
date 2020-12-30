import random

class Bandit:
    def __init__(self, wr_actual):
        self.wr_actual = wr_actual * 1000
        self.wr_calc = 0
        self.pullcount = 0
##        self.result = 0
    def pull(self):
        rng = random.randint(0,1000)
        result = rng < self.wr_actual
##            print("Lost!")
##            result = 0
##        else:
##            print("Win!")
##            result = 1 # win
        self.update(result)

    def update(self, result):
        total = self.wr_calc * self.pullcount + result
        self.pullcount += 1
        self.wr_calc = total / self.pullcount
        print("New WR calculated: " + str(self.wr_calc))
        
bandit1 = Bandit(0.8)
bandit1.pull()
