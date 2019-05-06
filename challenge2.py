print("please enter your age")
age = input()

if int(age) <= 21:
    print("I am {} years older than you".format(21- int(age)))
elif int(age) <=105:
    print("I am {} years younger than you".format(int(age)- 21))
elif int(age) > 105:
    print("I'm not sure I believe you")