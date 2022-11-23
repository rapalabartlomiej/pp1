def scnd(a):
    max_value_a = max(a)
    while  max(a)==max_value_a:
        a.remove(max_value_a)
    
    
    return max(a)


arr = [6,1,9,9,1]
print(scnd(arr))