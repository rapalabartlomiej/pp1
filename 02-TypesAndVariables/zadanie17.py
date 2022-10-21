cm = float(input("podaj wzrost w cm: "))
inch = cm/2.54
feet = 0
while(inch >12):
    feet= feet +1
    inch = inch-12
inch = int(round(inch, 0))
cm = int(round(cm, 0))
print(f"I am {cm} tall, i.e. {feet} feet and {inch} inches.")    
