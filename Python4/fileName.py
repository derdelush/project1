file = open("d:/filename.txt", "r")

outfile = ""
for line in range(10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()
file = open("d:/filename.txt", "w")
file.write(outfile)
file.close()
