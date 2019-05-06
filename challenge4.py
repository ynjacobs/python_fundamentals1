secret_number = 18

print("please enter a number")
number = input()

if int(number) == 18:
    print("You Win!")

elif int(number) == 17 or int(number) == 19:
    print("So close!")

else:
    print("Try again")
