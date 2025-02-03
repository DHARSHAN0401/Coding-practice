def is_armstrong():
    num=int(input("enter the number to check armstrong or not: "))
    num_str=str(num)
    num_digit=len(num_str)
    armstrong=0
    for i in num_str:
        armstrong+=int(i)**num_digit
    print((armstrong), "is armstrong")
is_armstrong()