class Car:
    def __init__(self,p,d):
        self.price=p
        self.discount=d
    def procss(self):
        print(self.price,self.discount)

c=Car(2000000,"10%")
#c.aadi()
c.procss()
