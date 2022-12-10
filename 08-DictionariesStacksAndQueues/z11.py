import json

with open["z10.json"] as file:
    data = json.load(file)
for i in data:
    for k,v in i.items():
            print(k,":",v)