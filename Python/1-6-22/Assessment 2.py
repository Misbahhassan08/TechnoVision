'''Assignment 2
Daate:27/5/2022
Topics Covered are
- Casting
- Numbers
- Strings
- Booleans
- Operators'''


# 1. User Aritchmetic Operators
#in this program i had used Arithematic operations
x=1
y=2
#Applying arithematic operation
z=x+y*y/x
#printing value after Arithematic operation
print('After Arithematic Operation  :')
print(z)






# 2. User Compound assignment Operators
# In this solution i have used the assignment operator

x=3
y=4
#here is the use of assignment operator
x==y==2
print(x,y)
# 3. User Increement Operators with prefix /postfix
#here is the use of prefixes of increment
x+=1
#here is the postfix of increment operator
y=+1
print('The incremented numbers with prefix :\n')
print(x)
print('The incremented numbers with postfix :\n')
print(y)





# 4. To find salary on the behalf of working hour and hour week
#So in this solution i have manually fix the values of Rate Hour , hour week and working hour
Rateofhour=5
hourweek=5
workinghours=20
#here i am finding the salary by multiplying hour rate with total working hours and adding hours week means number of hours on week days
salary=Rateofhour*(int(workinghours)+hourweek)
print('Your salary is \n')
print(salary)






# 5. To find salary by getting input such as working hour and hour week.
#So in this solution i hgetting the values of Rate Hour , hour week and working hour automatically from user
hourrate=30
print('Kindly input the working hours and hour weeks :')
workinghours=input()
hourweeks=input()
#here i am finding the salary by multiplying hour rate with total working hours and adding hours week means number of hours on week days
salary=hourrate*(int(workinghours)+int(hourweeks))
print('Your salary is \n')
print(salary)







# 6. To find reverse of any input number.
print("Enter any two number :\n")
# num=input()
first=input()
second=input()
# In this solution i have used a format string to print the reverse of the number
print( "Reverse of number is ")
#format is the builtin method for string to set the format for string
print(format(second),(first))








# 7. To find the number is even or odd by using arithmetic operator "%".

#In this code i am using the modulus operator for finding the even and odd number
print("Enter any number \n")
x=input()
#Basically the if condition is used to define the logic for even and odd number if the remainder for a number when it is devided by two is zero it is evem

if int (x)%2==0:
    print('Number is even')
#otherwise it is odd
else:
    print('Number is odd')







# 8. Write a program which reads a character from the keyboard and writes out its ASCII representation.
#--------NOT RELATED TO TOPIC --------------------------------------
# Write a program to read Fahrenheit temperatures and print them in Celsius. The formula is
# C = (5/9)(F - 32)
print('Enter the temperature in farenheit:\n')
#In this code i am getting the farenheight as input
f=input()
#And converting that into centigrade by using the formula
C = (5/9)*(int(f) - 32)
print('Temperature in Centigrade is :\n')
print(C)






# 9. Write a program that reads in the radius of a circle and prints the circle’s diameter,
# circumference and area. Use the value 3.14159 for “pi”.
'''This program is abouit calculation of area and circumference of circle .In this program i had taken radius as input
user then implemented formula for the calculation area and circumference respectively'''
#This program is similar to last assignment but there is a slight change of printing diameter here
print("Enter the radius of circle \n")
r=int(input())
pi=3.14159
#Applying formulas for diameter circumference and area
circumference=2*pi*r
diameter=2*r
area=pi*r*r
print("The Diameter ,area and circumference of a circle are as follows\n")
print(diameter)
print(area)
print(circumference)






# 10. To find that you have entered exact digit or not .
#In this program i have used if condition for finding the exact digit
print("enter any number\n")

e=input()
#The logic behind finding the exact number is that : if the number is exactlly divisible by 1 it will be exact number
if int(e)%1==0:
    print('Number is Exact ')
else:
#Otherwise it will not be an exact number may be a decimal one
    print('Number is not exact ')





# 11. To find that entered number is even or odd.
#This is the repeat questionso here i have applied the same logic as it is in question 7
print("Enter any number \n")
a=input()

if int (a)%2==0:
    print('Number is even')
else:
    print('Number is odd')