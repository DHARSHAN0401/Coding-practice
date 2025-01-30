#Q15 to check if a number is a perfect number:

def is_perfect_number(num):
    if num <= 1:
        return False
    sum_divisors = 0
    for i in range(1, num // 2 + 1):
        if num - (num // i) * i == 0:  
            sum_divisors += i
    return sum_divisors == num

# Test cases
num = int(input("Enter a number: "))  
if is_perfect_number(num):
    print("true") 
else:
    print("false")  
