# A spam comment is defined as a text containing following keywords:
# "Make a lot of money ","buy now","subscribe this",
# "Click this", WAP to select these spams?


text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")