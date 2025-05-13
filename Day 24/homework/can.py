count = 0
product = 1

while count < 5:
    print("enter number :")
    number = int(input())
    product *= number
    count += 1

print(product)