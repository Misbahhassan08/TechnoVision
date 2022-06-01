'''Assignment 4
Date 30-5-2022'''
#Q! Write a  program to find maximum between two numbers.
'''This program refer to as finding of maximum number using if else along with comparator operator '''
print('Enter two numbers ')
#getting the input
x=int(input())
y=int(input())
#comparing two numbers
if x>y:
#printing Maximum number
    print('Maximum number is :',x)
elif y>x:
    print('maximum number is :',y)

#Q2 Write a  program to find maximum between three numbers.

'''This program refer to as finding of maximum between three numbers using if else along with comparator operator '''
print('Enter three numbers ')
#getting the input
x=int(input())
y=int(input())
z=int(input())
#comparing two numbers
if x>y>z:
#printing Maximum number
    print('Maximum number is :',x)
elif y>x>z:
    print('maximum number is :',y)
elif z>x>y:
    print('Maximum Number is :',z)
# Q3 Write a  program to check whether a number is negative, positive or zero.
'''This program refer to as finding weather the enter number is positive, negative or zero using if else condition'''
print('Enter any number :')
a=int(input())
#comparing number
if a>0:
#printing as positive if number is greater than zero
    print('Number is positive ')
#printing as negative if number is less  than zero
elif a <0:
    # printing as zero if number is equal to zero
    print('Number is negative')
elif a==0:
    print('Number is zero')

#q4 Write a  program to check whether a number is divisible by 5 and 11 or not.
'''This program is refer to as checking of number weather it is divisble by 5 or 11 in this program i have used 
modulus operator '''
print("Enter the number to check weather it is divisible by 5 or 11:")
b=int(input())
#if the remainder when number is divisible by 5 is zero it is divisble by 5
if b%5==0:
    print('Number is divisible by 5')
#if the remainder when number is divisible by 11 is zero it is divisble by 11
elif b%11==0:
    print('Number is divisible by 11 ')
#if the remainder when number is divisible by 5 or 11  is not  zero it is not divisblle by 5 or 11
else :
    print  ("Number is not divisible by 5 and 11")
#Q5 Write a  program to check whether a number is even or odd.
'''This program is refer to as checking of even or odd of the input number '''
print('Enter any number ')
c=int(input())
#if the remainder of the number when it is divided by 2 is zero it will be even number
if c%2==0:
    print('Number is even')
#if the remainder of the number when it is divided by 2 is not  zero it will be odd number
else:
    print("Number is odd")
#Q6 Write a  program to check whether a year is leap year or not.
'''This program is refer to as finding of leap year 
Leap year is the year in which there are 366 days '''
print('Enter number odf days ')
d=int(input())
if d==366:
    print('The year leap year')
elif d==365:
    print(' It is a normal Year ')
#Q7 Write a  program to input any alphabet and check whether it is vowel or consonant.
'''this program is refer to as checking of albhabets weather it is vowel or consonent  '''
print('Enter any alphabet')
e=input()
#if the input alphabetare are 'a' e' i' o ' u' then it is vowel
if e=='a' or e=='i' or e=='e' or e=='o' or e=='u':
    print('Alphabet is vowel')
#otherwise it is consonant
else :
    print("Alphabet is consonent ")
# Write a  program to input week number and print week day.
'''this program is refer to as printing of week days correspond to week number '''
print('Enter day number ')
f=int(input())
if f==1:
    print('Monday')
elif f==2:
    print('Tuesday')
elif f==3:
    print('Wednesday')
elif f==4:
    print('Thursday')
elif f==5:
    print('Friday')
elif f==6:
    print('Saturday')
elif f==7:
    print('Sunday')
else:
    print("invalid day ")
#Q9 Write a  program to input month number and print number of days in that month.
'''this program is refer to as printing of Month name  correspond to month number '''
print('Enter month number  ')
f=int(input())
if f==1:
    print('January ')
elif f==2:
    print('Feburary')
elif f==3:
    print('March')
elif f==4:
    print('April')
elif f==5:
    print('May')
elif f==6:
    print('June ')
elif f==7:
    print('July')
elif f==8:
    print('August')
elif f==9:
    print('September')
elif f==10:
    print('October')
elif f==11:
    print('November ')
elif f==12:
    print('December ')

else:
    print("invalid month ")
#Q10 Write a  program to input angles of a triangle and check whether triangle is valid or not.
'''This program is refer to as checking of validity of triangle and we know that the sum of angles of trianles are 
not greater than 180 so if the sum of angles of triangles are greater than 180 it is consider invalid '''
print("Enter three angles of triangles ")
g=int(input())
h=int(input())
i=int(input())
if 0<g+h+i<=180:
    print('Triangle is valid')
else:
    print('Triangle is invalid')
#Q11 Write a  program to input all sides of a triangle and check whether triangle is valid or not.
'''This program is also refer to as checking the validity of triangle if the number of sides 
of triangle are equal
to 3 then it is refer to as valid one otherwise it is invalid '''
print('Enter the number of sides of triangle')
j=int(input())
if j==3:
    print("Triangle is valid ")
else:
    print("Triangle is invalid ")
# Write a  program to check whether the triangle is equilateral, isosceles or scalene triangle.
''' This program is refer to as checking the type of triangle 
If all the three sides of triangle are equal it is Equaleteral Triange
if two sides of triangles are equal it is isoceles triangle
if all the sides of triangles are unequal it is scalene triangle'''
print('Enter the length of all sides of triangle ')
k=int(input())
l=int(input())
m=int(input())
if k==l==m:
    print('Equilateral triangle')
elif k==l or l==m or m==k:
    print('Isosceles Triangle ')
elif k!=l or l!=m or m!=k:
    print('Scalene Triangle ')
#Q13 Write a  program to find all roots of a quadratic equation.
'''Don't know '''
#Q14 Write a  program to calculate profit or loss.
'''This program is refer to as calculation of profit and loss 
since we know the formula for profit and loss so it is easily be calculated '''
print('Enter sale price :')
saleprice=int(input())
print('Enter cost Price:')
costprice=int(input())
profit=saleprice-costprice
loss=costprice-saleprice
print('The Profit is ',profit)
print('The loss is ',loss )


#Q15 Write a  program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
'''This program is refer to as calculation of grade of student correspondence to its percentage '''
print('Enter marks for Physics,chemistry,Biology,Mathematics and Computer sciencerespectively;')
physics=int(input())
chemistry=int(input())
biology=int(input())
mathematics=int(input())
computer=int(input())
percentage=((physics+chemistry+biology+mathematics+computer)/500)*100
if percentage>=90:
    print('Grade A')
elif percentage>=80:
    print('Grade B')
elif percentage>=70:
    print('Grade C')
elif percentage>=60:
    print('Grade D')
elif percentage>=50:
    print('Grade E')
elif percentage>=40:
    print('Grade E')
elif percentage<40:
    print('Grade F')

# Q16 Write a  program to input basic salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%
'''This program is refer to as calculation of gross salary on the basis of base salary '''
print("Enter the basic salary:")
HRA=1000
DA=1000
basesalary=int(input())
if basesalary<=10000:
    grosssalary=(20/100)*HRA+(80/100)*DA
    print('ross salary is ',grosssalary+basesalary)
elif basesalary<=20000:
    grosssalary = (25 / 100) * HRA + (90 / 100) * DA
    print('ross salary is ', grosssalary+basesalary)
elif basesalary>20000:
    grosssalary = (30 / 100) * HRA + (95 / 100) * DA
    print('ross salary is ', grosssalary+basesalary)
# Write a  program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
#This program is refer to as calculation of Electricity bill on the basis of units consumed
#the user will just enter the number of units which are consumed and this program will automatically calculate
#electricity bill
print('Enter number of Units')
u=int(input())
if 0<u<50:
    print('Your Bill is ',bill1=0.5*u)
elif 50<u<150:
    print('YOUR BILL IS :',bill2=0.75*100+(0.5*u))
elif 150<u<250:
    print("Your bill is :",bill3=1.20*100+0.75*100+(0.5*u))
elif u>250:
    print("Your bill is :",bill4=1.50*u+(20/100)*u)
