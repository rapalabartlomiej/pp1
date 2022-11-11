import string


def numberss():
    for i in range(1,10):
        if i%3==0:
            print(i)
        else:
            print(i,end=" ")
numberss()



def num(a):
    b=a*a
    for i in range(1,b+1):
        if i%a==0:
            i = str(i)
            print(i.zfill(2))
        else:
            i = str(i)
            print(i.zfill(2),end=" ")
num(3)
