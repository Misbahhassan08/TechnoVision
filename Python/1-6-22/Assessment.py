'''i want ot print this using multiple or nested loop
*************************
** University of Gijrat**
*************************
'''

'''firstly i will initialize the for loop
then in that loop i will print the first line
i- ***************************
'''
#Just initializing the array since i am not using the range function
'''In second loop i will print 
**University of Gijrat**'''
'''In the third loop i will print 
 *******************************'''

for x in range(1):
        print('*'*25)
        for y in range(1):
                print("**University of Gujrat**")
                for z in range(1):
                        print('*'*25)
                x=x+1
                y=y+1
                z=z+1



# Print String Reverse in reverse order E.g Input : Pakistan OutPut : natsikap
'''In this question i want to print reverse of string
'''
y=input('Enter any string')
for k in y:
    if k<y:
        print(y)






#Q#3 To print right side diagonal.

i=0

while i<5:
    j=0
    while j<5:
        if i==j:
            print('*')
        else:
            print(' ')










#Q4 To print down-side triangle.
'''This question refer to printing of down side 
triangle i have done this question using both while and for loop as well '''
#(Though while Loop)
i=0 # initialization of index
while i <=5:
    print('*'*i)
    i=i+1
#through for loop
i=[1,2,3,4,5]
for k in i:
    print('*'*k)
    k=k+1



# Calculate Factorial of any giver number
#we know that the factorial is equal to x!=x*x-1;

x=int(input('Enter any number to find its factorial'))
xfact=x*(x-1)
print(xfact)
