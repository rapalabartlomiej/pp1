def f(a):
    pomoc = a[0]
    a[0] = a[len(a)-1]
    a[len(a)-1] = pomoc
    return a
        
def pokaz(a):
    for i in range(0,len(a)):
        print(a[i])


a= [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
pokaz(a)
print("")
pokaz(f(a))