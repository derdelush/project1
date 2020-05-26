def characters():
    file = open("d:/teams.txt", "r")
    file.seek(24)
    #where 24 is number of characters from the start of the file
    print(file.read(2))
    file.close()
    return

characters()
