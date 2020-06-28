str_input = input("Enter a char : ")
starts_with = lambda x: "It is a number" if x in "0123456789" else "It is not a number"
print(starts_with(str_input))