'''Assignment 4
Date:31/5/2022'''
# 1. Accept the temperature in degree Celsius of water and check whether it is boiling or not
# (boiling point of water in 100 oC.
'''This program is refer to as checking whether the water is boiling or not just getting temperature as input 
 if water temperature is 100 degree it is boiling else it is not '''
print("Enter the temperature of water ")
a=int(input())
if a>=100:
    print('Water is boiling ')
else :
    print('Water is not boiling ')
# 2. Accept the age of 4 people and display the youngest one?
'''this program is refer to as finding the younger one among the 4 persons 
we are getting the input of 4 persons ae and then compared them using if else and printing the smaller one '''
print('Enter the age of 4persons:')
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a<b<c<d:
    print('Younger one is person 1 ')
elif b<a<c<d:
    print('Younger one is person 2')
elif c<a<b<d:
    print('Younger one is person 3')
elif d<a<b<c:
    print('Younger one is person 4')



# 3. Write a program to check whether a number  is prime or not.
'''This question is related to finding the prime number so i am not sure about this logic 
 thats the best i can do '''
print("Enter the number to check whether it is prime or not ")
e=int(input())

if e%2==0 or e%3==0 or e%5==0 or e%7==0 or e%11==0:
    print(' Number is not prime')
else  :
    print('Number is prime ')
# 4. Write a program to check a character is vowel or not.
'''this program is refer to as checking of albhabets weather it is vowel or consonent  '''
print('Enter any alphabet')
e=input()
#if the input alphabetare are 'a' e' i' o ' u' then it is vowel
if e=='a' or e=='i' or e=='e' or e=='o' or e=='u':
    print('Alphabet is vowel')
#otherwise it is consonant
else :
    print("Alphabet is consonent ")

# 5. A company decided to give bonus to employee according to following criteria:
# Time period of Service                Bonus
#     More than 10 years             10%
#     >=6 and <=10                   8%
#     Less than 6 years              5%
#     Ask user for their salary and years of service and print the net bonus amount.
'''This program is refer to as getting the input of salary and years of service then 
printing the bonus of employees with reference to years of experience '''
print('Enter the salary:')
salary=int(input())
print('Enter the years of service :')
years=int(input())
if years>10:
    bonus=salary*(10/100)
    print('Your bonus is ',bonus)
elif 6<=years<=10:
    bonus=salary*(8/100)
    print('Your bonus is ',bonus)
elif years<6:
    bonus=salary*(5/100)
    print('Your bonus is ',bonus)


# 6. Accept the number of days from the user and calculate the charge for library according to following
# 	Till five days : Rs 2/day.
# 	Six to ten days  : Rs 3/day.
# 	11 to 15 days  : Rs 4/day
# 	After 15 days    : Rs 5/day
'''This program is refer to as calculation of charges of book return after particular days '''
print('Enter the numbers of days ')
days=int(input())
#Simply user get input of numbers of days
if days <=5:
#then days are multiply by per day charges mentioned in the program
    charges=2*days
    print('Your charges are',charges)
elif 6<=days<=10:
    print('Your Charges are :',charge=3*days)
elif 11<=days<=15:
    print('Your Charges are :',charge=4*days)
elif  15< days :
    print('Charges are :', charge=5 * days)

# 7. Accept the kilometers covered and calculate the bill according to the following criteria:
# 	First 10 Km              Rs11/km
# 	Next 90Km               Rs 10/km
# 	After that               Rs9/km
'''this program is refer to as calculation of bill w.r.t kilometer travelled '''
print('Please Enter the kilometer you have travelled :')
kilometers=int(input())
if kilometers<10:
    '''for first 10 kilometer cost will be 11 rs per kilometer'''
    bill = 11 * kilometers
    print('Your bill is ',bill)
elif 10< kilometers<100:
    '''for next 90 cost will be 10 rs per kilometer '''
    bill = 10 * kilometers + 11 * 10
    print('Your bill is ',bill)
    '''for rest 9 rs per kilometer '''

elif kilometers>100:
    bill = 9 * (kilometers-100)+(10 * 90) + 11 * 10
    print('Your bill is',bill)
# 8. Accept the marks of English, Math and Science, Social Studies Subject and display
# the stream allotted according to following
# 	All Subjects more than 80 marks —       Science Stream
# 	English >80 and Math, Science above 50 –Commerce Stream
# 	English > 80 and Social studies > 80    —   Humanities
'''This program is refer to as classification of student on the basis of their marks in particular subjects'''
print('Enter the marks of English,Math ,Science,Social studies respectively:')
English=int(input())
Math=int(input())
Science=int(input())
Socialstudies=int(input())
if English > 80 and Math>80 and Science >80:
    print('Student is in Science Stream')
elif English>80 and Math>50 or Science >50:
    print('Student is in commerce stream')
elif English > 80 and Socialstudies > 80:
    print('Student is in Humanities ')
# 9. Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :
#      Unit                                                     Price
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
#This program is refer to as calculation of Electricity bill on the basis of units consumed
#the user will just enter the number of units which are consumed and this program will automatically calculate
#electricity bill

print('Enter number of Units')
u=int(input())
if 0<u<100:
    bill = 0
    print('Your Bill is ',bill)
elif 100<u<200:
    bill = 5*u
    print('YOUR BILL IS :',bill)
elif 200<u:
    bill=10*(u-200)+5*100
    print("Your bill is :",bill)
