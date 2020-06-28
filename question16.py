def sum_list(input_list):
    the_sum = 0
    for element in input_list:
        the_sum = the_sum + element 
    return the_sum


final_list = []
the_sum = 0
try:
    while True:
        final_list.append(float(input("Enter a number or enter blank to finish ")))
except ValueError:
    print("done")
print('your input are',final_list)
print('The sum of the inputs is : ',sum_list(final_list))