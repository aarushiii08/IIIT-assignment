#armstrong number
x = int(input("enter a number - "))
temp = x
n = 0
while x > 0:
    a = x % 10
    n = n + a ** 3
    x = x // 10 
if temp == n:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number") 