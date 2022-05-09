# Author: W.I Ngobeni(41819985)
print(" ")
print("BMI Calculator")
print(" ")
print("please select desired unit by selecting a corresponding number")
print("1. Weight in kilograms, height in meters")
print("2. Weight in pound, height in inches")
print(" ")

unit = float(input("Indicate choice: "))
if unit==1:
    weight=round(float(input("Enter your weight in kg: ")),2)
    height=round(float(input("Enter your height in m: ")),2)
    BMI=round((weight)/(height**2),2)
    if BMI >=35:
        Label = "Severely obese"
    elif BMI <35:
        Label= "Obese"
    elif BMI <30:
        Label= "Overweight"
    elif BMI <25:
         Label= "Healthy"
    elif BMI <18.5:
        Label= "Underweight"
    print(" ")
    print("BMI Report")
    print("Weight:",weight,"kg")
    print("Height:", height,"m")
    print("BMI:",BMI)
    print("Status: ",Label)
    print("")
    exit=input("Press enter to quit  the program")
if unit==2:
    weight=round(float(input("Enter your weight in pounds: ")),2)
    height=round(float(input("Enter your height in inches: ")),2)
    BMI=round((weight)/(height**2)*703,2)
    if BMI >=35:
        Label = "Severely obese"
    if BMI <35:
        Label= "Obese"
    if BMI <30:
        Label= "Overweight"
    if BMI <25:
         Label= "Healthy"
    if BMI <18.5:
        Label= "Underweight"
    print(" ")
    print("BMI Report")
    print("Weight:",weight,"lbs")
    print("Height:", height,"in")
    print("BMI:",BMI)
    print("Status:",Label)
    print("")
    exit=input("Press enter to quit  the program")
