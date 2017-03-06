bin_file = open("boss.bin", 'rb')
file1 = open("L11_lo.txt", 'w')
file2 = open("L11_hi.txt", 'w')
f = True
for i in bin_file:
    for j in i:
        print(str(j))
        buf = str(hex(j))[2:]
        if len(buf) == 1:
            buf = '0'+buf
        if f:
            file1.write(buf+'\n')
        else:
            file2.write(buf+'\n')
        f = not f
bin_file.close()
file1.close()
file2.close()
