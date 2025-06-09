#1
numbers = [1,2,3,4,5,6,7,8,9,10]



for i in numbers:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

#2

names = ["can","nika","dato","saba","leila","gio","ahmet","mstafa","alexsandre","bela"]

for i in names[1::2]:
    print(i)

#3
name = "goa"

bla= 0

bla1=1

for i in name:
    print(name[bla]  +  "-"  +  str(bla1) )
    bla=bla+1
    bla1=bla+1


#4

numbers1=[1,2,3,4,5,6,7,8,9,10]

bla_bla=0

num=-1

while  bla_bla < 10:
    print(numbers1[num])
    bla_bla=bla_bla+1
    num=num-1


#5

can = [1,2,3,4,5,6,7,8,9,10]

can1=0

can2=-1
#5-1
while can1 < len(can):
    print(can[can1])
    can1 = can1+1

#5-2
while can1 < len(can):
    print(can[can1])
    can1 = can1+1
    can2=can2-1


#6

leila=["nika","gio","saba","dato","bela"]

for i in range (1, len(leila), 2):
    leila[i]="can"

print(leila)

