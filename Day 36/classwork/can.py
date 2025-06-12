#1
can = input("enter name: ")


print(can.upper())
print(can.lower())
print(can.capitalize())


#2
can = "bla bla"

can1=input("neter words: ")

can2 = can.find(can1)

if can2 != -1:
    print(can1  + " - "  + str(can2))
else:
    print("This symbol is not in word")