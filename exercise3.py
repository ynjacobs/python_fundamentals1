print("What is your name?")
user_name = input()
print("Hello, {}".format(user_name))

secret_password = "please"

print("What's the password?")
password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print("That's {}!".format(correct_or_not))

print("How old are you?")
age = input()

print("You were born in {}".format(2019 - int(age)))