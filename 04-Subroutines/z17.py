def f(nazwa,litera):
    licznik = 0
    for i in range(len(nazwa)):
        if nazwa[i] == litera:
            licznik += 1
    return licznik
    
print(f("You never get a second chance to make a first impression","e"))