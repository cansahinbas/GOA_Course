#1
numbers = [1,2,3,4,5]

for i in range(5):
    bla=int(input("neter numbers: "))
    numbers.append(bla)

print(numbers)

#2
numbers = [1,2,3,4,5]

numbers.insert(4,"can")
numbers.insert(5,"15")
numbers.insert(0,170)
numbers.append(6)

print(numbers)