# WAP using function to convert celsius to fahrenheit ?
# Formula  = (0 degree Celsius * 9/5) + 32 = 32 degree F


def farh(cel):
    return (cel *(9/5)) + 32

c = 20
f = farh(c)
print("Fahreheit Temperature is " + str(f))
