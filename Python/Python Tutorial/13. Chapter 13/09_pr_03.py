# A list contain the multiplication table of 7 . WAP to convert it to a vertical string of same numbers (7)
#                                                                                                        14
#                                                                                                         .

l = [str(i*7) for i in range(1, 11)]
print(l)

verticalTable = "\n".join(l)
print(verticalTable)