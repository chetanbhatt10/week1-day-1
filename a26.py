import math
a=int(input("constant with square term:"))
b=int(input("constant with linear:"))
c=int(input("constant with no power of x:"))
r1=(-b-math.sqrt(b*b-4*a*c))/2*a
r2=(-b+math.sqrt(b*b-4*a*c))/2*a
print("First Root is:",r1)
print("Second Root is:",r2)
