def kreski(a):
    a = (len(a)*5)+1
    for i in range(0,a):
        print("-",end="")
    print("")

def uzupelnianie(a):
    for i in range(0,len(a)):
        if a[i]<10:
            a[i] = str(a[i])
            a[i] = "   "+a[i]+ "|"
        elif a[i]<100:
            a[i] = str(a[i])
            a[i] = "  "+a[i]+ "|"
        elif a[i]<1000:
            a[i] = str(a[i])
            a[i] = " "+a[i]+ "|"
    return a 



def srodek(a):
    print("|",end="")
    for i in range(0,len(a)):
        print(a[i],end="")
    print("")
    
    
    
          
array = [1,23,6,282,5,34,2,32,2,323]
kreski(array)
array = uzupelnianie(array)
srodek(array)
kreski(array)

