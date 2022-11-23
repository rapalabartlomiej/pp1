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
def median(array):
    bubblesort(array)
    if len(array)%2 == 1:
        return array[int(((len(array)+1)/2)-1)]
    else:
        return (array[int(len(array)/2)]+array[int(len(array)/2)-1])/2
print(median([1,0,9,6,4.25]))