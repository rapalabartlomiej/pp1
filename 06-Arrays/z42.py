def f(a):
    pomoc = 0
    for i in range(0,len(a)):
        pomoc = a[i][0]
        a[i][0] = a[i][len(a[0])-1]
        a[i][len(a[0])-1] = pomoc
    return a
       
        
def pokaz(a):
    for i in range(0,len(a)):
        print(a[i])


a= [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
pokaz(a)
print("")
pokaz(f(a))