# Positional vs Keywords Arguments

# Function with more than one 1 input
from os import name

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Sachin Gupta","Mumbai")

# functional with keywords arguments

greet_with(location="jabalpur",name="Jai")