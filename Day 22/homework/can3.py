user_input=int(input("enter number:"))

for i in range(1,user_input+1,1):
    if user_input % i == 0: 
        print(i) 