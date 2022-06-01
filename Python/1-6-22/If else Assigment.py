'''Assignemt om if else and Logical operators
 Date 28/5/2022'''
# If Else:To find minimum number among from the 3 entered numbers.minimum number
#This program is refer to as if else condition which 3 numbers are compared and printed the
x=int(input())
y=int(input())
z=int(input())
if x<y<z:
    print("Minimum number is ",x)
elif y<x<z:
    print('Minimum number is ',y)
elif z<x<y:
    print('Minimum number is ',z)
elif x==y==z:
    print('Numbers are equal')

# To find that user is applicable for scholarship or not.
#This program is refer to as scholarship eligibility checker in which i have checked the percentage of student
#and if the percentage is above 60 then student is eligible otherwise he is not
b=input('Enter the percentage of student')
if 60<b<100:
    print('Student is eligible for the Scholarship')
else:
    print("Student is not Elegible for scholarship")
# To determine that entered number is Positive or Negative.
#In this program i have checked whether the number is negative or positve by using the conditional operator
a=int(input("Enter any number "))
#if the number is greater than zero it will be positve number else it will be negative
if a<0:
    print("Number is Negative")
else:
    print('Number is positve ')
# To determine that entered character is vowel using OR operator.
#In this program i have implemented the OR operator o check the character
c=input("Enter the character to find whether it vowel or not")
#if it is belong to a,e,i,o,u it will be vowel otherwise it will not be a vowel
if c=='a'or'e'or'i'or'o'or'u':
    print('Charater is vowel')
else:
    print("Character is not vowel")
# To find maximum number using AND operator.
# in this program i have implemented the And operator  to find the maximum number
print('Enter three  numbers ')
d=int(input())
e=int(input())
f=int(input())
# these numbers are compared with each other and maximum number will be printed
if d>e and f:
    print('Maximum number is ',d)
elif e>d and f :
    print('Maximum number is ',e)
elif f>d and e:
    print('Maximum number is ',f)


# To find eligibility for scholarship using Multiple IF condition.
# this question is similar to above one but here i have implemented the multiple or nested if conditions
#to find the student eligibility for the scholarship
print('Enter percentage of student ')
h=int(input())
if 60<h<70:
    print('Student is eligible for partial scholarship')
elif 70<h<80:
    print('Student is eligiblr for full scholarship')
elif 80<h<100:
    print("Student is available for full scholarship along with 20000 stipend ")
else:
    print("Student is not Eligible")
# To find the square-root of an entered number using if condition.
# In this question i have found the square root of number by using the if condition
i=int(input("Enter any number to find its squre root "))
if i>0:
    print(i**0.5)
else:
    print('Square not possible ')
# To find that entered number is even or odd using if-else
#In this code i am using the modulus operator along with if else condition for finding the even and odd number
print("Enter any number \n")
j=input()
#here if the remainder of number when it is divided by 2 is zero it even
if int (j)%2==0:
    print('Number is even')
    #else it is odd
else:
    print('Number is odd')
# To determine about leap year using if else condition.
#HEre if the number of days are 365 the year is normal
k=int(input())
#Otherwise it will be leap year
if k ==366:
    print('It is Leap year ')
elif k==365:
    print('It is a normal year ')
else:
    print("Please enter valid days ")
# To print grade against marks using if-else-if statement.If Else:
#In this program i have printed grades for students using the if else condition
print('Enter percentage of student ')
h=int(input())
#print grade C if the percentage is between 60 and 70
if 60<h<70:
    print('Grade C')
#print grade B if the percentage is between 70 and 80
elif 70<h<80:
    print('Grade B ')
#print grade A if the percentage is between 80 an 100
elif 80<h<100:
    print("Grade A ")
else:
    print("Student is Fail")


