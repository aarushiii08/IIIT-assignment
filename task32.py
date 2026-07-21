#to count number of vowels, consonents and blanks
a = input("enter a string")
vowels = 0
consonents = 0
blanks = 0
for i in a:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        vowels += 1
    elif("a"<i<="z"):
        consonents += 1
    elif("A"<i<="Z"):
        consonents += 1
    elif(i==" "):
        blanks += 1
print("vowels - ",vowels)
print("consonents - ",consonents)
print("blanks - ",blanks)