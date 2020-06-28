def print_even(your_list):
    even_list = []
    for elements in your_list:
        if int(elements)%2 == 0:
            even_list.append(int(elements))

    return even_list

def take_list_input():
    input_list = []
    while True:
        a = ''
        a = input("Enter your numbers for the list : ")
        if a:
            input_list.append(a)
        else:
            break
    return input_list

the_input = take_list_input()
print('The list with even numbers is : ',print_even(the_input))