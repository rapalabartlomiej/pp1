def bubblesort(array):
    for i in range(0,len(array)):
        array = sort(array,len(array)-i)
    return array

def sort(tab,dlogosc):
    pomoc = 0
    for i in range(0,dlogosc-1):
        if tab[i] > tab[i+1]:
            pomoc = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = pomoc
    return tab
    

a = [9,1,7,9,9,2,1,1]
print(bubblesort(a))