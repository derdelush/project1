file = open("d:/ASD.txt", "a")
for n in range(1, 11):
    newline = "This is line " + str(n) + "\n"
    file.write(newline)
file.close()
