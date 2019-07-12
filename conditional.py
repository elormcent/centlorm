i = 6
if(i % 2 == 0):
    print ("Even Number")
else:
    print ("Odd Number")


def even():
    number = int(input("Enter a whole number :- "))
    if (number > 0 % 2 == 0):
        print("It\'s an even number, nice work")
    elif (number > 0 % 2 == 1):
        print("it\'s an odd number, good job")
    elif (number == 0):
        print("you entered \'0' 'Zero'")
    elif (number < 0 ):
        print("you entered a negetive number")
    else:
        print("Enter a number greater than \'0' 'Zero'")
                 

even()
    
    
