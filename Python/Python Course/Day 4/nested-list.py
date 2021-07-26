# Index Errors and working with Nested list

Language = ["C","C++","Java","Python","Ruby"]
print(len(Language))
# print(Language[len(Language)]) Index Error
print(Language[len(Language)-1-2])

Fruits = ["Apple","Banana","Orange","Watermelon","Mango"]
Vegetables = ["Potatoes","Onion","Brinjal","Tomatoes"]

dirty_dozen = [Fruits,Vegetables]

print(dirty_dozen)