import random
def rand_elem(array):
    a = random.randint(0,len(array)-1)
    return array[a]



a = [4,2,8,4,7,9,5]
print(rand_elem(a))
print(rand_elem(a))
print(rand_elem(a))
print(rand_elem(a))