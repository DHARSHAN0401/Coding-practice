def grade():
    mark=int(input("enter the marks : "))
    if mark>=90:
        print("grade A")
    elif mark>=80:
        print("grade B")
    elif mark>=70:
        print("grade c")
    elif mark>=60:
        print("grade D")
    else:
        print ((mark),"is fail")
#call function:        
grade()