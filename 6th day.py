# Strings in Python 
'''
A string is like a sentence in Python. 
It's made up of letters, numbers, 
or symbols enclosed in quotes (single or double)
'''
name ="Joseph"
friend = "Stalin"
anotherfriend="Adolf"
print(name,friend,anotherfriend)

''' if we want to write in the forms of paragraph  or we can 
say that multi line string 
so we will use (''' ''') example''' 
 
foods = """my favorite foods are
dosa
Idli
Allo paratha....
"""
print(foods)


cod="""Call of Duty is a popular first-person shooter (FPS) 
video game franchise known for its fast-paced action,
intense multiplayer matches, and immersive single-playercampaigns.

The series covers various historical and futuristic settings, offering
a wide range of gameplay experiences.
"""
print(cod)

#  to print the specific word in a string  
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


# here how it's count 0,1,2,3,4 = total 5
# so if we  write Adolf so so total is 5 but machine will count 4 & (n-1) total -1 


 # Length
'''  to find the total no. of character in a string or in a paragraph 
 So the syntax is Len'''

notice=""" Here all the student are imformed that 
 our School is going to organise Sports Day on 12th Aug ,
 Instrested Student given their name to respective class Teacher 
  Thank You"""
len1=len(notice)
print(len1)
print(notice[20]) #here  it count 20 character including space 