# #1
# can = input("neter word: ")

# result = 0

# for i in can:
#     if i == " ":
#         result += 1

# print(result)

# #2
# can = ["can","leila","bela","nika","gio"]

# words = input("enter word: ")
# numbers = int(input("enter numbers: "))

# can.insert(numbers,words)

# print(can)

# #3
# can = input("enter campelcase world: ")

# result=""

# for i in can:
#     if i.isupper():
#         result += " " + i.lower()
#     else:
#         result += i

# print(result)

# #4
# can = input("enter world: ")

# result=""

# for i in can:
#     result += i
#     if i == " ":
#         result += "_"
#     else:
#         result += i

# print(result)


#5
names=[]
words=[]

for i in range(5):
    name = input("enter name: ")
    names.append(name)

for i in names:
    for i in name.lower():
        if i in "bcdfghjklmnpqrstvwxyz":
            words.append(i)

a = sorted(set(words))

print(a)