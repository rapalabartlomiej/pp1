def f(a,b):
    pomoc = 0
    for i in range(0,len(a)):
         for j in range(0,len(b)):
             if a[i] == b[j]:
                 pomoc+=1
                 break        
        
    if len(a)==pomoc:
        return True
    else:
        return False
    



b = [1,2,3,6]
a = [1,2,1,2,2,1,1]
print(f(a,b))
