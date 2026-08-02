#Multiplication Table
number = int(input("Enter a number: "))
for i in range(1, 11):
     print(number, "x", i, "=",number * i)
#Sum of Numbers
total = 0
for i in range(1, 11):
    total = total + i
print("Total = ",total)

#Print Even Numbers:
for i in range(2, 22, 2): 
    print(i)

#Print Odd Numbers:
for g in range(1, 21, 2): 
    print(g)

#Countdown:
for i in range(10, 0, -1): 
    print(i) 
print("Go!")

#Star Pattern:
for i in range(1, 6):
    print("*" * i)