import random
randNumber = random.randint(1, 100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess :"))
    guesses += 1
    
    if(userGuess == randNumber):
        print("You Guessed It Right!")
    else:
        if(userGuess>randNumber):
            print("You Guessed It Wrong! Enter a Smaller Number")
        else:
            print("You Guessed it wrong! Enter a Larger Number")    

print(f"You Guessed the Number in {guesses} guesses")     

with open("hiscore.txt","r") as f:
    hiscore = int(f.read()) 

    if(guesses<hiscore):
        print("You Have Just The Hi-Score")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))