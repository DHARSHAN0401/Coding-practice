#Q3 to check the prime number:

def is_prime(num):
    
    # Prime numbers start from 2
    if num < 2: 
        return False
    for i in range(2, int(num ** 0.5) + 1):
        
    # Check divisors up to √num
        if num % i == 0:
            return False
    return True

# Input from the user
num = int(input("Enter a number to check is prime or not: "))
if is_prime(num):
    print((num),"is a prime number.")
else:
    print((num), "is not a prime number.")
