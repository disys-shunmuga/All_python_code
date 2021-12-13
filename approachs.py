""" Apporach 1 """

name = "name"

""" Apporach 2 """

class classname:
    __work = "python"

    def __init__(self):
         self.__method=1

    def method(self):
        print(self.__method)

cc=classname()
cc.method()

""" Apporach 3 """

saturday=("sleep","eat","play","repeat")
print(saturday[3])

""" Apporach 4 """

dcit1={"sunday":" Day 1","monday":" Day 2","tuesday":" Day 3"}

print(dcit1["sunday"])

""" Apporach 5 """

list1=["data1","data2","data3","data4","data5"]
for i in list1:
    #print(i)
    if(i=="data4"):
        print("yes")
        print(i)
        break
    #print(i)

""" Apporach 6 """

obb=[{"data1":1},{"data2":2},{"data3":3}]
for i in obb:
    for j in i:
        if(i[j]==3):
            print("yes")
        else:
            print("No")


""" Apporach 7 """

lis={"sunday":{"morning":["eat","sleep","repeat"]},"monday":{"morning":["eat","work","sleep","repeat"]}}
for i in lis.values():
    #print(i)
    for j in i.values():
        #print(j)
        for k in j:
            if(k == "eat"):
                print("found")
                break
    break
    
    
    

        
        
