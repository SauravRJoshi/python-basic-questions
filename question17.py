def multiply_items(input_list):
    multiply = 1
    for elements in input_list:
        multiply *= elements
    return multiply

input_number = []
try:
    while True:
        input_number.append(float(input("Enter a number or enter blank to finish ")))
except ValueError:
    pass
print(multiply_items(input_number))