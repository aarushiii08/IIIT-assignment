#student report
name = input("enter name - ")
roll_no = int(input("enter roll number - "))
branch = input("enter branch - ")
print("enter marks")
sub1, sub2, sub3, sub4, sub5 = int(input("subject 1, subject 2, subject 3, subject 4, subject 5,").split(","))
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total // 5
percentage = ( total // 500 ) * 100
print(name)
print(roll_no)
print(branch)
print(total)
print(average)
print(percentage) 