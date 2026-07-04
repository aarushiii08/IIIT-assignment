#guess a number
import random
x = random.randint(1,100)
n = int(input("enter a number between 1 to 100-"))
while x != n:
    if x > n:
        print("Higher than that")
    else:
        print("lower than that") 
    n = int(input("Try again"))
print("correct")  
