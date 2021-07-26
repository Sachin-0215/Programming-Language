# The game() function in program lets a user play a game and returns the score as an 
# integer . You need to read a file 'Hi-score.txt' which is either blank or contains the previous 'Hi-score'.
# You need to WAP to update the 'Hi-score' whenever games() breaksthe 'Hi-score'.

def game():
    return 44677123

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))