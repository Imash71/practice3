class Student:
   school = "Programming School"
   def __init__(self, name):
       self.name = name
s1 = Student("Ali")
s2 = Student("Dana")
print(s1.school)
print(s2.name)