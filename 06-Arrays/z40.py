def szukaj(array):
    min = array[0][0]
    pomocmin= [0,0] 
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            if array[i][j] < min:
                min = array[i][j]
                
                pomocmin[0] = i
                pomocmin[1] = j 
    
    max = min
    pomocmax= [0,0]
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            if array[i][j] > max:
                max = array[i][j]
                print(f"{i} + {j}")
                pomocmax[0] = i
                pomocmax[1] = j 
          
    print(f"min :{min} lokalizacja: {pomocmin}")
    print(f"min :{max} lokalizacja: {pomocmax}")
    
    
    



a = [[-38, 19], [5,40],[-3337,11],[2222229,16]]
szukaj(a)
