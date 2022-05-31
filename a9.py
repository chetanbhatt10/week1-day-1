a=int(input("First Number is:"))
b=int(input("Second Number is:"))
c=int(input("Third Number is:"))
if(a>=b):
    if(c>=a):
        print("Greatest Number is:",c)
    else:
        print("Greatest Number is:",a)
else:
    if(b>=c):
        print("Greatest NUmber is:",b)
    else:
        print("Greatest Number is:",c)