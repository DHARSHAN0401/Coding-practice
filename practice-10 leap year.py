#Q10 leap year.
def leap_year():
    a=int(input("enter the year "))
    if(a%4==0 and a%100!=0)or(a%400==0):
        print((a),"this is leap year")
    else:
        print("not leap year")
        
#call the function.
leap_year()
