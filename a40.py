a=int(input("Smallest Range of Number is:"))
b=int(input("Biggest Range of Number is:"))
sum=0
for i in range(a,b+1):
    if(i<=0):
        sum+=i
    else:
        continue
print(sum)
    
    