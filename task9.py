#count number of digits 
x = int(input("enter the number - "))
count = 0
while x > 0:
    count = count + 1
    x = x // 10
print(count) 