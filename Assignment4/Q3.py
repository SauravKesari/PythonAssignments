#Q.3. Write a Python program to create a file of numbers by taking input from the user. Split this file  into two 
# files where one file contains odd numbers, and the other file contains even numbers  from the file. 
# You can take input of non-zero numbers, with an appropriate prompt, from the  user until the user enters a
#  zero to create the file assuming that the numbers are non-zero.  


f=open("nums.txt","a")
f1=open("even.txt","w")
f2=open("odd.txt","w")
while(1):
    number=int(input("Enter Numbers greater than Zero:- "))
    if(number<=0):
        break
    else:
        if(number%2==0):
            f1.write(str(number)+"\n")
        else:
            f2.write(str(number)+"\n")    