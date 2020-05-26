file = open("d:/filename.txt", "r")
contents = list(file.readlines())
file.close()

contents[0] = ("This is a newline \n")

file = open("d:/filename2.txt", "w")
file.write("".join(contents))
file.close()
