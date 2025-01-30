#Q16 find the single number in the array

def find_single_number(nums):
    result = 0
    for i in nums:
        result = result ^ i  
    return result

#test case:
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Single number:", find_single_number(nums))
