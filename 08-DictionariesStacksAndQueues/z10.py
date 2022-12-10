array = [{
    "name":"Poland",
    "population" : 123331
},
{
    "name":"francja",
    "population" : 123411
},
{
    "name":"niemcy",
    "population" : 123331
},
{
    "name":"wlochy",
    "population" : 11331
},
{
    "name":"albANIA",
    "population" : 123846331
}

]
lenght = len(array)
while lenght>0:
    for k,v in array[lenght-1].items():
        print(k,":",v)
    print("")
    
    lenght=lenght-1
