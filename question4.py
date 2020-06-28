input_string = list(input("Enter a string,seperated by comma : "))
final_string = []

final_string[::] = input_string[::]

input_string_1st_char = input_string[0:2]
comma_index = input_string.index(",")
input_string_2nd_char = input_string[comma_index + 1:comma_index + 3]


final_string[:2] = input_string[comma_index + 1:comma_index + 3]
final_string[comma_index + 1:comma_index + 3] = input_string[0:2]

print(''.join(final_string))