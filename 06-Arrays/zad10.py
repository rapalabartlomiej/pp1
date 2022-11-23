def f(x):
    even = 0
    odd = 0
    for i in range(len(x)):
        if x[i]%2 ==1:
            odd+=1
        else:
            even+=1
    return f"odd {odd} even {even}"
array = [1,1,0,0,1,1,2,-1,0]
print(f(array))