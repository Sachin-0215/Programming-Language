# Paint area calculator

import math
test_h = int(input("Height of the Wall? "))
test_w = int(input("Width of the Wall? "))

coverage = 5

def paint_cal(height, width, cover):
    area = height*width
    number_of_cans = area/cover
    # total_cans = round(number_of_cans)
    total_cans = math.ceil(number_of_cans)
    print(f"You'll need {total_cans} cans of paints. ")


paint_cal(test_h, test_w, coverage)
