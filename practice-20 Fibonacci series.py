#Q20 fibonacci series.

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
#call function:
n=int(input("enter the number:"))
print(fibonacci(n))
