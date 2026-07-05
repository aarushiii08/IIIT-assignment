#palindrome
x = int(input("enter a number - "))
temp = x
y = 0
while x > 0:
    y = (y * 10) + (x % 10)
    x = x // 10
if temp == y:
    print("palindrome")
else:
    print("not palindrome") 