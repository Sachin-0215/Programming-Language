# Can we change the self parameter inside a class to something else(say 'Sachin').Try changing self to 'parameter' or Sachin and see the effects. 

class Sample: 
    def __init__(parameter, name):
        parameter.name = name

obj = Sample("Sachin") 
print(obj.name) 
 