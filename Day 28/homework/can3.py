number = int(input("enter  number"))
is_prime =True

for i in range(2,number):
    if number % i ==0:
        is_prime=False

if is_prime:
    print("Wthis is prime number")
else:
    print("this isn't prime number")