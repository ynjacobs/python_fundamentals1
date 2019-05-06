distance = 0
answer = ""
while answer != "quit":
    print("Would you like to walk or run or quit?")
    answer = input()
    if answer == "walk":
        distance += 1
       
    elif answer == "run":
        distance += 5
        
    print("Distance from home is {} km".format(distance))
