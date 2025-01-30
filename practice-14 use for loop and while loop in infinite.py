#Q14 using a for loop and another using a while loop print the infinite condition :
def infinite_for_loop():
    num = 1
    for _ in iter(int, num):  
        print("This is an infinite for loop!")
        
def infinite_while_loop():
    while 1:  
        print("This is an infinite while loop!")


print("Choose an infinite loop to run:")

#test case:

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    infinite_for_loop()
elif choice == "2":
    infinite_while_loop()
else:
    print("Invalid choice! Please enter 1 or 2.")
