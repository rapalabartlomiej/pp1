file = open('ell.txt','w')
array = ["Batman","ironman","shrek","skher3","shrek2"]
for i in array:
    file.write(i)
    file.write("\n")
file.close()