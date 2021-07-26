# Create a class with a class Attribute a ; Create an object from it and set a directly 
# using Object.a = a . Does this change the class Attribute

class Sample:
    a = "Sachin" 

obj  = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky"

print(Sample.a)
print(obj.a)