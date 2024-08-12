# LOOPS
''' loops are just a way to repeat actions in Python, 
saving you from writing the same code over and over!
                or
    loop are used to repeat instructions
'''

# FOR LOOP 
'''' You know exactly how many times to go down'''
name="Abcdefghijklmnopqrstuvwxyz"
for i in name :
    print(i,end=" ")
    
    

color=["Red","Black","Yellow","Blue"]
for i in color:
    print(i)
    
    
number=[1,2]
for i in number:
    print(i)
    
    
# Range   

''' basically (n-1) & no. start with [0,1,2,3,4.......n]
so if we write to print no from 0-5 it will print [0,1,2,3,4]
and if we  does't want that then type (n+1)'''

for z in range(10):
    print(z+1)
    
    ''' For specific selection'''
    
for y in range(1,90):   
    print(y)
    
    
    
    # eg 1. To print a multiplication table 
table =int(input(" Enter the Number :"))
print("Multiplication of table ",table)
for i in range(1,10):
    print(table," x",i,"=",table *i)
    
    
    
    
    