#insert item at list
numbers=[1,2,5,7,9]
numbers.append(13)
print(numbers)
#InsertMethod
numbers.insert(0,9)
print(numbers)
#remove items fro,m list
numbers.remove(9)
print(numbers)
#clears the items in the lists
#numbers.clear()
print(numbers)
#Check the Availability oif the itens
print(numbers.index(2))
print(13 in numbers )
#count the numbers how many time a number repeat in a list
print(numbers.count(5))
#sort our list
numbers.sort()
print(numbers)
#reverse the list
numbers.reverse()
print(numbers)