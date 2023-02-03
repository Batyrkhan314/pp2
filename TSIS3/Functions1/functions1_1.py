'''.A recipe you are reading states how many grams you need for the ingredient. Unfortunately, 
your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
'''


def changer(n):
    o  = 28.3495231*float(n)
    return o

'''t = input("mass in grams: ")
print("Mass in ounces: " + str(changer(t)))'''