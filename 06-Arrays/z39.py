a= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(0,len(a)):     
    for j in range(0,len(a[i])):
        if j == 0:
            a[i][j] = i+1
        else:
            a[i][j] =a[i][j-1]+a[i][0]   
         
print(a)