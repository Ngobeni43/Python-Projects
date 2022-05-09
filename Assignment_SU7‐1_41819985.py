# Author: W.I Ngobeni(41819985)
import math
Side = round(float(input("Please insert one side of your square in meters: ",)),2)
if Side<=0:
    print("Please insert a number greater than 0")
else:
    diagonal = round(math.sqrt(Side**2+Side**2),2)
    perimeter = round(4*Side)
    print("The length of the diagonals of the Square is:",diagonal)
    print("The perimeter of the Square is: ",perimeter)
