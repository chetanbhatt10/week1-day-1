

while(True):
    a=int(input("First Number is:"))
    b=int(input("Second Number is:"))
    operation=int(input("Which operation you wants to do? '1' for 'Addition','2' or 'Subtraction','3' for 'Multiplication','4' for 'Division':"))
    if(operation==1):
        print(a+b)
    elif(operation==2):
        print(a-b)
    elif(operation==3):
        print(a*b)
    elif(operation==4):
        print(a/b)
    again=int(input("Do you want to calculate again? '1' for 'yes' and '0' for 'no'"))
    if(again==0):
        break