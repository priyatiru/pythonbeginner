class student:
    school='telusko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    def get_m1(self):  
        return self.m1
    def set_m1(self,value):
        self.m1=value
        print("This is mutator method ")
    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def simple():     
        print("This is static method")
s1=student(21,34,54)
s2=student(21,12,13)
print(s1.avg())
print(s1.get_m1())
s2.set_m1(16)
print(s2.get_m1())
print(student.info())
student.simple()