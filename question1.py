def count_string(get_string):
    my_dict = {}
    for i in get_string[0:]:
        my_dict.update( {i : get_string.count(i)} )
    
    return my_dict
    
input_string = input("Enter a string : ")
print(count_string(input_string))