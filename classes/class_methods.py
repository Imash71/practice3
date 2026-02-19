class Person:
   def __init__(self, name):
       self.name = name
   def greet(self):
       print("Hello, my name is", self.name)
person1 = Person("Imash")
person1.greet()