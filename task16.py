#fibonacci 
def fibo(n):
    if n <= 1:
        print(n)
    print(fibo(n-1)+fibo(n-2))
x = int(input("number of digits"))
for i in range(x):
    print(fibo(i)) 