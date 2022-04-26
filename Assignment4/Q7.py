file=open("question7.txt","w")
lines=[]
while True:
    elem=input("Enter the line Element:-  ")
    if(elem=='exit'):
        break
    else:
        lines.append(elem)
for i in lines:        
    file.write(i+"\n")
file.close()

f1=open("question7.txt")
for i in f1:
    print(i)

    
