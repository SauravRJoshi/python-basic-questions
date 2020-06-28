def get_smallest(input_list):
    h = input_list[0]
    for element in range(0,len(input_list)):
        if h < input_list[element]:
            pass
        else:
            h = input_list[element]
    return h

input_list = []
try:
    while True:
        input_list.append(int(input("Enter numbers or press enter to find smalles : ")))
except ValueError:
    pass
print("The smallest number from your inputs is : ",get_smallest(input_list))