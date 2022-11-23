def f(a,b):
    if len(a) != len(b):
        return False
    for i in range(0,len(a)):
        if a[i] != b[i]:
            return False  
    return True
a = ["water","book","sky"]
b = ["water","book","sky"]
print(f"array1: {a}")
print(f"array2: {b}")
if f(a,b):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are not the same")