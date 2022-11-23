def occurs(number, array):
     for i in range(0,len(array)):
         if number == array[i]:
             return True
     return False
a = 24
b = [15,38,7,23,14]
print(f"Number: {a}")
print(f"array: {b}")
if occurs(a,b):
    print(f"Result: number {a} appears in the array")
else:
    print(f"Result: number {a} do not appears in the array")