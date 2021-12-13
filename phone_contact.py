class Phone:

    pb = []
    
    def add_contact(self,c_name:str,pno:str):
        self.name = c_name
        self.p_no = pno
        if isinstance(self.name,str)== False:
            raise TypeError("give the input in str")
        if isinstance(self.p_no,str)== False:
            raise TypeError("give the input in str")
        if(len(self.p_no)<10):
            raise ValueError("the number must be 10 character")
            #pass
        if(len(self.name) > 20):
            raise ValueError("the name must be 10 character")
            #print()
        else:
            Phone.pb.append(self.name)
            Phone.pb.append(self.p_no)
            #print(Phone.pb)


    def disp(self):
        print(Phone.pb)
        #pass

    def convert(self):

        

'''
    def search(self):

        #self.s_name = Phone.pb
        self.temp = str(input("enter the name : "))
        for i in Phone.pb:
            if(self.temp in Phone.pb)== True:
                print(self.temp)
                break
            else:
                raise TypeError("Type the name correctly")
                break
'''
    
        
                
    



asi=Phone()
check=Phone()
asi.add_contact("Shunmugapragasam","9876543211")
#asi.disp()
asb=Phone()
asb.add_contact("sanjeev","73327364440")
#asb.disp()
check.disp()
#check.search()
check.Convert()
