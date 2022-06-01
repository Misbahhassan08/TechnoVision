# 1. User Aritchmetic Operators
x=1
y=2
z=x+y
print('sum is :')
print(z)


# ----------Assignment #2 starting  from here--------

# 2. User Compound assignment Operators
x==3
y+=4
# 3. User Increement Operators with prefix /postfix

x+=1
y=+1
print('The incremented numbers with prefix :\n')
print(x)
print('The incremented numbers with postfix :\n')
print(y)

# 4. To find salary on the behalf of working hour and hour week
Perhourincome=30
hourweek=5
workinghours=20

salary=Perhourincome*(int(workinghours)+hourweek)
print('Your salary is \n')
print(salary)
# 5. To find salary by getting input such as working hour and hour week.
Perhourincome=30
print('Kindly input the working hours and hour weeks :')
workinghours=input()
hourweeks=input()

salary=Perhourincome*(int(workinghours)+int(hourweeks))
print('Your salary is \n')
print(salary)

# 6. To find reverse of any input number.
print("Enter any two number :\n")
# num=input()
first=input()
second=input()
# str(num)
# print(str(num)[::-1])#[start:end:step]
print( "Reverse of number is{second} {first} ".format(second, first))


# 7. To find the number is even or odd by using arithmetic operator "%".
print("Enter any number \n")
p=input()

if int (p)%2==0:
    print('Number is even')
else:
    print('Number is odd')


# 8. Write a program which reads a character from the keyboard and writes out its ASCII representation.
print("Enter any character\n")
c=input()
print("The ASCII value of '" + c + "' is", ord(c))
# Write a program to read Fahrenheit temperatures and print them in Celsius. The formula is
# C = (5/9)(F - 32)
print('Enter the temperature in farenheit:\n')
f=input()

C = (5/9)*(int(f) - 32)
print('Temperature in Centigrade is :\n')
print(C)
# 9. Write a program that reads in the radius of a circle and prints the circle’s diameter,
# circumference and area. Use the value 3.14159 for “pi”.
print("Enter the radius of circle \n")
r=input()
pi=3.14159
circumference=2*pi*float(r)
diameter=2*float(r)
area=pi*float(r)**2
print("The Diameter ,area and circumference of a circle are as follows\n")
print(diameter)
print(area)
print(circumference)
# 10. To find that you have entered exact digit or not .
print("enter any number\n")
e=input()
def cal():
    if int(e)%2==0:
        return True
    else:
        return False
print (cal())
# 11. To find that entered number is even or odd.
print("Enter any number \n")
p=input()

if int (p)%2==0:
    print('Number is even')
else:
    print('Number is odd')