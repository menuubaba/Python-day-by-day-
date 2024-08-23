#           LISTS
#   They are used to store multiple values in a single variable
#   They are created using the square brackets :    ['abc','asd',.......]  
#  and moreover that we can use any type of variable in it 
# it can be string,int,float,boolean .

list1 =["Apple","Mango","banana"] 
print(list1) 

print(type(list1))

# type 
 # to tell which type of data is    

list2=[1,2,3,4]
list3=['nmb','hk','kjg']
list4=[True,False,False,True]
print(type(list2))
print(type(list3))
print(type(list4))

# List()Constructor

# same as list instead of square bracket we can also use round brackets 
# for eg.
bgmilist =("Erangel","mirammar","Sanok", "Nusa")
print(type(bgmilist))


# Accesing list items 
# to access the elements of a list enter the index number 
# eg.
players=["jonathan","Mortal","Spower","Scout","Snax","Delta","Mavi","Nakul"]
print(players[6])

# not that if we write -ve value the index start from 1,2,3... and it start from RIGHT - LEFT
# while if we write in +ve value it should be go like 0,1,2,3.... it start from LEFT -Right
print(players[-3])


            # RANGE
# to select  from where to where eg.
print(players[1:6])  # here we can see its start from mortal and ends with Delta 
 # another example  (from starting)
print(players[:2]) 

print(players[2:])

print(players[0:-5])

            # Checking value in List
        
# To determine if a specified item is present in a list use the       in     keyword:

if "Scout" in (players):
    print("Yes It's Exits")

# another example
if "MAxxy" in (players):
    print("Yes it's exits")
else:
    print("No it's Doesn't Exits")
    
    
        # changing value in list 
    
    
    # simply write the index number and edit the change      eg.
weapons=["akm","m416","Ump","Win94"]
weapons[2]="Kar98"
print(weapons)

 # within the range 
weapons[1:3]="AWM","Uzi"
print(weapons)


      # Insert Items
    # to insert items within the list without replacing the values.

# use INSERT (index value, values)

weapons.insert(2,"M416")
print(weapons)
 
         # To Add new Items
         
         
# to add new itmes we use append syntax.

weapons.append("AWM")
print(weapons)
            # OR
            # we can use the command insert(index value,value)
weapons.insert(6,"thomsan")
print(weapons)

            # to merge 2 lists 
            # we use  to merge 2 list so we use the command
            # Extend

utlities=["smoke Grenades","molotove cocktails","Stun Grenades"]
health=["Medkit","bandages","First Aid Kit","Energy Drink","Pain Killers"]
utlities.extend(health)
print(utlities)


            # to Remove
            
# to remove the values in a list we use the command remove()
colors=["red","green","Yellow","Black"]
colors.remove("green")
print(colors)

            # To remove specific index
del colors[2]
print(colors)
