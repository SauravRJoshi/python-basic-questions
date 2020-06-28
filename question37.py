my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
keys_prod = 1
values_prod = 1
for i in keys_list:
    keys_prod *= i 
for j in values_list:
    values_prod *= j


print("The product of keys : ",keys_prod)
print("The product of keys : ",values_prod)
print("The product of all items in the list :",keys_prod*values_prod)