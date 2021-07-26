# wap to fill in a letter template given below with name and date 
# letter = ''' Dear <!Name !>
#             you are selected !
#             <!Date !> '''

letter = '''Dear <!Name!>
Greetings from ABC coding house. I am Happy to tell you about your Selection 
You Are Selected !
Have a great Day ahead!
Thanks and Regards
Bill
Date : <!Date!> '''


name = input("Enter your Name\n")
date = input("Enter Date\n")

letter = letter.replace("<!Name!>", name)
letter = letter.replace("<!Date!>", date)
print(letter)