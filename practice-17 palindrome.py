#Q17 check the palindrome:

def is_palindrome(number):
    num_str= str(number)
    reversed_str=""
    for i in num_str:
        reversed_str=i+reversed_str
    if num_str == reversed_str:
        return True 
    else:
        return False 


#call function:
number = input("Enter to check the palindrome : ")
print(is_palindrome(number))
