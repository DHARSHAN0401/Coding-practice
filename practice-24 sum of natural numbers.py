#Q24 find sum of first n natural number.

def sum_of_natural_numbers(n):
    count=0
    for i in range(1, n + 1):
        count+=i
    return count

# test case:
n=int(input("enter the natural number:"))
print(sum_of_natural_numbers(n))
