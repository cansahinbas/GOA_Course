#1
can = input("enter proposal: ")

result=""
bosluk=" "
doruluk=False

for i in can:
    if i != bosluk:
        if doruluk:
            result += i.upper()
            doruluk=False
        else:
            result += i.lower()
    else:
        doruluk = True

print(result)

 