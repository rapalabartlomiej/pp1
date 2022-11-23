def f(a,b):
    for i in range(0,len(b)):
        if a == b[i]:
            return ""
    return a
    
    
    
    
a = [4,36,12,28,9,44,5] 
b = [5,1,36]
c = ""
for i in range(0,len(a)):
    c = f(a[i],b)
    if c != "":
        print(f"{c} ",end = "")