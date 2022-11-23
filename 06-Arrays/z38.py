def create_2d_arr(x,y):
    a = []
    for i in range(0,x):
        a.append([])
        for j in range(0,y):
            a[i].append("0")
        
    
    
    print(a)
    return a
create_2d_arr(3,5) 