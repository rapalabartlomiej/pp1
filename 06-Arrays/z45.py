def onedeme(a):
    pomoc = 0
    tab = []
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            tab.append(int(a[i][j]))
            
    return tab 



a = [[1,2,3,4,5],[6,7,8,9,0],[23,12,1,2]]
print(onedeme(a))