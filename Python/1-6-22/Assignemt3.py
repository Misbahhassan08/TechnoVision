# To print the message "Red" 10 times using for loop.
for k in range(0,10):
    print('red')

# To print first five odd numbers using for loop.
for a in range (0,5):
    print(2*a+1)
# To print the sum of given numbers using for loop.
a=3
b=5
for x in range(a,b):
    x=a+b
print('Sum of two numbers are ',x)

# To calculate the square-root given numbers using for loop.
print("Enter any number to find its square root:")
c=int(input())
for i in range(c):
     y=c**0.5
print("Square root of number is ",y)
# To print the table of the given number using for loop.
print("Enter any number to find its table")
x=int(input())
for i in range(1,11):
    y=i*x
    i+=1
    print(y)

# To find the factorial given number using for loop.
print("Enter any number to find its factorial")
x=int(input())
y=1 #initialization of factorial
for i in range(1,x+1):

    y=i*y

print(y)

# To print the text within the boxes using multiple for loop.


# To print right side diagonal.




# To print left side diagonal.
i=0 #row value
j=4 #col value
for row in range(5):
    for col in range(5):
        if i==row and j==col:
            print('*')
            i=i+1
            j=j-1
        elif row==col:
            print('*')
        else:
            print(' ')
# To print the cross sign or symbol.
i=0
j=4
for row in range(5):
    for col in range(5):
        if i==row and j==col:
            print('*')
            i=i+1
            j=j-1
# To print right side triangle.


for k in range (0,5):
    print(('*'*k))
    k=k+1



# To print down-side triangle.
a=5 #Number of rows
for k in range (0,a):
    print(('*'*a))
    a=a-1


# To print the symbol (#).




# To print the sum in a matrix shape using for loop.
for j in range(0, 5):
    print(j)
    for k in range(0, 5):
        print(k)
    print('\n')
# To check marks validation using do while loop
