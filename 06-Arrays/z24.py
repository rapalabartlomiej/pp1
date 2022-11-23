def f(a,arrr):
    pomoc = 0
    for i in range(0,len(arrr)):
        if arrr[i]==a:
            pomoc += 1
    if pomoc == 1:
        return True
    return False

array = [2,3,2,5,8,1,9,8]
unique = []
for i in range(0,len(array)):
    if f(array[i],array):
        unique.append(array[i])
print(unique)

