# Write a Python Program to Check weather a Given Number is odd or Even
'''
num=int(input("Enter the number:"))
if num%2==0:
            print("Even")
else:
  print("Odd")
  '''
  # 2.Check weather a candidate Eligible for Vote or not.
'''
vote=int(input("Enter Your Age:"))
if vote >=18:
    print("You are Eligible to vote")
else:
    print("Not Eligible")
    '''
    #3.  check weather Given Number is Divisible by 7 or Not.
'''
num=int(input("Enter the Number: "))
if num%7==0:
    print("It's Divisible by 7")
else:
    print("The No. is't divisible")
    '''
  #4 program to display “Hello” if a number entered by user is a multiple of five , otherwise print “Bye”
'''
num=int(input("Enter the No:"))
if num%5==0:
    print("Hello")
else:
    print("Bye")
    '''
  #5. program to accept percentage from the user and display the grade according to the following **
'''** criteria:
** Marks Grade**
marks > 80: A+ grade
marks > 70 : A grade
marks > 60: B grade
** marks > 50: C grade**
else Failed.'''


'''
score=float(input("Enter the percentage:"))

if score >=50 and score<60:
    print("C grade")
    if score >60 and score <70:
        print("B grade")
if score >70 and score<80:
    print("A grade")
if score >80:
    print("A+ grade")
else:
    print("Failed")
'''
# 6 program that interprets the Body Mass Index (BMI) based on a user’s weight and height.
'''It should tell them the interpretation of their BMI based on the BMI value.
• Under 18.5 they are underweight
• Over 18.5 but below 25 they have a normal weight
• Over 25 but below 30 they are slightly overweight
• Over 30 but below 35 they are obese
• Above 35 they are clinically obese.

The BMI is calculated by dividing a person’s weight (in kg) by the square of their height (in m) .
Take height and weight from the user.

            Answer:

height=float(input("Enter your height (in cms):"))
weight=float(input("Enter your weight (in kg):"))
bmi=(weight/height)
if bmi <= 18.5:
    print("Underweight")
if bmi >=18.5 and bmi <=25:
    print("Normal")
if bmi >25 and bmi <30:
    print("Slightly Overweight")
if bmi >30 and bmi <35:
    print("Obese")
if bmi >35:
    print("Clinically obese")
    '''
    
    #7 program to calculate the electricity bill (accept number of unit by the user )
    #according to the following criteria 
''' Unit price
first 100 units No Charge
next 100 units Rs 5 rupees per unit
after 200 units Rs 10 rupees per unit
( For Example if units is 350 than total bill amount is Rs 2000)
'''

unit = int(input("enter the units:"))
amount=0
if unit<100:
 print("No Charge")
elif 100< unit <=200:
 amount+=(unit-100)*5
 print("bill is" , amount)
elif unit>200:
 amount = 500+ (unit-200)*10
 print("bill amount is" , amount)