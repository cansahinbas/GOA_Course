#1

#ფუნქციის შესაქმნეწლად ვიყენებთ def keyword-ს მერე ვუწერეთ ნებისმიერ სახელს და ბოლოს ფრჩხილები და ორი წერტილი

#2

def numbers_jami(a,b):
    print(str(a) + " + " + str(b) + " = " + str(a+b))

numbers_jami(5,7)
numbers_jami(4,12)
numbers_jami(9,4)
numbers_jami(312,2311)

#3

def even_or_odd():
    user_input=int(input("enter numbers: "))
    if user_input % 1 == 0:
        print("რუსცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

even_or_odd()

#4

def numbers_kvadrat(numbers):
    print(str(numbers) + " კვადრატია = " + str(numbers*numbers))
    
numbers_kvadrat(3)
numbers_kvadrat(85)
numbers_kvadrat(7)
numbers_kvadrat(25)
numbers_kvadrat(12)

#5

def words(w):
    print(w.upper())

words("bla_blabla")

#6

def name_username(name,username):
    print("youre name is so good " + name + "and not same usrname " + username)

name_username("can","sahinbas")