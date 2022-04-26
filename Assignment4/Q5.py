#Q.5. Write a Python program to create a file containing student records where each record contain  
# rollno and marks in 3 subjects separated by a comma (marks to be considered as list of 3 values).  
# e.g. records of students: 1, [45, 40, 35], 2, [41, 38, 39], 3, [35, 30, 37] (each line of the file  containing record of only 1 student). Prepare mark list in the following format:  
#Roll No. Mark-1 Mark-2 Mark-3 Total  
# 1 45 40 35 120  

#creating file
line=50*'='
stud=open("Student.txt",'w')
#taking rollno
print("------------For Exit the loop enter -1--------------")
print(line)
while(1):
    rollno=int(input("Enter rollno:- "))
    if(rollno==-1):
        break
    else:
        marks=[]
        for i in range(3):
            mark=int(input("Enter Mark{}:- ".format(i+1)))
            if(mark>=0 and mark<=100):
                marks.append(mark)
           
        stud.write(str(rollno)+"\t")
        #writting marks into file
        total=0
        for i  in marks:
            total+=i
            stud.write(str(i)+"\t")
        stud.write(str(total))
        stud.write("\n")
stud.close()

stud=open("Student.txt")
print("RollNo\tMarks1\tMarks2\tMarks3\tTotal")
for i in stud:
    print(i)

