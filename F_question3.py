def mult_list(your_list):
    mul = 1
    for i in your_list:
        mul *= i
    return mul

sample_list = [8, 2, 3, -1, 7]
print('The multiplied reuslt is : ',mult_list(sample_list))