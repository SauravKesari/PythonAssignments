#Q.2. Write a Python program to create a text file of multiple lines. Display the following: 
#  1. Entire text file  
#2. 1st n lines of the text tile.  
#3. m lines starting from the nth line  
#4. number of words in each line


#writing user data in file in append mode
line=50*'='
file=open("words.txt","a")
while(1):
    lines=input("Enter the text for line:- ")
    if(lines.lower()=='exit'):
        break
    else:
        file.write(lines+"\n")
file.close()
#reading data from file
print(line)
print("Entire Data is")
print(line)
f1=open("words.txt","r")
print(f1.read())
f1.close()
#first n lines of files
def readmyLines(n,f):
    f1=open(f,"r")
    for i in range(n):
        mytxt=f1.readline()
        print(mytxt)

nLines=int(input("Enter First n of lines to read:- "))
print("First {} lines reading: ".format(nLines))
print(line)
readmyLines(nLines,"words.txt")

#m lines starting from  nth lines
def readmnLines(m,n,f):
    f1=open(f,"r")
    mytxt=f1.readlines()
    for i  in range(m,n):
        print(mytxt[i])
    f1.close()
#----start and end point----------    
m=int(input("Start point Line Number:- "))
n=int(input("End Point Line number:-"))
print(line)
print("Line with specific range")
print(line)
readmnLines(m,n,"words.txt")

#count no of words
print(line)
print("---------------word count-----------")
print(line)
line_count=0
f1=open("words.txt")
for i in f1:
    words_count=0
    words=i.split(' ')
    words_count+=len(words)
    print("line {} words:- {}".format(line_count,words_count))  
    line_count+=1  
