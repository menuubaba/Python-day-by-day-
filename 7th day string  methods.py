 # String Method
a="Charlie Chaplin is a great actor"
len(a)
print(a)

# Upper Case 
print(a.upper())

#lower case
print(a.lower())

# Replace 
print(a.replace("great", "legend"))


#center 
print(a.center(50,"."))


#count (count repreated words) eg.
b="Abcdeffghabcacsr"
count=b.count("a")
print(count)


# startwith 
str2=""" battle ground Mobile India (BGMI)
is the best game in India 
and there are more than 5million downloads 
"""
print(str2.startswith("India"))

#end with  (the character or the word end with specific word in numbers ) eg.
str1=""""Welcome to my World:
    This world is cruel
    but i love my world"""
print(str1.endswith("world"))



# Find 
'''to find the a world but it will tell the place in the form of numbers eg.'''
d="I am an Athiest "
print(d.find("an"))


