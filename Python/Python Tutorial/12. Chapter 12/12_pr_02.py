# WAP to print third , fifth and seventh element from a list using enumerate function. 

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(l):
    if index==1 or index== 4 or index==6:
        # print(index , item)
        print(f"The {index + 1}th element is {item}")