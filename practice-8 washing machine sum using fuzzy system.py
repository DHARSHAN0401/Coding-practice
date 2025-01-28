#Q8 washing machine works on the principle of Fuzzy System, the weight of clothes put inside it for washing is uncertain but based on weight measured by sensors and the water level chosen, it decides total time needed. 

def washing_machine():
    weight=int(input("enter the weight"))
    waterlevel=input("enter the water level")
    if weight<0:
        print("invalid weight")
    elif weight==0:
        print("time estimation is 0min")
    elif weight>7000:
        print("over load")
    else:
        if waterlevel=="L":
            if 0<weight<=2000:
                print("time estimation is 25mins")
        elif waterlevel=="M":
            if 2001<weight<=4000:
                print("time estimation is 35mins")
        elif waterlevel=="H":
            if 4001<weight<7000:
                print("time estimation is 45mins")
        else:
            print("invalid input")
    
#call the function
washing_machine()
    
    
