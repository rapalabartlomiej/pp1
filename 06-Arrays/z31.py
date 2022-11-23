def odd_even(array,booo):
    booo = not(booo)
    for i in range(0,len(array)):
        if array[i]%2==booo:
            print(f"{array[i]} ",end="")
    print("")
    



a = [4,2,8,4,7,9,5]
odd_even(a,True)
odd_even(a,False)