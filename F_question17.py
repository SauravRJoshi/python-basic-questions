str_input = input("Enter a char : ")
starts_with = lambda x: "Starts with the char" if x.startswith(str_input) else "Doesn't start with the char"
str_to_check = input("Enter the string to check : ")
print(starts_with(str_to_check))