#1)
#.upper() windadebis yvelka sos adidebs .lower() apataravebs .capitalize() pirvel asos adidebs marto .find() ki frcxilebis shignit chawerili aso romel indexshia imas achvenebs

#2)
can = input("enter name: ")

print(can.lower())

#3)

can = input("enter email: ")

can1=can.find("@")

if can1 >= -1:
    print(can.upper())

#4)

can = input("neter book name")

print(can.title())

#5)
can = input("enter word: ")
can1 = input("enter word: ")

print(can.count(can1))

#6)
can = input("enter word: ")

if can == can.upper():
    print(can)
else:
    print(can.upper())