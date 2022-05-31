a=int(input("Principle Amount is:"))
b=float(input("Rate is:"))
c=float(input("Time span in year is:"))
amount=a*(1+b/100)**c
print(amount-a)