#login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#GRADE Calculator
marks = int(input("Enter your marks: "))
if marks>100 or marks<0:
    print("Invalid marks!!")
elif marks>=80:
    print("A+")
elif marks>=70:
    print("A")
elif marks>=60:
    print("B")
elif marks>=50:
    print("C")
elif marks>=40:
    print("D")
else:
    print("Fail")

#Leap year checker
y = int(input("Enter year: "))
if y%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")

#Number Checker
n = int(input("Enter anumber: "))
if n>0 and n%2==0:
    print("Positive Even Number")
elif n>0 and n%2!=0:
    print("Positve Odd Number")
elif(n==0):
    print("Zero")
else:
    print("Negative Number")