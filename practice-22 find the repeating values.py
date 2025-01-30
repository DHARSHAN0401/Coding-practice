#Q22 find the repeated values.

def find_repeated_values(n):
    repeated = []
    seen = set()
    
    for i in n:
        if i in seen:
            repeated.append(i)
        else:
            seen.add(i)
    return repeated

# test case
n= [1, 2, 3, 4, 2, 3, 5]
print(find_repeated_values(n))
