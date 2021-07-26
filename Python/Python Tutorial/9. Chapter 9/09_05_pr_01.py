# WAP to read the text from a given file ''poem.txt' and find out whether it contain the word 'twinkle'


f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()