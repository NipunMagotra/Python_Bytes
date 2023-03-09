
user_input = input("")

no_spaces = user_input.replace(" ", "")

length = len(no_spaces)


output = "S{} ({})".format(length, user_input.replace(" ", ""))


print(output)
