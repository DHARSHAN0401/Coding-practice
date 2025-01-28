#Q9  addition and subtraction with them However, if any subtraction results in a negative number, display it as a positive value.

def add_and_subtract():
    num1=int(input("enter the number "))
    num2=int(input("enter the number "))
    
    add = num1+num2
    #calculate absolute value for addition using while loop
    abs_add = add
    while abs_add < 0:  
        abs_add = -abs_add
    opposite_add = -abs_add
    print("Addition of 2 values: ",(abs_add)or(opposite_add))
        
    sub= num1-num2
    #calculate absolute value for subtraction using while loop
    abs_sub=sub
    while abs_sub < 0: 
        abs_sub = -abs_sub
    opposite_sub = -abs_sub
    print("Subtraction of 2 values: ", (abs_sub)or(opposite_sub))
        
#call the function
add_and_subtract()

    
