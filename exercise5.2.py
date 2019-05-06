distance = 0
answer = ""
energy_increment = 2
energy = 0
while True:
    print("Would you like to walk or run or quit?")
    answer = input()

    if answer == "walk":
        distance += 1
        energy +=1
        
        
       
    elif answer == "run":
        if energy - energy_increment < 0:
            print("You can't run")
            continue
        distance += 5
        energy -= energy_increment

    elif answer == "quit":
        print("bye")
        break

    else:
        print("I dont understand")
        continue

    print("your engery level is {}".format(energy))
        
    print("Distance from home is {} km".format(distance))
        
print("Finished")
    
