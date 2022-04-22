weight=int(input("Enter Weight:"))
unit=input("Lbs(L) or KGs(K)")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"You are {converted}Kilos")
elif unit.upper()=='K':
    converted=weight//0.45
    print(f"You are {converted}Lbs")

