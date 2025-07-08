#1
def hello_world():
    print("hello world")

hello_world()

#2
def hello_name(name):
    print("hello " + name)

hello_name("can")

#3
def numbers_plus(a,b):
    print(str(a) + " + " + str(b) + " = " + str(a+b))

numbers_plus(15,21)
numbers_plus(32,90)
numbers_plus(13,30)

#4
def Even_or_odd(num):
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

Even_or_odd(4)
Even_or_odd(5)
Even_or_odd(231)

#5
def numbers_list(sia):
    rezult = 0
    for i in sia:
        rezult += i
        
    print(rezult / len(sia))

numbers_list([12,12,40,30])
numbers_list([3,1,23,1,3,1,31,321,32])

#6
def striqoni(s):
    print(len(s))

striqoni("jdsbnauid absui ashd iusaghbioud sja")

#7
def big_word(words):
    print(words.upper())

big_word("I am jose morinjo")

#10
def numebrs_big(a,b):
    if a > b :
        print(str(a) +" biger den " + str(b))
    else:
        print(str(b) +" biger den " + str(a))

numebrs_big(1111,2221)
numebrs_big(143,212)
numebrs_big(19,21)
numebrs_big(16,23)

#11
def true_or_folse(num):
    if num > 1:
        print("True")
    else:
        print("false")

true_or_folse(4)
true_or_folse(-4)
true_or_folse(90)
true_or_folse(-2131)

#12
def grzeli(sia):
    grzeli1 = ""

    for i in sia:
        if len(i) > len(grzeli1):
            grzeli1 = i

    print(grzeli1)

grzeli(["d asd asdas","dsa d asd asd as"," dasd asd asd a"])

#13
def luzi(mdebare):
    rezultati = []

    for ricxvi in range(1, mdebare + 1):
        if ricxvi % 2 == 0:
            rezultati.append(ricxvi)
    
    print(rezultati)

luzi(12)
luzi(321)

#14
def damatebiti_xmovnebi(teksti):
    xmovnebi = "aeiouAEIOU"
    raodenoba = 0

    for simbolo in teksti:
        if simbolo in xmovnebi:
            raodenoba += 1

    print(raodenoba)

damatebiti_xmovnebi("d sad asd sada s")