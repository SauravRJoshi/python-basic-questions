def return_length():
    input_list = []
    while True:
        a = ''
        a = input("Enter your chars for the list : ")
        if a:
            input_list.append(a)
        else:
            break
    
    final_value = 0
    for element in input_list:
        if len(element) > int(final_value):
            final_value = len(element)

    return final_value

print('The length of the longest word is',return_length())