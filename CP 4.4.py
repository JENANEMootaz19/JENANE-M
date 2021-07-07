a=input("donner une liste séparé par - :")
def separ(m):
        b=m.split("-")
        
        b=sorted(b)
        
        x="-".join(b)
       
        return x
        

result=separ(a)
print(ord("§"))
print(result)
