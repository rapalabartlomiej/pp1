array = [1, 2, 3, 4, 5]
array[0] -= 1 
array[-1] += 4
array[len(array)//2] *= 2
for i in range(len(array)):
    array[i] += 3
print(array)