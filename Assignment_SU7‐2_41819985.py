# Author: W.I Ngobeni(41819985)
import math
Long = round(float(input("PLease insert the length of the longest side: ")),2)
Sidex = round(float(input("PLease insert the length of one other side: ")),2)
SideY = round(float(input("PLease insert the length of the last side: ")),2)

if Long**2 == Sidex**2 + SideY**2:
    print("Your triangle is a right angle triangle")
else:
    print("Your triangle is not a right angle triangle")
