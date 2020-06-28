def reverse_str(your_string):
    final_list = []
    for i in your_string[-1::-1]:
        final_list.append(i)
    
    return ''.join(final_list)

input_str = list(input("Enter a string : "))
print('Your reversed string is : ',reverse_str(input_str))