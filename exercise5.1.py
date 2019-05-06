distance = 0
answer = ""
while answer != "go home":
    print("Would you like to walk or run or go home?")
    answer = input()
    if answer == "walk":
        distance += 1
        print("Distance from home is {} km".format(distance))
    elif answer == "run":
        distance += 5
        print("Distance from home is {} km".format(distance))

    elif answer !="go home":
        print("you have entered a command that does not exist")