file = open('countries.txt','r')
file_content = file.read()

filess = file_content.readlines()

for line in filess:
     print(line, end="")

file.close()
