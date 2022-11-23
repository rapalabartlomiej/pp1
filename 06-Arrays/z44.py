def transpose_matrix(m):
    pomoc = create_2d_arr(len(a[0]),len(a))
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            pomoc[j][i] = m[i][j]  
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
        
a = [[1,2,3,4,5],[6,7,8,9,0]]
pokaz(transpose_matrix(a))