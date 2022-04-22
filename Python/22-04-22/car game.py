x=""
while x!="quit":
    x = input("> ").lower()

    if x.lower()=="start":
        print("car is started")
    elif x.lower()=='stop':
        print('Car is stopped')
    elif x.lower()=='quit':
        print('Game is quitted ')
    elif x.lower() == 'help':
        print(''''
        Stop: To Stop
        Start: To start
        Quit :To quit the game ''')
    else:
        print("I don't understand")



