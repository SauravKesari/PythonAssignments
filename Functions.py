import myModule
def fun(myname):
    print("My name is:- "+myname)
fun("Lio")    
#Nested fun
x=15
print('Global x:- ',x)
def fun1():
    global x
    y=35
    x=x+10
    print('Non local y is:-',y)
    print('Inside fun x:- ',x)
    def fun2():
        nonlocal y
        y=y+20
        print('Y inside fun:- ',y)
    fun2()    
fun1()    

#keyword arguements
def key(child1,chile2):
    print('My values are:-'+child1+" and "+chile2)
key(child1='EMail',chile2='Pass')    

#multiple arguements in one function

def multiple(*key):
    sum=0
    for i in range(0,len(key)):
        sum+=key[i]
    print("Sum is:- ",sum)    
multiple(2,3,4,5)        
#module call
print(myModule.person['age'])
