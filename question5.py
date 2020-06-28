def add_str(input_str,copy_str):
    if len(input_str) < 3:
        pass
    else:
        if input_str[-1] == 'g' and input_str[-2] == 'n' and input_str[-3] == 'i':
            copy_str.append('l')
            copy_str.append('y')
        else:
            copy_str.append('i')
            copy_str.append('n')
            copy_str.append('g')
    return copy_str

input_str = list(input("Enter a string :"))
copy_str = input_str
final_str = ''.join(add_str(input_str,copy_str))
print(final_str)