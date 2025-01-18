#Q5 remove the duplicates from the list :
  
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:  # Add item only if it's not already in result
            result.append(item)
            return result
        else :
            return false
           

# Input
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("List without duplicates:", remove_duplicates(numbers))
