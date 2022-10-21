wzrost = input("Enter your height1 in cm ")
waga = input("Enter your weight in kg ")
wzrost = float(wzrost)
waga = float(waga)

wzrost = wzrost*wzrost
waga = waga/wzrost
waga = waga*10000
print(f"BMI index: {waga}")

if waga>19.5 and waga < 24.99:
    print("waga prawidlowa")
else :
    print("waga nieprawidlowa")
