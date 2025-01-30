#Q23 sum of squares.

def sum_of_squares(n):
    count=0
    for i in range(1,(n+1)):
        count+=(i**2)
    return count

#test case:
n=int(input("enter the number:"))
print(sum_of_squares(n))  
