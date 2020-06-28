def unique_list(input_set):
    return list(sorted(set(input_set)))


def take_list_input():
    input_list = []
    while True:
        a = ''
        a = input("Enter your chars for the list : ")
        if a:
            input_list.append(a)
        else:
            break
    return input_list

the_input = take_list_input()
print("Your input list : ",the_input)
print("The uniqe list : ",unique_list(the_input))