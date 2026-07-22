#Positive / Negative Number
number = int(input("Enter a number: "))
if number >= 0:
     print("Positive Number")
else:
     print("Negative Number")

#Largest Number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>num2:
     print("Largest number: ",num1)
else:
     print("Largest number: ",num2)

#Divisible
num = int(input("Enter a number: "))
if num%5==0:
     print("Divisible")
else:
     print("Not Divisible")

#Even & Positive
num = int(input("Enter a number: "))
if num%2==0 and num>0:
    print("Positive Even Number")
else:
    print("Not a Positve Even Number")
