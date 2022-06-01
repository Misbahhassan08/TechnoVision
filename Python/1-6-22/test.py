# 2. Accept the age of 4 people and display the youngest one?
'''this program is refer to as finding the younger one among the 4 persons
we are getting the input of 4 persons ae and then compared them using if else and printing the smaller one '''
print('Enter age of 4 persons :')
a=int(input('person 1 age\n'))
b=int(input('person 2 age\n'))
c=int(input('person 3 age \n'))
d=int(input('person 4 age\n'))
if a<b<c<d:
    print('Younger one is ',a)
elif b<a<c<d:
    print('Younger one is ',b)
elif c<b<a<d:
    print('Younger one is ',c)
elif d<b<c<a:
    print('Younger one is ',d)
elif a==b==c==d:
    print("All have same ages ")
else:
    print('invalid input ')