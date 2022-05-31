a=int(input("Your Price:"))
b=int(input("Actual Price:"))
if(b>a):
    print("Loss")
elif(a>b):
    print("Profit")
else:
    print("No NEt Margin")
