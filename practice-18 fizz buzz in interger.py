#Q18 fizz buzz, which is divisible by 3 and 5 in a string .

def fizz_buzz():
    num=int(input("enter the numbers :"))
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            print("fizz buzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(str(i))

#call function:
fizz_buzz()
