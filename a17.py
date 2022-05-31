rng=int(input("Maximum NUmber of rnage is:"))
rngs=int(input("Minimum NUmber of range is:"))
for i in range(rngs,rng+1):
    if(i>0):
        print("Positive")
    elif(i<0):
        print("Negative")