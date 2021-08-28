# Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        s = "my name is " + self.name + " and I am " + str(self.age) +  " years old!"
        return s

class SayHi(object):
    def __init__(self, obj):
        self.obj = obj        
    
    def __str__(self):
        return "Hi, " + self.obj.__str__()

d1 = Dog("Dot", 4)
d2 = Dog("Elf", 3)
assert(str(SayHi(d1)) == "Hi, my name is Dot and I am 4 years old!")
assert(str(SayHi(d2)) == "Hi, my name is Elf and I am 3 years old!")
print("Test cases passed")