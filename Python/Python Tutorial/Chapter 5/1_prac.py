# WAP to create a dictionary of hindi words and values as their English translations . Provide user with an option to look it up

myDict = {
    "Pankha":"Fan",
    "Dabba":"box",
    "Vastu":"Item"
}
print("Options are ",myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is :",myDict[a])
# Below line will not throw an error if the keys is not present in the dictionary
print("The meaning of your word is :",myDict.get(a))