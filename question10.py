def odd_index(input_str):
    final_list = input_str[1::2]
    return final_list

input_list = list(input("Enter a string :"))
print(odd_index(input_list))