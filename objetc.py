from useful import Student
from useful import Chef
from chef import ChineseChef

Student1 = Student("jim", "business", 3.7, False)
Student2 = Student("pam", "art", 2.4, True)

print(Student2.name)
print(Student1.on_honor_roll())

myChef = Chef()
myChef.make_chicken() 

myChineseChef = ChineseChef()
myChineseChef.make_chicken() 
 
