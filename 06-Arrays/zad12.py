array = [[2,5,4],[9,0,3]]
print(array)
print(f"{len(array)} na {len(array[0])}")
print(array[0][1])
print(array[1][2])
print(*array[1], sep=", ")
print("------")
for i in range(len(array)):
    print(*array[i], sep=", ")
print("------")
for i in range(len(array)):
    print(array[i][-1])