#1
def even_or_odd():
    user_input=int(input("enter numbers: "))
    if user_input % 1 == 0:
        print("რუსცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

even_or_odd()


#2

def name_list():
    list=[]

    for i in range(5):
        can=input("enter name: ")
        list.append(can)

    print(list)

name_list()

#3

def even_or_odd(numbers):
    bla = 0
    for i in range(1 , numbers + 1):
        print(i) 

even_or_odd(5)

#4

def number_bla(numbers):
    result = 0
    for  i in range(numbers + 1, numbers+100):
        if i % 2 == 0:
            result += 1
        if result == 1:
            print(i)

number_bla(10)