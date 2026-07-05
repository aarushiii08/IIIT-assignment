#check last digit is divisible by 3 or not
x = int(input("enter the number - "))
y = x % 10
if (y % 3) == 0:
    print("divisible by 3")
else :
    print("not divisible by 3") 