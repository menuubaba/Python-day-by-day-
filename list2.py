         #  LOOP Through List
mobile=["Apple","Samsung","MotoRola","Realme"]
for i in mobile:
    print(i)
    
    # List Comparison 
    # to check the value are present in the list is or not   eg.
animals=["Horse","Lion","Giraffe","Camel"]
wild=[]
for a in animals:
  if "Lion" in a:
   wild.append(a)
print(wild)  



number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 1, 23, 234, 12, 5, 78, 21, 1]
abc = []

for x in number:
    if x%2==0:
        abc.append(x)
        print(x)
        
number =['a','b','asdasd']
alpha=[]
for y in number:
    if 'a' in number:
        alpha.append(y)
        print(alpha)
        
        
        # SORTING 
        # To sort the sequenceof the values in a list by  small to big 
number1=[9,2,3,1,2,532,21,14,64,74,23,2,4,6,7,4,2,23,53,53,21,6,5,4,45,546,1,2,4,4,5,2]
number1.sort()
print(number1)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)