def change_str(input_string):
    second = []
    second = input_string[0]
    input_string[0] = input_string[-1]
    input_string[-1] = second
    return input_string

input_string = list(input("Enter a string : "))
b = change_str(input_string)
print(''.join(b))