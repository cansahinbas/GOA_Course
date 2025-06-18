#1
#.append gamoiyeneba im dros roca gvinda ragacis damateba siashu
#.insect ki akonkretebs romel indexshi unda davamatot 
#.pop ki romel indexsac vutitebs imas auqmebs

#2
can=[1,2,3,4,5,6,7,8,9,10]

print(len(can))

#3
can=[]

for i in range(5):
    can1=int(input("enter numbers: "))
    can.append(can1)

print(can)

#4
colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop(4)
print(colors)

#5
animals = ["dog", "cat", "elephant", "lion"]

animals.insert(1,"Mankey")

#6
can = []

for i in range(3):
    can1 = input("enter student name")
    can.append(can1)

can.insert(0,"Teacher")
can.pop(2)
print(len(can))
print(can)