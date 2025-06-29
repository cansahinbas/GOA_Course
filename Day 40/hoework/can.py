#1
can = input("neter word: ")

result = 0

for i in can:
    if i == " ":
        result += 1

print(result)

#2
can = ["can","leila","bela","nika","gio"]

words = input("enter word: ")
numbers = int(input("enter numbers: "))

can.insert(numbers,words)

print(can)

#3
can = input("enter campelcase word: ")

result=""

for i in can:
    if i.isupper():
        result += " " + i.lower()
    else:
        result += i

result = result.capitalize()

print(result)

#4
can = input("enter word: ")

result=""

for i in can:
    result += i
    if i == " ":
        result += "_"
    else:
        result += i

print(result)

#5
names=[]
list1=[]
other=[]

for i in range(5):
    name = input("enter name: ")
    names.append(name)

for name in names:
    for i in name:
        if i in "bcdfghjklmnpqrstvwxyz":
            list1.append(i)

for i in list1:
    if i not in other:
        other.append(i)

other.sort()
print(other)
