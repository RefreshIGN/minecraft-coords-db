import numpy as np
import sys

#Creates the file if not already existent, adds data to every line
#I'd like to line up the "|" character if the list includes instances with a different number of digits
try:
    open("coords.txt","x")
    with open("coords.txt","a") as a:
        for i in range(10000):
            a.write(str(i) + "| EMPTY\n")
except:
    pass

try:
    open("settings.txt","x")
except:
    pass

coords_list = [x.strip() for x in open("coords.txt","r").readlines()]

with open("settings.txt","r") as st:
    try:
        inc = int(st.read())
    except:
        with open("settings.txt","w") as ts:
            inc = 10
            ts.write(inc)
pg = inc

print("This is Alex_sta's Minecraft Coords Notebook!\nType 'help' for commands.\n")

#Central input function
def help():
    global inputs
    global pg
    inputs = input("")
    if inputs.lower() == "help":
        print("Type 'Write' to add or change a coordinate \nType 'Read' to see list of coordinates \nType 'Find' to find a coordinate saved on a specific line \nType 'Settings' to change a see and edit the settings.\n")
        help()
    elif inputs.lower() == "write":
        writelist()
    elif inputs.lower() == "read":
        viewlist()
    elif inputs.lower() == "settings":
        settings()
    elif inputs.lower() == "find":
        find = input("What line is the coordinate on?: ")
        checkint(find)
        print(coords_list[find])
        help()
    elif inputs.lower() == "next":
        pg += inc
        viewlist()
    elif inputs.lower() == "prev":
        pg -= inc
        if pg <= -1:
            pg = 0
            print("You cannot go under 0, please use the command 'Next' to return to the list.\n")
        viewlist()
    else:
        print("That's not a recognized command, please try again.\n")
        print("Type 'help' for commands.\n")
        help()

#Checks if the inputed value is an integer
def checkint(d):
    global check
    d = str(d)
    check = 0
    if d[0] == "-":
        check = 1
    else:
        check = 0
    if d[check:].isdigit() == True:
        pass
    else: 
        raise Exception("That isn't an integer. Please insert an integer.")
        sys.exit(1)

#Checks the first instance of an empty value in coords.txt
def checklast():
    for h in range(len(coords_list)):
        for j in range(len(coords_list[h])):
            if coords_list[h][j] == "|":
                if coords_list[h][j+1:] == " EMPTY":
                    return h
                else:
                    pass

#Edits the text file directly to make it act as a database
def writelist():
    global x, y, z
    x = input("What is the X coordinate?: ")
    checkint(x)
    y = input("What is the Y coordinate?: ")
    checkint(y)
    z = input("What is the Z coordinate?: ")
    checkint(z)
    name = input("What name would you like to associate with the coordinate?: ")
    option = input("Type 'append' to append the coordinate to the end of the list. Put in a number if you would like to save the coordinate on a specific line\n")
    if option.lower() == 'append':
        append = 1
    else:
        checkint(option)
        print(option)
        append = 0
    with open("coords.txt","r"):
        if append == 1:
            for k in range(len(coords_list)):
                if coords_list[k].find("EMPTY") != -1:
                    coords_list[k] = str(k) + "| " + str(x) + ", " + str(y) + ", " + str(z) + ", " + name
                    divineduplicationblast()
                    print(coords_list[k])
                    break
        elif append == 0:
            if coords_list[int(option)].find("EMPTY") <= 0:
                choice = input("There is already a coordinate stored here. Would you like to override it? (Yes/No): ")
                if choice.lower() == "yes":
                    coords_list[int(option)] = str(int(option)) + "| " + str(x) + ", " + str(y) + ", " + str(z) + ", " + name
                    print(coords_list[int(option)])
                    divineduplicationblast()
                else:
                    help()
            else:
                coords_list[int(option)] = str(int(option)) + "| " + str(x) + ", " + str(y) + ", " + str(z) + ", " + name
                print(coords_list[int(option)])
                divineduplicationblast()
    help()

#Deletes the contents of the text file, then rewrites it from coords_list
def divineduplicationblast():
    with open("coords.txt","w") as coords:
        for l in range(len(coords_list)):
            coords.write(coords_list[l] + "\n")

#Uses this to show inc# of coordinates
def viewlist():
    for i in range(pg-inc,pg):
                if np.sign(i) >= 0:
                    print(coords_list[i])
    print("Type 'Next' or 'Prev' to go forward or backwards")
    help()

#Function to change setting. Maybe I'll add more, probably not
def settings():
    global inc
    with open("settings.txt","w") as st:
        st.write(str(inc))
    print("The current page increment is " + str(inc))
    settings_input = input("Use the command 'Increment' to edit the increment. \nUse the command 'exit' to exit to the main help menu.\n")
    if settings_input.lower() == "increment":
        inc = int(input("What would you like to change the input to?: "))
        checkint(inc)
        help()
    elif settings_input.lower() == "exit":
        help()
    else:
        print("That's not a recognized command.")
        settings()


help()