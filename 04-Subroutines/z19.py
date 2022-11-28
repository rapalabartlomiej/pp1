def f(max,min,liczba):
    pomoc = 0
    if min>max:
        pomoc = max
        max = min
        min = pomoc
    print(liczba)
    if liczba >= min and liczba <= max:
        return True
    return False
print(f(10,1,10))