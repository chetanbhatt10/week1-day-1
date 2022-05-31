a=int(input("Numbers upto:"))
sume=0
sumo=0
for i in range(1,a+1):
    if(i%2==0):
        sume+=i
    elif(i%2!=0):
        sumo+=i
print("Sum of Even NUmbers is:",sume)
print("Sum of Odd NUmbers is:",sumo)       