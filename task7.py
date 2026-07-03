#factorial
x = int(input("enter the number to find factorial - "))
n = 1
while x > 1:
    n = n * x 
    x = x - 1
print(n) 