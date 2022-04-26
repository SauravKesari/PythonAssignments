#Q.6. Write a Python program to create a file of strings by taking input from the user and then create  a dictionary 
# containing each string along with their frequencies. (e.g. if the file contains ‘apple’,  ‘banana’, ‘fig’, ‘apple’,
#  ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’ then the output should  be {'apple': 3, 'banana': 2, 'fig': 3, 
# 'grapes': 2}.  

#creation of dictionary and list for storing data
worddict={}
wordlist=[]
# Taking input and storing into list
while(1):
    word=input("Enter words:- ")
    if(word.lower()=='exit'):
        break
    else:
        wordlist.append(word)

#Writing list data into file names temp.txt
file=open("temp.txt","w")
for i in wordlist:
    file.write(i+"\n")
file.close()

#Reading file and adding that into list without any tabspace and '\n'
f1=open("temp.txt")
# reading file data line by line and store it into li list
f2=f1.readlines()
# strip method remove \t and \n from data
li=[x.strip() for x in f2]
# Thee data is:
print(70*'=')
print("Data of File is:- ",li)

# Storing list named 'li' data into dictionary and counting frequency
for i in li:
    if(i in worddict):
        worddict[i]+=1
    else:
         worddict[i]=1
print(70*'=')
print("Dictionary with Frequency is:",worddict)            
