a = int(input("Enter the year: "))

if (( a%400 == 0)or (( a%4 == 0 ) and ( a%100 != 0))):
    print(f"{a} is a Leap year")
else:
    print(f"{a} is Not a leap")
