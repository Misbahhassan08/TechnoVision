try :
    age=int(input("Enter the age:"))
    income =20000
    risk=income / age
    print("Your age is ",age)
    print('Your risk is :',risk)
except ZeroDivisionError:
    print('Age cannot be zero')
except  ValueError:
    print("Invalid Value ")
