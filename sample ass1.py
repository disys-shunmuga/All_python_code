'''buffet = [{"briyani":25,"egges":25,"chickenbriyani":45,"ice_cream":25,"jamon":25}]

invit={"ramesh":"chocolate","suresh":"pen","rajesh":"dairy","suam":None,"suma":None}

gift=[]

for come,g in invit.items():
    if g!= None:
        gift.append(g)
        print(g)
    if come :
        print("have a dinner")'''


class disys:
    def __init__(self,vacc):
        self.vac=[]
        self.vac.append(vacc)
        self.count=0

    def logic(self):
        for i in self.vac:
            if i["vaccc"]== None:
                self.count=self.count+1
                #print(self.count)
                print(self.count,"Not vaccinated")
            else:
                self.count=self.count+2
                print(self.count,"Vaccinated")
                continue
        print(self.vac)

jb=disys({"name":"jb","empid":"007","vaccc":None})
fb=disys({"name":"fb","empid":"008","vaccc":"1st dose"})
db=disys({"name":"db","empid":"009","vaccc":"1st dose"})
jb.logic()
fb.logic()
db.logic()



