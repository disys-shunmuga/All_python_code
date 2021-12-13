import inhertance1

class states(inhertance1.india):

    def __init__(self,c,i):

        self.number_of_cities = c
        self.it_company = i
        super().__init__(28,"rich")

    def opp(self):

        print(self.number_of_cities,self.it_company )

        
