#Q.1. Write a Python program to create a file of numbers by taking input from the user and then  display the content of 
# the file. You can take input of non-zero numbers, with an appropriate  prompt, from the user until the user enters a 
# zero to create the file assuming that the numbers  are non-zero.  

file=open("nums.txt","w")
while(1):
    num=int(input("Enter Number"))
    if(num<=0):
        break
    else:
        file.write(str(num)+"\t")
file.close()

f=open("names.txt","r")
for i in f:
    print("Numbers are:- ",i)