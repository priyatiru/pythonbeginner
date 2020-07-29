
class Person:
    def __init__(self,initialAge):
        if initialAge>=0:
            self.age=initialAge
        else:
            self.age=0
            print("Age is not valid, setting age to 0.")
    def checkOld(self):
        if self.age<13:
            print("You are young.")
        elif 13<=self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
        
    def yearPasses(self):
        self.age=self.age+1

t = int(input())
for i in range(0, t):
    age = int(input())         
    x = Person(age)  
    x.checkOld()
    for j in range(0, 3):
        x.yearPasses()       
    x.checkOld()
    print("")