f=open('name.txt')
#printing file data
for i in f:
    print(i)
f.close()    
#counting no of lines and chars
f1=open('name.txt')
count=0
char=len(f1.read())
for i in f1:
    count+=1
    
print("Total Lines are: {}".format(count)) 
print('Tptal characters are:- {}'.format(char))       

