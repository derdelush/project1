def newTeam():
    file = open("d:/teams.txt", "w")
    #where d:/teams.txt = filepath
    for n in range(0, 5):
        print("Please type the name of a team: ")
        team = input() + "\n"
        file.write(team)
    file.close()

newTeam()

def readTeams():
    file = open("d:/teams.txt", "r")
    print("First team: " + file.readline())
    print("Second team: " + file.readline())
    file.close()

readTeams()
