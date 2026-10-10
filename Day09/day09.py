#Task -01 Basic List
fruits = ["Apple", "Banana", "Orange", "Guava", "Jackfruit"]
print(fruits[0])
print(fruits[2])
print(fruits[4])

#Task -02 Update List
language = ["Python", "C", "Java", "HTML"]
language[1] = "C++"
print(language)

#Task -03 Append
items = []
items.append("Pen")
items.append("Pencil")
items.append("Book")
items.append("Notebook")
items.append("Table Lamp")
print(items)

#Task -04 Remove
languages = ["Python", "C", "C++", "Java", "Javascript"]
languages.remove("Java")
print(languages)

#Task -05
products = ["Mouse", "Keyboard", "Monitor", "Printer", "Webcam"]
print(products)
products.append("Headphone")
products.remove("Printer")
print(products)

#Task -06 for loop +list
"""numbers = [10,20,30,40,50]
for i in numbers:
    print(i)"""

#Task 07
names = ["RUBAET", "RAHIM", "KARIM", "HASAN"]
for a in names:
    print("Hello",a,"!!")

#Task -08 List+Condition
numbers = [12,7,20,15,8,3,10]
for i in numbers:
    if(i%2==0):
        print(i)

#Task -09 Freelancing Style Data Filtering
prices = [250, 1200, 450, 3000, 800, 1500, 100]
print("Prices over 1000 tk:")
for p in prices:
    if(p > 1000):
        print(p)

#Task -10 Salary Filtering
salaries = [15000, 25000, 18000, 48000, 12000, 35000, 22000]
print("Salaries Greater Than 20000 Tk:")
for s in salaries:
    if(s>20000):
        print(s)

#Task 11 Count Even Numbers
numbers = [12, 7, 20, 15, 8, 3, 10, 1, 6]
count = 0
for t in numbers:
    if(t%2==0):
        count = count+1
print("Total Even Number =",count)

#Task 12 Calculate Total
prices = [250, 500, 1200, 300, 750]
amount = 0
for r in prices:
    amount = amount+r
print("Total Prices =",amount)

#Task 13
prices = [250,1200,450,3000,800,1500,100,2200]
amounts = 0
for w in prices:
    if(w >= 500 and w <= 2000):
        amounts = amounts + w
print("Total Price : ",amounts) 
