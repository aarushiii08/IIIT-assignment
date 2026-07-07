#define a class that can add and subtract two number
class solve:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
a = int(input("enter 1st number - "))
b = int(input("enter 2nd number - ")) 
s = solve()
s.add(a,b)
s.sub(a,b) 