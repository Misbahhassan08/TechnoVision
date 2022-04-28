phone=input("Phone:")
digit_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"Four"

}
for ch in phone:
    print(digit_mapping.get(ch,"!"))