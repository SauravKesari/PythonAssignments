#Q.4. Write a Python program to create a file of elements of any data type (mixed data type, i.e. some  elements maybe 
# of type int, some elements of type float and some elements of type string). Split  this file into three file 
# containing elements of same data type (i.e. 1st file of integers only, 2nd file of float only and 3rd file of strings only). Take input from the user to create the file.  
integerFile=open("integer.txt","a")
floatFile=open("float.txt","a")
stringFile=open("string.txt","a")
while(1):
    elem=input("Enter Element:- ")
    if(elem=='exit'):
        break
    else:
        try:
            # Convert it into integer
            val = int(elem)
            integerFile.write(elem+"\n")
        except ValueError:
            try:
                # Convert it into float
                val = float(elem)
                floatFile.write(elem+"\n")
            except ValueError:
                stringFile.write(elem+"\n")
                
