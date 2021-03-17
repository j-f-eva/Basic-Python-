# oject oriented theory class
#basic class 

#create class
class Student:
    name =''
    id = ''
    
    #constructor function  underdash dte hobe
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def printInfo(self):
        print("My info is : ", self.name,self.id )
        print('I am a print info function')
    
    def demoMethod(self):
        print(self.name[:5])
        print(self.id)
        print(self.name[5:])
    
    def printHI(self):
        if 'Hobby' in self.__dict__:
            print(self.name)
        

#object create        
eva = Student("Jannatul Ferdous Eva",18201053)

#call classes
eva.printInfo()
eva.demoMethod()

jannatul = Student('hi, i am eva',18201053)

jannatul.printInfo()
print(jannatul.__dict__)

jannatul.demoMethod()
print(jannatul.__dict__)
        
        