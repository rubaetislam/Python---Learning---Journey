#Square Function
def square(number):
    return number * number
print(square(5))
print(square(6))

#Maximum Number Function
def check(number):
    if(number %2 == 0):
        print("EVEN")
    else:
        print("ODD")
check(44)
check(11)

#Mini projest 01
def sqr(a):
    return a*a
sol = sqr(5)
print("Result = ",sol)

#Mini project 02
def num(a):
    if (a%2==0):
        return "Even Number"
    elif(a%2!=0):
        return "Odd Number"
Number = num(10)
print("The number is", Number)

#mini projest 03
def greet(name):
    print("Hello", name)
greet("RUBAET")

#mini project 04
def num(a, b):
    return a*b
number = num(5,8)
print("Multiplication = ",number)

#mini project 05
def num(a,b):
    if(a>b):
        return a
    else:
        return b
number = num(5,8)
print("Greater number is = ",number)

#mini project 06
def temp(c):
    f = (9*c)/5+32
    return f
temperature = temp(30.95)
print("Today's temperature is", temperature)