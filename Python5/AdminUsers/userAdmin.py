
import subprocess
import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = str(input("Please enter the name of the user to add: "))
        print ("Use the username '" + username + "'? (Y/N)")
        confirm = str(input("")).upper()
        os.system("sudo adduser " + username)
        return

def del_user():
    confirm = "N"
    while confirm != "Y":
        username = str(input("Please enter the name of the user to remove: "))
        print ("Remove the username '" + username + "'? (Y/N)")
        confirm = str(input("")).upper()
        os.system("sudo userdel -r " + username)
        return

def add_user_to_group():
    username = str(input("Please enter the name of the user that you wish to add to a group: "))
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0].decode("utf-8").strip()
    print("Please input a list of groups to add the user to")
    print("The list should be separated by spaces")
    print("The available groups are: " + output)
    chosenGroups = str(input("Groups: "))
    output=output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    print("Add to: ")
    found = True
    groupString = ""
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("- Existing Group: " + grp)
                groupString = groupString + grp + ","
        if found == False:
                print("- New Group:" + grp)
                groupString = groupString + grp + ","
        else:
            found = False

    groupString = groupString[:-1] + " "

    while True:
        print ("Add user '" + username + "' to the groups above? (Y/N)")
        confirm = str(input("")).upper()
        if confirm == "N":
            break
        if confirm == "Y":
            os.system("sudo usermod -aG " + groupString + username)
            break
    return
