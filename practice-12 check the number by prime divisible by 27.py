# Q12 write a program that check whether this number can be divided evenly by 27. 

def is_multiple_of_27(num):
    remainder = num
    while remainder >= 27:
        remainder -= 27  
    return remainder == 0
#test case:
num = int(input("Enter a number: "))
if is_multiple_of_27(num):
    print((num),"is a multiple of 27.")
else:
    print((num),"is not a multiple of 27.")

