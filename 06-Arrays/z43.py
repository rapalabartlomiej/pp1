def identity_matrix(n):
    pomoc = create_2d_arr(n,n)
    pomoc = jedynki(pomoc)
    return pomoc

def create_2d_arr(x,y):
    a = []
    for i in range(0,x):
        a.append([])
        for j in range(0,y):
            a[i].append("0") 
    return a


def pokaz(a):
    for i in range(0,len(a)):
        print(a[i])

def jedynki(a):
    for i in range(0,len(a)):
        a[i][i] = '1'
    return a
        

pokaz(identity_matrix(3))
print("")
pokaz(identity_matrix(5))
print("")
pokaz(identity_matrix(8))
