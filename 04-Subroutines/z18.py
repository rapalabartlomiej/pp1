def f(liczba):
    liczba = str(liczba)
    suma = 0 
    for i in range(len(liczba)):
        suma = suma + int(liczba[i])
    return suma
        

print(f(7182))