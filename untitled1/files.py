l = [str(i)+str(i-1) for i in range(20)]
f = open("file.txt", "w")
for index in l:
    f.write(index + '\n')
f.close()
k = open("file.txt", "r")
print(k.read())
k.close()
