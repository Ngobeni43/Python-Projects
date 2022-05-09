User_Name=input("Please enter your name: ")
User_Surname=input("Please enter your surname: ")
column=int(input("Enter the number of columns you want: "))
if column<4:
    Column=int(input("please enter a number greater than 3: "))
row=column-2
charecter=input("What charecter should make your shape?: ")
print(" ")
print("Your full name",User_Name,User_Surname)
print(" ")
print("Your rectangle is complete")
for i in range(column):
    for j in range(row):
        if i==0 or i==column-1  or j==0 or j==row-1:
            print(charecter,end="")
        else:
            print(charecter, end="")
    print()
