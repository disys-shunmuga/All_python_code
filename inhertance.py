import inhertance1
import inhertance2



class cities(inhertance2.states):

    def __init__(self,p):

        self.population = p
        super().__init__(45,50)

    def read(self):

        print(self.population)

data = cities(100000000)
data.read()
data.op()
data.opp()
