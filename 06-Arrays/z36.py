def printerr(a):
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            print(f"{a[i][j]} ",end="")
        print("")
a = [[1,2,3,4],[5,6,7,8]]
printerr(a)