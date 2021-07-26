# Creating an  empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
# b.add(5)  -----> Set is a collection of non repeative elements
# b.add(5)
# b.add([4,5,6])   -----> Cannot add lists to sets

# Accessing the elements

# b.add({4:5})     -----> Cannot add dictionary to sets
b.add((4,5,6))

print(b)

# Length of the set 
print(len(b))    # ------ Prints the length of this set

# Removal of an item
b.remove(5)  # ---> removes 5 from set b
# b.remove(55)  # ---> throws an error while trying to remove 55(which is not present in the set)
print(b)

print(b.pop())
print(b)