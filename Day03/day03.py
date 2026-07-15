#BMI Calculator
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight/(height ** 2)
print("Your BMI is : ",bmi)

#Age Calculator
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))
age = current_year-birth_year
print("Your age is: ",age)

#Student Information
name = input("Enter your name: ")
department = input("Enter your department: ")
semester = input("Enter your semester: ")

print("\n------ Student Information ------")
print("Name: ",name)
print("Department: ",department)
print("Semester: ",semester)

#Circle Area Calculator
r = int(input("Enter radius: "))
import math
area = math.pi * r ** 2
print("Area of a circle: ",area)

#Temperature Calculator
c = float(input("Enter temperature in celsius: "))
f = (c*9/5) + 32
print("Temperature in fahrenheit: ",f)