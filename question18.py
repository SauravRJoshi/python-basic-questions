def get_largest(input_list):
    h = input_list[0]
    for i in range(0,len(input_list)):
        if h > input_list[i]:
            pass
        else:
            h = input_list[i]
    return h

input_list = []
try:
    while True:
        input_list.append(int(input("Enter numbers or press enter without input to find largest : ")))
except ValueError:
    pass
print("Your list of inputs are : ",input_list)
print('The largest number from the list is : ',get_largest(input_list))