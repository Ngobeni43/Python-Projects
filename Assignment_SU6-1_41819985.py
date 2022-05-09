'Wisani  Isaac Ngobeni__Student number_41819985'
import math
Height=float(input("Please povide me with altitude: "))
Base=float(input("Please provide me with base: "))
Hype=round(math.sqrt((Height**2)+(Base**2)),1)
Circumference= Height+Base+Hype
Area=round(0.5*Height*Base,1)
print(Hype)
print("The perimeter of the triangle is:",Circumference)
print("The area of the triangle is:",Area)
Width=float(input("Please provide the width of the triangular volume : "))
mVolume=round((Area*2),1)
Volume=round((Area*Width),1)
print("Volume of the triangle if width is 2m:",mVolume)
print("Actual volume of triangle is:",Volume)
