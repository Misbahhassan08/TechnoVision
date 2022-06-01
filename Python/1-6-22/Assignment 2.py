# If Else:
# To find minimum number among from the 3 entered numbers.
print("Enter any three numbers :")
x=int(input())
y=int(input())
z=int(input())
if x<y<z:
    print("The minimum number is:",x)
elif x>y>z:
    print("The minimum number is:",z)
elif x>y<z:
    print("The minimum number is:",y)
elif x==y==z:
    print('Numbers are equal ')










# To find that user is applicable for scholarship or not.
a=int(input("Enter the percentage of marks :"))
if 60<=a<=100:
    print("Student is elegible for the scholarship:")
else:
    print("Student is ineligible for the scholarship:")






# To determine that entered number is Positive or Negative.
print("Enter any  numbers :")
b=int(input())
if b<0:
    print("Number is negative")
else:
    print("Number is positive :")
# To determine that entered character is vowel using OR operator.
c=input("Enter any character:")
if c=='a'or c=='e'or c=='i'or c=='o'or c=='u':
    print('Character is vowel')
else:
    print('character is consonent ')


# To find maximum number using AND operator.
print("Enter any  5 number ")
d=input()
e=input()
f=input()
g=input()
h=input()
if d>e and d>f and d>g and d>h :
    print ('Macimum number is ',d)
elif e>d and e>f and e>g and e>h:
    print ('Maximum number is ',e)
elif f>d and f>e and f>g and f>h:
    print("Maximum number is ",f)
elif g>d and g>e and g>f and g>h:
    print("Maximum number is ",g)
elif h>d and h>e and h>f and h>g:
    print("Maximum number is ",h)
else:
    print('Invalid Number ')




# To determine that number is positive or negative using NOT operator.
print("Enter any number ")
i=int(input())
if i !=-i:
    print('Number is nagative')
else :
    print("Number is positive ")






# To find eligibility for scholarship using Multiple IF condition.
a=int(input("Enter the percentage of marks :"))
if 80<=a<=100:
    print("Student is elegible for full scholarship:")
elif 60<=a<=80:
    print("Student is elegible for  half  scholarship:")
else :
    print('Student is ineligeble for scholarship')





# To find the square-root of an entered number using if condition.
print('Enter any number ')
j=float(input())
if j>0:
    print("Square root of number is:",(j**0.5))
else :
    print('Number is invalid :')
# To find that entered number is even or odd using if-else
print("Enter any number \n")
k=input()

if int (k)%2==0:
    print('Number is even')
else:
    print('Number is odd')


# To determine about leap year using if else condition.
print("Enter days of years:")
days=int(input())
if days==366:
    print("IT is  leap year ")

else:
    print("It is not a leap year")


# To print grade against marks using if-else-if statement.
print("Enter your marks out of 100")
l=int(input())
if 40<l<50:
    print("Your grade is E")
elif 50<l<60:
    print("Your grade is D")
elif 60<l<70:
    print("Your grade is C")
elif 70<l<80:
    print("Your grade is B")
elif 80<l<90:
    print("Your grade is A")
elif 90<l<100:
    print("Your grade is A++")
else:
    print("Your grade is F ")

# Switch:
# To determine about day using switch statement.

switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",

    }
print( switcher[1])

# To find the area or circumference of the circle using switch condition.
# To find the result of arithmetic operators using switch statement.
# To determine about vowels and consonants using switch statement.
# To print maximum number using conditional operator.
print("Enter any  5 number ")
d=input()
e=input()
f=input()
g=input()
h=input()
if d>e and d>f and d>g and d>h :
    print ('Macimum number is ',d)
elif e>d and e>f and e>g and e>h:
    print ('Maximum number is ',e)
elif f>d and f>e and f>g and f>h:
    print("Maximum number is ",f)
elif g>d and g>e and g>f and g>h:
    print("Maximum number is ",g)
elif h>d and h>e and h>f and h>g:
    print("Maximum number is ",h)
else:
    print('Invalid Number ')



# To calculate salary and tells the bonus using conditional operator.
Perhourincome=30
print('Kindly input the working hours and hour weeks :')
workinghours=input()
bonus=5000
if workinghours>45:

    print(salary=Perhourincome*(int(workinghours)+bonus ))
else:
    print(salary=Perhourincome*(int(workinghours)))


# Generic:
# Write a program that reads in five integers and then determines and prints the largest
print("Enter any three numbers :")
x=int(input())
y=int(input())
z=int(input())
if x<y<z:
    print("The lardest number is:",z)
elif x>y>z:
    print("The largest number is:",x)
elif x<y>z:
    print("The largest number is:",y)
elif x==y==z:
    print('Numbers are equal ')

# and the smallest integers in the group. Use only the programming techniques you have
# learned.
print("Enter any three numbers :")
x=int(input())
y=int(input())
z=int(input())
if x<y<z:
    print("The minimum number is:",x)
elif x>y>z:
    print("The minimum number is:",z)
elif x>y<z:
    print("The minimum number is:",y)
elif x==y==z:
    print('Numbers are equal ')

