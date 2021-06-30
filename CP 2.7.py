x=int(input("Enter a number"))
if (x>=500):
	x=x*0.5
elif (200<x<500):
        x=x*0.3
elif (x<200):
        x=x*0.1
        
print(x)
