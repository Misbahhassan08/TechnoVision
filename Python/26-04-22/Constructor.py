class Person:
    #Calling contructor
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("talk")
John=Person("Faizan Rafique")

print(John.name)