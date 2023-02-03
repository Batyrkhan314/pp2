'''Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
 The following formula is used for the conversion: C = (5 / 9) * (F – 32)'''


def far_to_cent(n):
    t = (5/9) * (float(n)-32)
    return t

a = input("in farenheit: ")
print("result in centigrade: " + str(far_to_cent(a)))