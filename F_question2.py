def sum_list(your_list):
    summ = 0
    for i in your_list:
        summ += i
    return summ

sample_list = [8,2,3,0,7]
print('The sum of the numbers in a list are : ',sum_list(sample_list))